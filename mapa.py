import osmnx as ox
import networkx as nx
from geopy.geocoders import Nominatim

def get_coordinates(address):
    geolocator = Nominatim(user_agent="geoapi")
    location = geolocator.geocode(address)
    if location:
        print(f"Coordinates for '{address}': ({location.latitude}, {location.longitude})")
        return location.latitude, location.longitude
    else:
        print(f"Address '{address}' not found.")
        return None

def calculate_distance(start_address, end_address):
    # Get coordinates for each address
    start_coords = get_coordinates(start_address)
    end_coords = get_coordinates(end_address)
    
    if not start_coords or not end_coords:
        return "One or both addresses could not be located."
    
    # Midpoint for graph range
    midpoint = ((start_coords[0] + end_coords[0]) / 2, (start_coords[1] + end_coords[1]) / 2)
    graph = ox.graph_from_point(midpoint, dist=2000, network_type='drive')

    
    # Nearest nodes to start and end points
    start_node = ox.distance.nearest_nodes(graph, X=start_coords[1], Y=start_coords[0])
    end_node = ox.distance.nearest_nodes(graph, X=end_coords[1], Y=end_coords[0])
    
    # Shortest path distance
    shortest_path = nx.shortest_path_length(graph, start_node, end_node, weight="length")
    distance_km = shortest_path / 1000
    return f"The distance between the two addresses is approximately {distance_km:.2f} km."

# Example usage
start_address = "Rua da Graça 914, São Paulo, Brazil"
end_address = "Rua General Flores 114, São Paulo, Brazil"
print(calculate_distance(start_address, end_address))
