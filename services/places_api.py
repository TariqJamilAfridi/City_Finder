import requests
import time

# Demo data for when APIs are down
DEMO_DATA = {
    "Restaurants": [
        {"name": "BBQ Tonight", "lat": 24.8607, "lon": 67.0011},
        {"name": "Kolachi Restaurant", "lat": 24.8138, "lon": 66.9753},
        {"name": "Cafe Flo", "lat": 24.8700, "lon": 67.0661},
        {"name": "Burning Brownie", "lat": 24.8607, "lon": 67.0011},
        {"name": "The Patio", "lat": 24.8546, "lon": 67.0207},
    ],
    "Mosques": [
        {"name": "Masjid-e-Tooba", "lat": 24.8785, "lon": 67.0809},
        {"name": "Jama Masjid", "lat": 24.8650, "lon": 67.0092},
        {"name": "Masjid-e-Ibrahim", "lat": 24.8567, "lon": 67.0184},
    ],
    "Banks": [
        {"name": "Habib Bank Limited - Clifton", "lat": 24.8138, "lon": 66.9753},
        {"name": "United Bank Limited - Saddar", "lat": 24.8546, "lon": 67.0271},
        {"name": "MCB Bank - Gulshan", "lat": 24.9214, "lon": 67.0897},
    ],
    "Hospitals": [
        {"name": "Aga Khan University Hospital", "lat": 24.8897, "lon": 67.0752},
        {"name": "Liaquat National Hospital", "lat": 24.8690, "lon": 67.0712},
        {"name": "Jinnah Postgraduate Medical Centre", "lat": 24.8834, "lon": 67.0333},
    ],
    "ATMs": [
        {"name": "HBL ATM - Clifton", "lat": 24.8155, "lon": 66.9738},
        {"name": "MCB ATM - Saddar", "lat": 24.8546, "lon": 67.0295},
        {"name": "UBL ATM - Gulshan", "lat": 24.9192, "lon": 67.0921},
    ],
    "Petrol stations": [
        {"name": "PSO Petrol Pump - Clifton", "lat": 24.8233, "lon": 66.9799},
        {"name": "Shell Petrol Station - Shahrah-e-Faisal", "lat": 24.8765, "lon": 67.0647},
        {"name": "Total Parco - Gulshan", "lat": 24.9198, "lon": 67.0914},
    ],
    "Pharmacies": [
        {"name": "Agha's Supermarket Pharmacy", "lat": 24.8670, "lon": 67.0663},
        {"name": "Fazal Din Pharmacy", "lat": 24.8592, "lon": 67.0296},
        {"name": "Sehat Pharmacy", "lat": 24.9147, "lon": 67.0886},
    ],
    "Hotels": [
        {"name": "Pearl Continental Hotel", "lat": 24.8631, "lon": 67.0292},
        {"name": "Avari Towers Karachi", "lat": 24.8601, "lon": 67.0280},
        {"name": "Marriott Hotel Karachi", "lat": 24.8723, "lon": 67.0591},
    ],
    "Shopping malls": [
        {"name": "Dolmen Mall Clifton", "lat": 24.8081, "lon": 66.9751},
        {"name": "Lucky One Mall", "lat": 24.9018, "lon": 67.0713},
        {"name": "Ocean Mall", "lat": 24.8250, "lon": 67.0290},
    ],
    "Schools": [
        {"name": "Karachi Grammar School", "lat": 24.8690, "lon": 67.0402},
        {"name": "St. Patrick's High School", "lat": 24.8557, "lon": 67.0294},
        {"name": "Beaconhouse School System", "lat": 24.8732, "lon": 67.0620},
    ],
    "Universities": [
        {"name": "University of Karachi", "lat": 24.9447, "lon": 67.1235},
        {"name": "NED University", "lat": 24.9211, "lon": 67.1138},
        {"name": "Institute of Business Administration (IBA)", "lat": 24.8872, "lon": 67.0651},
    ],
    "Parks": [
        {"name": "Bagh Ibn Qasim", "lat": 24.8201, "lon": 66.9905},
        {"name": "Hill Park", "lat": 24.8601, "lon": 67.0337},
        {"name": "Jehangir Park", "lat": 24.8542, "lon": 67.0221},
    ],
    "Bus stations": [
        {"name": "Saddar Bus Station", "lat": 24.8587, "lon": 67.0258},
        {"name": "Tower Bus Stop", "lat": 24.8490, "lon": 67.0314},
        {"name": "Gurumandir Bus Station", "lat": 24.8621, "lon": 67.0071},
    ],
}

# Mapping categories to Nominatim search amenities
CATEGORY_TAGS = {
    "Restaurants": "restaurant",
    "Mosques": "place_of_worship",
    "Banks": "bank",
    "Hospitals": "hospital",
    "ATMs": "atm",
    "Petrol stations": "fuel",
    "Pharmacies": "pharmacy",
    "Hotels": "hotel",
    "Shopping malls": "mall",
    "Schools": "school",
    "Universities": "university",
    "Parks": "park",
    "Bus stations": "bus_station"
}

def get_demo_data(category):
    """Return demo/sample data when APIs are unavailable"""
    if category in DEMO_DATA:
        results = []
        for idx, place in enumerate(DEMO_DATA[category]):
            results.append({
                "id": idx + 1,
                "name": place["name"],
                "category": category,
                "lat": place["lat"],
                "lon": place["lon"],
                "address": f"{place['name']}, Karachi, Pakistan"
            })
        return results
    return []

def search_places_nominatim(city_name, category):
    """Search using Nominatim API"""
    if category not in CATEGORY_TAGS:
        return {"error": "Invalid category"}, 400
    
    amenity = CATEGORY_TAGS[category]
    
    url = "https://nominatim.openstreetmap.org/search"
    headers = {"User-Agent": "CityFinderApp/1.0 (University Assignment)"}
    
    params = {
        "q": f"{amenity} in {city_name}",
        "format": "json",
        "limit": 50,
        "addressdetails": 1
    }
    
    try:
        response = requests.get(url, headers=headers, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        results = []
        seen_names = set()
        
        for place in data:
            name = place.get('display_name', '').split(',')[0]
            
            if not name or name in seen_names or len(name) < 3:
                continue
            
            seen_names.add(name)
            
            address = place.get('display_name', 'Address not available')
            lat = float(place.get('lat', 0))
            lon = float(place.get('lon', 0))
            
            results.append({
                "id": place.get('place_id', 0),
                "name": name,
                "category": category,
                "lat": lat,
                "lon": lon,
                "address": address
            })
        
        return results
        
    except (requests.RequestException, requests.Timeout) as e:
        print(f"Nominatim API error: {e}")
        return None  # Signal to use fallback

def search_places(area_id, category):
    """
    Primary search function with fallback to demo data
    """
    from config import Config
    city_name = Config.CITY_NAME
    
    print(f"Searching for {category} in {city_name}...")
    
    # Try Nominatim API first
    results = search_places_nominatim(city_name, category)
    
    # If API failed, use demo data
    if results is None or (isinstance(results, tuple) and results[1] >= 400):
        print(f"API unavailable, using demo data for {category}")
        demo_results = get_demo_data(category)
        if demo_results:
            return demo_results
        else:
            return {"error": f"Service temporarily unavailable. Please try again later."}, 503
    
    if len(results) > 0:
        print(f"Found {len(results)} places using Nominatim")
        return results
    else:
        # No results from API, try demo data
        print(f"No API results, using demo data for {category}")
        demo_results = get_demo_data(category)
        if demo_results:
            return demo_results
        return {"error": f"No {category} found in {city_name}"}, 404