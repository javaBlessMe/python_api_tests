import requests
params = {"q":"Moscow, Russia", "format":"geojson"}
response = requests.get("https://nominatim.openstreetmap.org/search",
                        headers={"User-Agent":"PostmanRuntime/7.37.3", "Accept":"*/*"},
                        params=params).json()
print(response)