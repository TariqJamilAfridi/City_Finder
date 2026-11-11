from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from google.oauth2 import id_token
from google.auth.transport import requests as google_requests
from config import Config
from database.db import init_db, get_db_connection
from services.geocoding import get_city_area_id
from services.places_api import search_places

app = Flask(__name__)
app.config.from_object(Config)

with app.app_context():
    init_db()

def login_required(f):
    def wrap(*args, **kwargs):
        if 'user_id' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    wrap.__name__ = f.__name__
    return wrap

@app.route('/')
def index():
    if 'user_id' in session:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))

@app.route('/login')
def login():
    if 'user_id' in session:
        return redirect(url_for('dashboard'))
    return render_template('login.html', client_id=app.config['GOOGLE_CLIENT_ID'])

@app.route('/auth/google', methods=['POST'])
def google_auth():
    token = request.json.get('token')
    try:
        idinfo = id_token.verify_oauth2_token(
            token, google_requests.Request(), app.config['GOOGLE_CLIENT_ID']
        )
        
        google_id = idinfo['sub']
        email = idinfo['email']
        name = idinfo['name']
        picture = idinfo.get('picture', '')

        conn = get_db_connection()
        cursor = conn.cursor()
        
        user = cursor.execute('SELECT id FROM users WHERE google_id = ?', (google_id,)).fetchone()
        
        if not user:
            cursor.execute('''
                INSERT INTO users (google_id, name, email, profile_picture) 
                VALUES (?, ?, ?, ?)
            ''', (google_id, name, email, picture))
            conn.commit()
            user_id = cursor.lastrowid
        else:
            user_id = user['id']
            
        conn.close()

        session['user_id'] = user_id
        session['user_name'] = name
        session['user_picture'] = picture
        
        return jsonify({"status": "success", "redirect": url_for('dashboard')})
        
    except ValueError:
        return jsonify({"status": "error", "message": "Invalid token"}), 401

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/dashboard')
@login_required
def dashboard():
    conn = get_db_connection()
    recent = conn.execute('''
        SELECT DISTINCT search_category FROM search_history 
        WHERE user_id = ? ORDER BY searched_at DESC LIMIT 5
    ''', (session['user_id'],)).fetchall()
    conn.close()
    
    recent_searches = [r['search_category'] for r in recent]
    
    return render_template('dashboard.html', 
                           user_name=session['user_name'], 
                           user_picture=session['user_picture'],
                           city_name=app.config['CITY_NAME'],
                           recent_searches=recent_searches)

@app.route('/api/search')
@login_required
def api_search():
    category = request.args.get('category')
    city = app.config['CITY_NAME']
    
    area_id = get_city_area_id(city)
    if not area_id:
        return jsonify({"error": f"Could not find boundary for {city}"}), 404
        
    results = search_places(area_id, category)
    
    if isinstance(results, tuple):
        return jsonify(results[0]), results[1]
        
    conn = get_db_connection()
    conn.execute('''
        INSERT INTO search_history (user_id, search_category) VALUES (?, ?)
    ''', (session['user_id'], category))
    conn.commit()
    conn.close()
    
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)