import requests

# First, test getting Karachi's area ID
print("Testing Nominatim API for Karachi...")
url = "https://nominatim.openstreetmap.org/search"
headers = {"User-Agent": "CityFinderApp/1.0 (University Assignment)"}
params = {
    "q": "Karachi",
    "format": "json",
    "limit": 1
}

response = requests.get(url, headers=headers, params=params, timeout=10)
print(f"Nominatim Response Status: {response.status_code}")
data = response.json()
print(f"Nominatim Data: {data[0] if data else 'No data'}")

if data:
    place = data[0]
    osm_id = int(place['osm_id'])
    osm_type = place['osm_type']
    
    if osm_type == 'relation':
        area_id = 3600000000 + osm_id
    elif osm_type == 'way':
        area_id = 2400000000 + osm_id
    else:
        area_id = None
    
    print(f"\nOSM Type: {osm_type}")
    print(f"OSM ID: {osm_id}")
    print(f"Area ID: {area_id}")
    
    # Now test Overpass API
    if area_id:
        print("\n" + "="*50)
        print("Testing Overpass API...")
        
        tag = '["amenity"="restaurant"]'
        overpass_query = f"""[out:json][timeout:25];
area({area_id})->.searchArea;
(
  node{tag}(area.searchArea);
  way{tag}(area.searchArea);
  relation{tag}(area.searchArea);
);
out center 10;"""
        
        print(f"\nQuery:\n{overpass_query}")
        
        overpass_url = "https://overpass-api.de/api/interpreter"
        
        # Try method 1: Direct data
        print("\n--- Method 1: Direct data ---")
        try:
            headers1 = {
                'Content-Type': 'application/x-www-form-urlencoded',
                'User-Agent': 'CityFinderApp/1.0'
            }
            resp1 = requests.post(overpass_url, data=overpass_query, headers=headers1, timeout=30)
            print(f"Status: {resp1.status_code}")
            print(f"Headers: {resp1.headers.get('Content-Type')}")
            if resp1.status_code == 200:
                result = resp1.json()
                print(f"Success! Found {len(result.get('elements', []))} elements")
            else:
                print(f"Error: {resp1.text[:200]}")
        except Exception as e:
            print(f"Exception: {e}")
        
        # Try method 2: data parameter
        print("\n--- Method 2: data parameter ---")
        try:
            headers2 = {'User-Agent': 'CityFinderApp/1.0'}
            resp2 = requests.post(overpass_url, data={'data': overpass_query}, headers=headers2, timeout=30)
            print(f"Status: {resp2.status_code}")
            print(f"Headers: {resp2.headers.get('Content-Type')}")
            if resp2.status_code == 200:
                result = resp2.json()
                print(f"Success! Found {len(result.get('elements', []))} elements")
            else:
                print(f"Error: {resp2.text[:200]}")
        except Exception as e:
            print(f"Exception: {e}")
        
        # Try method 3: GET request
        print("\n--- Method 3: GET request ---")
        try:
            headers3 = {'User-Agent': 'CityFinderApp/1.0'}
            resp3 = requests.get(overpass_url, params={'data': overpass_query}, headers=headers3, timeout=30)
            print(f"Status: {resp3.status_code}")
            print(f"Headers: {resp3.headers.get('Content-Type')}")
            if resp3.status_code == 200:
                result = resp3.json()
                print(f"Success! Found {len(result.get('elements', []))} elements")
            else:
                print(f"Error: {resp3.text[:200]}")
        except Exception as e:
            print(f"Exception: {e}")
