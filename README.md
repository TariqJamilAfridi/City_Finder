# CityFinder - Smart City Location Discovery Platform

CityFinder is a lightweight, city-based location discovery platform that allows users to find specific amenities and services within a configured city using OpenStreetMap data.

## Features

- 🗺️ **Interactive Map** - Powered by Leaflet.js for smooth navigation
- 🔍 **13+ Categories** - Restaurants, Hospitals, Banks, ATMs, Schools, Parks, and more
- 📍 **Real Location Data** - Uses OpenStreetMap/Nominatim APIs with demo data fallback
- 🎯 **No Authentication Required** - Direct access to city exploration
- 🌐 **Directions Integration** - Get directions to any location via OpenStreetMap

## Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### 1. Clone the repository
```bash
git clone <your-repo-url>
cd CityFinder
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables
Copy `.env.example` to `.env` and customize if needed:
```bash
cp .env.example .env
```

The default configuration uses **Karachi** as the city. You can change it in `.env`:
```env
CITY_NAME=Karachi
```

### 4. Run the Application
```bash
python app.py
```

The application will start on: **http://127.0.0.1:5000**

## Usage

1. Open your browser and navigate to `http://127.0.0.1:5000`
2. Click on any category button (Restaurants, Banks, etc.)
3. View results on the map and in the sidebar
4. Click on any location card to view it on the map
5. Use the "Directions" button to get navigation via OpenStreetMap

## Technologies Used

- **Backend:** Flask (Python)
- **Frontend:** Bootstrap 5, Leaflet.js
- **APIs:** OpenStreetMap Nominatim API
- **Icons:** Font Awesome

## Project Structure
```
CityFinder/
├── app.py                 # Main Flask application
├── config.py             # Configuration management
├── requirements.txt      # Python dependencies
├── .env                  # Environment variables (not in git)
├── .env.example          # Example environment file
├── services/
│   ├── geocoding.py      # City geocoding logic
│   └── places_api.py     # Place search with fallback data
└── templates/
    └── dashboard.html    # Main UI template
```

## Customization

### Change the City
Edit `.env` file:
```env
CITY_NAME=Your City Name
```

### Modify Categories
Edit `templates/dashboard.html` and `services/places_api.py` to add/remove categories.

## Notes

- The app uses public OpenStreetMap APIs which may have rate limits
- Demo data is included as fallback when APIs are unavailable
- No authentication or database required for basic functionality

## License
MIT License
