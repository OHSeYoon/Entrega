from geopy.geocoders import Nominatim

def get_coordinates(address):
    geolocator = Nominatim(user_agent="geoapi")
    location = geolocator.geocode(address)
    if location:
        return location.latitude, location.longitude
    else:
        return "Address not found"

# Example usage
address = "Rua da Graça 201, São Paulo, Brazil"
coordinates = get_coordinates(address)
print(f"Coordinates for '{address}': {coordinates}")
