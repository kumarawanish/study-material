import math

def haversine_distance(lat1, lon1, lat2, lon2):
    R = 6371.0  # Earth's mean radius in kilometers

    # Convert latitude and longitude from degrees to radians
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)

    # Compute differences
    delta_lat = lat2_rad - lat1_rad
    delta_lon = lon2_rad - lon1_rad

    # Haversine formula
    a = math.sin(delta_lat / 2) ** 2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(delta_lon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = R * c

    return distance

# Example usage:
lat1 = 52.5200  # Latitude of point 1 (e.g., city 1)
lon1 = 13.4050  # Longitude of point 1
lat2 = 48.8566  # Latitude of point 2 (e.g., city 2)
lon2 = 2.3522   # Longitude of point 2

distance = haversine_distance(lat1, lon1, lat2, lon2)
print(f"Aerial distance between the points is {distance:.2f} kilometers.")