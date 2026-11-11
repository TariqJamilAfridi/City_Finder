import requests

url = "https://nominatim.openstreetmap.org/search"
headers = {"User-Agent": "CityFinderApp/1.0"}
params = {
    "q": "restaurant in Karachi",
    "format": "json",
    "limit": 10,
    "addressdetails": 1
}

print("Testing Nominatim for restaurants in Karachi...")
response = requests.get(url, headers=headers, params=params, timeout=15)
print(f"Status: {response.status_code}")

if response.status_code == 200:
    data = response.json()
    print(f"Found: {len(data)} results\n")
    
    for i, place in enumerate(data[:5], 1):
        name = place.get('display_name', '').split(',')[0]
        lat = place.get('lat')
        lon = place.get('lon')
        print(f"{i}. {name}")
        print(f"   Location: {lat}, {lon}")
        print(f"   Address: {place.get('display_name')}\n")
else:
    print(f"Error: {response.text}")
