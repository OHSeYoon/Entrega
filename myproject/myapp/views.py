from rest_framework.response import Response
from rest_framework.decorators import api_view
from geopy.geocoders import Nominatim
from .models import DistanceCalculation
import osmnx as ox
import networkx as nx

@api_view(['GET'])
def hello_world(request):
    return Response({'message': 'Hello, Flutter!!!'})

def get_coordinates(address):
    geolocator = Nominatim(user_agent="geoapi")
    location = geolocator.geocode(address)
    if location:
        return location.latitude, location.longitude
    else:
        return None

@api_view(['GET'])
def geocode_address(request):
    start_address = request.query_params.get('start_address')
    end_address = request.query_params.get('end_address')

    if not start_address or not end_address:
        return Response({'error': 'Both start and end addresses are required.'}, status=400)

    start_coords = get_coordinates(start_address)
    end_coords = get_coordinates(end_address)

    if not start_coords or not end_coords:
        return Response({'error': 'One or both addresses could not be located.'}, status=404)

    midpoint = ((start_coords[0] + end_coords[0]) / 2, (start_coords[1] + end_coords[1]) / 2)
    graph = ox.graph_from_point(midpoint, dist=2000, network_type='drive')

    start_node = ox.distance.nearest_nodes(graph, X=start_coords[1], Y=start_coords[0])
    end_node = ox.distance.nearest_nodes(graph, X=end_coords[1], Y=end_coords[0])

    shortest_path = nx.shortest_path_length(graph, start_node, end_node, weight="length")
    distance_km = shortest_path / 1000

    DistanceCalculation.objects.create(
        start_address=start_address,
        end_address=end_address,
        distance_km=round(distance_km, 2)
    )

    return Response({'distance_km': round(distance_km, 2)})
