# Create a class to hold a city location. Call the class "City". It should have
# fields for name, latitude, and longitude.
class City:
  def __init__(self, name, latitude, longitude):
    self.name = name
    self.lat = latitude
    self.lon = longitude
  
  def __str__(self):
    return f'{self.name}: ({self.lat}, {self.lon})'

# We have a collection of US cities with population over 750,000 stored in the
# file "cities.csv". (CSV stands for "comma-separated values".)
#
# In the body of the `cityreader` function, use Python's built-in "csv" module 
# to read this file so that each record is imported into a City instance. Then
# return the list with all the City instances from the function.
# Google "python 3 csv" for references and use your Google-fu for other examples.
#
# Store the instances in the "cities" list, below.
#
# Note that the first line of the CSV is header that describes the fields--this
# should not be loaded into a City object.
import csv

cities = []

def cityreader(cities = []):
  with open('cities.csv', newline='') as csvfile:
    read = list(csv.reader(csvfile, delimiter=','))
    for row in read[1:]:
      city, state, county, lat, lon = row[:5]
      cities.append(City(city, float(lat), float(lon)))
    
  return cities

cityreader(cities)

# Print the list of cities (name, lat, lon), 1 record per line.
for c in cities:
  print(c)

# STRETCH GOAL!
#
# Allow the user to input two points, each specified by latitude and longitude.
# These points form the corners of a lat/lon square. Pass these latitude and 
# longitude values as parameters to the `cityreader_stretch` function, along
# with the `cities` list that holds all the City instances from the `cityreader`
# function. This function should output all the cities that fall within the 
# coordinate square.
#
# Be aware that the user could specify either a lower-left/upper-right pair of
# coordinates, or an upper-left/lower-right pair of coordinates. Hint: normalize
# the input data so that it's always one or the other, then search for cities.
# In the example below, inputting 32, -120 first and then 45, -100 should not
# change the results of what the `cityreader_stretch` function returns.
#
# Example I/O:
#
# Enter lat1,lon1: 45,-100
# Enter lat2,lon2: 32,-120
# Albuquerque: (35.1055,-106.6476)
# Riverside: (33.9382,-117.3949)
# San Diego: (32.8312,-117.1225)
# Los Angeles: (34.114,-118.4068)
# Las Vegas: (36.2288,-115.2603)
# Denver: (39.7621,-104.8759)
# Phoenix: (33.5722,-112.0891)
# Tucson: (32.1558,-110.8777)
# Salt Lake City: (40.7774,-111.9301)

def getlatlon():
  latlon = input('Enter a comma separated latitude, longitude pair, or a non-number to quit: ')
  return map(float, latlon.split(','))


def inrange(num, least, most):
  return num >= least and num <= most


def cityreader_stretch(lat1, lon1, lat2, lon2, cities = []):
  if lat1 > lat2:
    lat2, lat1 = lat1, lat2
  if lon1 > lon2:
    lon2, lon1 = lon1, lon2
  
  within = []

  for city in cities:
    if inrange(city.lat, lat1, lat2) \
        and inrange(city.lon, lon1, lon2):
      within.append(city)

  return within


while True:
  try:
    lat1, lon1 = getlatlon()
    lat2, lon2 = getlatlon()
  except:
    print("Your entries couldn't be parsed as decimal numbers.")
    break

  within = cityreader_stretch(lat1, lon1, lat2, lon2, cities)
  for city in within:
    print(city)
