#Author: Raunak Bhojwani
#Created: November 2 2014
#Lab3: Quicksort
#Manipulating the sort_cities file

# Import the relevant files and classes
from city import City

def main():
    
    city_list = []                                              #Initialize an empty list to append to
    in_file = open("sort_cities.txt", "r")                     #Open the original file
    
    for line in in_file:                                        #For each line:
        t = line.strip()                                        #Strip the line of whitespace before and after it
        variable_list = t.split(",")                            #Split the variables that are separated by commas
        #Create the object in the city class
        city = City(variable_list[0], variable_list[1], variable_list[2], int(variable_list[3]), float(variable_list[4]), float(variable_list[5]))
        city_list.append(city)                                  #Append the reference into the empty list
    
    in_file.close()                                             #Close the file
    
    out_file = open("cities_out.txt", "w")                      #Open output file
    for cities in city_list:                                    #For each object:
        out_file.write(str(cities) + "\n")                      #Write the sting function
        
    out_file.close()                                            #Close the file
    
    
        
main()                                                          #Run the function defined above
        
        
