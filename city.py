#Author: Raunak Bhojwani
#Created: November 2 2014
#Lab3: Quicksort
#Class definition for a city

class City:
    def __init__(self, country_code, name, region, population, latitude, longitude ):                       # Constructor
        self.country_code = country_code                                                                    # Intialize instance varibales
        self.name = name
        self.region = region
        self.population = population
        self.latitude = latitude
        self.longitude = longitude
        
    def __str__(self):
        return self.name + "," + str(self.population) + "," + str(self.latitude) + "," + str(self.longitude)    # String function for printing the object
        
        
    