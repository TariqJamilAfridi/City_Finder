from flask import Flask, render_template, request, jsonify
from config import Config
from services.geocoding import get_city_area_id
from services.places_api import search_places

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/')
def index():
    return render_template('dashboard.html', 
                           city_name=app.config['CITY_NAME'],
                           recent_searches=[])

@app.route('/api/get-area-id')
def get_area_id():
    city = request.args.get('city', app.config['CITY_NAME'])
    
    area_id = get_city_area_id(city)
    if not area_id:
        return jsonify({"error": f"Could not find boundary for {city}"}), 404
    
    return jsonify({"area_id": area_id, "city": city})

@app.route('/api/search')
def api_search():
    category = request.args.get('category')
    city = request.args.get('city', app.config['CITY_NAME'])
    
    area_id = get_city_area_id(city)
    if not area_id:
        return jsonify({"error": f"Could not find boundary for {city}"}), 404
        
    results = search_places(area_id, category, city)
    
    if isinstance(results, tuple):
        return jsonify(results[0]), results[1]
    
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)