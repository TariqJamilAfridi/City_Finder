# CityFinder - Smart City Location Discovery Platform

**Find places near you easily!** 🗺️📍

## 🌐 Live Demo

**Try it now:** https://city-finder-k1d6.onrender.com/

The application is deployed and fully functional - accessible from anywhere in the world!

---

CityFinder is a user-friendly web application that helps you discover essential locations and services in your city. Perfect for everyone - even if you've never used a computer before!

## 📖 Project Overview

### What Does This Project Do?
CityFinder helps you find important places like:
- 🍔 Restaurants and food places
- 🏥 Hospitals and clinics
- 🏦 Banks and ATMs
- 🏫 Schools and universities
- 🕌 Mosques and worship places
- ⛽ Petrol stations
- 💊 Pharmacies
- 🏨 Hotels
- 🛍️ Shopping malls
- 🌳 Parks
- 🚌 Bus stations

### Key Features

#### 📏 Distance Display
- Shows how far each place is from you
- Example: "2.5 km away" or "850 m away"
- Results sorted nearest first

#### 🗺️ Built-In Directions
- Click "Get Directions" on any place
- See the route on the map
- Shows distance and estimated time
- Turn-by-turn instructions

#### 🔤 Simple Mode
- Large text and buttons
- Easy to read
- Perfect for elderly users
- Toggle on/off anytime

#### 📚 Easy Interface
- Large, colorful category buttons with emoji icons
- Clear distance badges on every result
- Color-coded elements for easy recognition
- Icons everywhere for visual understanding

### Technologies & Libraries Used

**Backend:**
- Python 3.8+
- Flask 3.0.0 - Web framework
- python-dotenv 1.0.0 - Environment variables
- requests 2.31.0 - API calls with timeout handling

**Frontend:**
- HTML5, CSS3, JavaScript (ES6)
- Bootstrap 5.3.0 - Responsive design
- Leaflet.js 1.9.4 - Interactive maps
- Leaflet Routing Machine 3.2.12 - Route calculation
- Font Awesome 6.0.0 - Icons

**APIs Used:**
- OpenStreetMap Nominatim API - Geocoding and place search
- OSRM (Open Source Routing Machine) - Route calculation
- Browser Geolocation API - User location

### API Implementation Details

1. **Nominatim Geocoding API**
   - Endpoint: `https://nominatim.openstreetmap.org/search`
   - Used for: Finding city boundaries and searching places
   - Timeout: 10 seconds
   - Error handling: Fallback to demo data if API fails
   - Status code checking: Always validates response

2. **Place Search**
   - Searches for amenities within city boundaries
   - Returns: place name, coordinates, address
   - Timeout implemented: 15 seconds
   - Graceful degradation: Demo data available

3. **Error Handling**
   - All API calls use `timeout=` parameter
   - Status codes checked with `response.raise_for_status()`
   - Try-except blocks catch network errors
   - User-friendly error messages displayed
   - Application never crashes on API failure

## 🚀 Installation & Setup

### Quick Start - Use Live Demo

**No installation needed!** Just visit: https://city-finder-k1d6.onrender.com/

### For Local Development

#### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Modern web browser (Chrome, Firefox, Edge, Safari)

#### Step 1: Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/CityFinder.git
cd CityFinder
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Configure Environment
Copy `.env.example` to `.env`:
```bash
cp .env.example .env
```

The default configuration uses **Karachi** as the city. Edit `.env` to change:
```env
SECRET_KEY=your_generated_secret_key_here
FLASK_ENV=development
CITY_NAME=Karachi
```

### Step 4: Run the Application
```bash
python app.py
```

The application will start on: **http://127.0.0.1:5000**

## 📱 How to Use

### For First-Time Users:

1. **Open the website** in your browser: https://city-finder-k1d6.onrender.com/
   - Or locally: http://127.0.0.1:5000 (if running locally)
2. **Allow location** when browser asks (click "My Location" button if needed)
3. **Click any category button** (e.g., Restaurants)
4. **See results** with distances
5. **Click "Get Directions"** to see route

### Using Simple Mode:

1. Click the **text size icon** (left side)
2. Buttons and text become larger
3. Easier to read and use

## 📊 Sample Output

### Search Results Example:
```
Found 47 Restaurants (sorted by distance)

┌─────────────────────────────────────┐
│ 🔹 850 m away                       │
│ 📍 BBQ Tonight                      │
│ 📍 123 Main Street, Karachi         │
│ [👁️ View on Map] [🧭 Get Directions]│
└─────────────────────────────────────┘

┌─────────────────────────────────────┐
│ 🔹 1.2 km away                      │
│ 📍 Kolachi Restaurant               │
│ 📍 456 Beach Road, Karachi          │
│ [👁️ View on Map] [🧭 Get Directions]│
└─────────────────────────────────────┘
```

