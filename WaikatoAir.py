# Import required files
from dictionaries import *
from functions import *
import random

# Running Introduction Program 
fname, lname = intro()

# Space out sections of program
linebreak()

# Running Location Function
y = locations(fname, lname, destinations)

date_time(y, num_flights)


