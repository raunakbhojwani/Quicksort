#Author: Raunak Bhojwani
#Created: November 2 2014
#Lab3: Quicksort
#Visualizing most populous cities

from cs1lib import *                                                # Relevant import functions


WINDOW_WIDTH = 720                                                  # Initialize constant variables
WINDOW_HEIGHT = 360
X_ORIGIN = WINDOW_WIDTH/2
Y_ORIGIN = WINDOW_HEIGHT/2
PIXELS_PER_DEGREE = WINDOW_HEIGHT/180.0

def city_name(city, x, y):                                          # Abstracting a function that draws the city's name
    enable_stroke()
    set_stroke_color(0, 0, 1)
    draw_text(city[0], x, y+1, centered=True)
    disable_stroke()
    
    
def visualize_cities():                                             # main function
    
    background_img = load_image("world.png")                        # load and draw the background image
    draw_image(background_img, 0, 0)
    

    visual_city_list = []                                           # Initialize an empty to list to append lists of cities' data
    in_file = open("cities_population.txt", "r")                     
    
    for line in in_file:                                        
        each_city = line.strip().split(",")                         # strip, split to create a list out of each line in the file
        visual_city_list.append(each_city)                          # each list is data about one city. append these lists into one bigger list  
    
    in_file.close()                                                 # close file
    
    enable_smoothing()
    set_fill_color(1, 0.5, 0)
    
    
    for city in visual_city_list[:51]:                              # for each city in the list until the 50th city, [:n]
        if not window_closed():
            x = X_ORIGIN + (float(city[3]) * PIXELS_PER_DEGREE)     # appropriate values of x and y considering the linear map
            y = Y_ORIGIN + (float(city[2]) * PIXELS_PER_DEGREE)
            disable_stroke()
            draw_circle(x, y, 3)                                    # draw circles as points for the cities
            city_name(city, x, y)                                   # function call
              
        
            request_redraw()
            sleep(1)
        
        
        
start_graphics(visualize_cities, "Visualize Cities!", WINDOW_WIDTH, WINDOW_HEIGHT, flipped_y = True) # START GRAPHICS