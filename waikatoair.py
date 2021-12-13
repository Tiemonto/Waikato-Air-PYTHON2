# Import required files
from dictionaries import *
from functions import *
# Sets the random number of available flights (between 2 - 6)
num_flights = (random.randrange(2, 7))

# Running Introduction Program 
fname, lname = intro()

# Space out sections of program
linebreak()

# Running Location Function
destination, price, discounted_price = locations(fname, lname, destinations, discount)

# Running date/time function
time_choice, booking = date_time(destination, num_flights, flights, discount, price, discounted_price)

#Running final confirmation function
decision = confirmation(time_choice, fname, lname, destination, flights, discount, price, discounted_price, booking)

