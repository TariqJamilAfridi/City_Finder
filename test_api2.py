import requests
import time

# Test with the alternative servers
servers = [
    "https://overpass-api.de/api/interpreter",
    "https://overpass.kumi.systems/api/interpreter",
    "https://overpass.openstreetmap.ru/api/interpreter"
]

area_id = 3606080948  # Karachi
tag = '["amenity"="restaurant"]'

overpass_query = f"""[out:json][timeout:25];
area({area_id})->.searchArea;
(
  node{tag}(area.searchArea);
  way{tag}(area.searchArea);
);
out center 100;"""

print("Testing different Overpass API servers...")
print(f"Query: {overpass_query[:100]}...\n")

for server in servers:
    print(f"Trying {server}...")
    try:
        headers = {'User-Agent': 'CityFinderApp/1.0'}
        response = requests.get(server, params={'data': overpass_query}, headers=headers, timeout=30)
        print(f"  Status: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            elements = data.get('elements', [])
            print(f"  ✓ SUCCESS! Found {len(elements)} elements")
            
            # Show first 3 results
            for i, elem in enumerate(elements[:3]):
                name = elem.get('tags', {}).get('name', 'No name')
                print(f"    {i+1}. {name}")
            break
        else:
            print(f"  ✗ Error: {response.text[:100]}")
    except Exception as e:
        print(f"  ✗ Exception: {str(e)[:100]}")
    
    print()