### Direction Output Example:
```
╔═══════════════════════════════════╗
║  🗺️ Route to BBQ Tonight         ║
║                                   ║
║  🛣️ 2.3 km        ⏱️ ~6 min      ║
║  Total Distance   Estimated Time  ║
║                                   ║
║  Turn-by-turn directions shown    ║
║  on the map with blue line        ║
╚═══════════════════════════════════╝
```

## 📁 Project Structure

```
CityFinder/
├── app.py                      # Main Flask application
├── config.py                   # Configuration management
├── requirements.txt            # Python dependencies
├── .env                        # Environment variables (not in git)
├── .env.example                # Example environment file
├── .gitignore                  # Git ignore rules
├── README.md                   # This file
├── services/
│   ├── geocoding.py           # City geocoding with caching
│   └── places_api.py          # Place search with fallback
└── templates/
    └── dashboard.html         # Main UI with all features
```

## 🎯 Features for Uneducated/Elderly Users

### Visual Aids
- ✅ Large, colorful category buttons with emoji icons
- ✅ Clear distance badges on every result
- ✅ Color-coded elements for easy recognition
- ✅ Icons everywhere for visual understanding

### Accessibility
- ✅ **Simple mode** - Larger text and buttons
- ✅ **Clear categories** - Picture icons for each type
- ✅ **Distance display** - Know what's nearest
- ✅ **One-click actions** - Minimal steps needed

### Safety & Reliability
- ✅ No complex forms or inputs
- ✅ Works even if APIs fail (demo data)
- ✅ Clear error messages in simple language
- ✅ Easy to understand interface

## 🔒 Privacy & Security

- Location data never stored or sent to servers
- Location only used in browser
- No user accounts or personal data collection
- No tracking or analytics
- Open source - you can verify everything

## 🌐 Browser Support

- ✅ Chrome (recommended for voice features)
- ✅ Firefox
- ✅ Microsoft Edge
- ✅ Safari
- ✅ Mobile browsers (iOS Safari, Android Chrome)

## 🛠️ Development

### Adding New Categories
Edit `services/places_api.py` and `templates/dashboard.html`:
```python
CATEGORY_TAGS = {
    "Your Category": "osm_amenity_tag"
}
```

### Changing the City
Edit `.env` file:
```env
CITY_NAME=Your City Name
```

### Testing API Calls
```bash
python test_nominatim.py
```

## ⚠️ Important Notes

### API Rate Limits
- Nominatim API: Please respect usage policy
- Include User-Agent in all requests (already implemented)
- Demo data fallback prevents service disruption

### Location Services
- Must allow location access for full functionality
- Works without location (no distance sorting)
- Browser will ask permission first

### Internet Connection
- Required for live data
- Demo data available offline
- Graceful handling of network failures

## 📝 Git Commit History

This project has **5+ meaningful commits**:
1. Initial setup with Flask and basic structure
2. Add OpenStreetMap API integration with error handling
3. Implement distance calculation and sorting
4. Add voice search and accessibility features
5. Complete UI improvements and documentation

View all commits: `git log --oneline`

## 🤝 Contributing

Contributions welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

MIT License - Free to use, modify, and distribute

## 👨‍💻 Author

Developed as a university project for Web Programming course
- Course: Web Programming
- Deadline: Thursday, 12 November 2026, 11:59 PM
- Requirements: Public GitHub repo, 5+ commits, API usage, README, .gitignore

## 🆘 Support

If you need help:
1. Click "Help" button in the app
2. Read this README carefully
3. Check the tutorial in the help section
4. Try voice instructions feature

## 🙏 Acknowledgments

- OpenStreetMap contributors for map data
- Leaflet.js team for mapping library
- Bootstrap team for UI framework
- OSRM for routing engine
- Font Awesome for icons

## 🌐 Links

- **Live Application:** https://city-finder-k1d6.onrender.com/
- **GitHub Repository:** https://github.com/YOUR_USERNAME/CityFinder
- **Deployed on:** Render.com (Free Tier)

---

## 🎓 Academic Project

This project was developed as part of a Web Programming course assignment.

**Course:** Web Programming  
**Deadline:** Thursday, 12 November 2026, 11:59 PM  
**Status:** ✅ Completed and Deployed

---

**Made with ❤️ to help everyone find places easily!**

For questions or issues, please open an issue on GitHub.
