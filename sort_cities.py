#Author: Raunak Bhojwani
#Created: November 2 2014
#Lab3: Quicksort
#Sorting world_cities.txt by latitude, population and alphabet

from string import lower                                    # Import the relevant functions
from city import City
from quicksort import sort

def compare_name(a, b):                                     # Compare function for name
    return lower(a.name) <= lower(b.name)

def compare_population(a, b):                               # Compare function for population
    if a.population <= b.population:
        return False
    else:
        return True

def compare_latitude(a, b):                                 # Compare function for latitude
    return a.latitude <= b.latitude
                        
def main():

    city_list = []                                              #Initialize an empty list to append to
    in_file = open("world_cities.txt", "r")                     #Open the original file
    
    for line in in_file:                                        #For each line:
        t = line.strip()                                        #Strip the line of whitespace before and after it
        variable_list = t.split(",")                            #Split the variables that are separated by commas
        
        #Create the object in the city class
        city = City(variable_list[0], variable_list[1], variable_list[2], int(variable_list[3]), float(variable_list[4]), float(variable_list[5]))
        
        city_list.append(city)                                  #Append the reference into the empty list
    
    in_file.close()                                             #Close the file
    
    
    out_file_name = open("cities_alpha.txt", "w")               #Open output file for name
    sort(city_list, compare_name)
     
    for cities in city_list:
        out_file_name.write(str(cities) + "\n")                      #Write the string function for name
         
    out_file_name.close()                                            #Close the file
 
 
    out_file_population = open("cities_population.txt", "w")                #Open output file for population
    sort(city_list, compare_population)
     
    for cities in city_list:
        out_file_population.write(str(cities) + "\n")                      #Write the string function for population
         
    out_file_population.close()                                            #Close the file

    out_file_latitude = open("cities_latitude.txt", "w")                #Open output file for latitiude
    sort(city_list, compare_latitude)
     
    for cities in city_list:
        out_file_latitude.write(str(cities) + "\n")                      #Write the string function for latitude
         
    out_file_latitude.close()                                            #Close the file

main()                                                          #Run the function defined above
