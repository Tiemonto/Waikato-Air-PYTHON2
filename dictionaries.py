#Imports random module

import random

# Sets the multiplier for the discount (6% - 30%)

discount = round(random.uniform(0.05, 0.31), 2)

# Dictionary of available Destinations & Prices

destinations = {
"1": {"Wellington": 35},
"2": {"Gisborne": 26},
"3": {"Blenheim": 37},
"4": {"Christchurch": 41},
"5": {"Dunedin": 48}
}

# Dictionary of available flight times and discount worthiness

flights = {
1: {"17/11/2021: 9:30pm": discount},
2: {"17/11/2021: 1:45pm": discount},
3: {"18/11/2021: 2:00pm": 0},
4: {"19/11/2021: 9:30pm": 0},
5: {"19/11/2021: 9:30pm": 0},
6: {"20/11/2021: 11:45pm": 0}
}


