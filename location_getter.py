import geocoder

def get_location(name):
    g = geocoder.arcgis(name)
    return g.lat, g.lng
