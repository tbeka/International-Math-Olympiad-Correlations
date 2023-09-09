#Importing Geospatial Python packages.
from geopy.geocoders import Nominatim
from geopy import distance
geolocator = Nominatim(user_agent="MyApp")

#Function to get the location of a country from its name
def loc(country):
    location = geolocator.geocode(country)
    return (location.latitude, location.longitude)

#Function to get a distance between two countries
def dist(country1, country2):
    loc1 = loc(country1)
    loc2 = loc(country2)
    return(distance.distance(loc1, loc2).kilometers)
