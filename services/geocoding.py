import requests
import functools

@functools.lru_cache(maxsize=1)
def get_city_area_id(city_name):
    url = "https://nominatim.openstreetmap.org/search"
    headers = {"User-Agent": "CityFinderApp/1.0 (University Assignment)"}
    params = {
        "q": city_name,
        "format": "json",
        "limit": 1
    }
    
    try:
        response = requests.get(url, headers=headers, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        if not data:
            return None
            
        place = data[0]
        osm_id = int(place['osm_id'])
        osm_type = place['osm_type']
        
        if osm_type == 'relation':
            return 3600000000 + osm_id
        elif osm_type == 'way':
            return 2400000000 + osm_id
        else:
            return None
    except requests.RequestException as e:
        print(f"Nominatim API Error: {e}")
        return None