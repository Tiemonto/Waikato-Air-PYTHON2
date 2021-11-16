# Linebreak Function
def linebreak(): 
    print   ('''============================================================================================
''')

# Intro Function
def intro():
    print("\nWelcome, and thank you for flying with Waikato Air today.")
    fname = input("\nPlease input your First Name: ")
    lname = input("\nPlease input your Surname: ")
    return fname, lname

# Location choosing Function
def locations(fname, lname, destinations):
    print(("\n{} {}, please choose a destination from the avaliable list (using numbers):\n").format(fname, lname))
    linebreak()
    for x in destinations.keys():
        for y in destinations[x].keys():
            print('{}: {} {}'.format(x, y, destinations[x][y]))
    linebreak()
    choice = input("(Choose Here): ")
    if choice in destinations.keys():
        for y in destinations[choice].keys():
            print("\nIs {} your chosen destination? Type 'Yes' or 'No'\n".format(y))
            decision = input("(Choose Here): ")
            if decision == 'no':
                print("\nPlease re-choose your destination:")
                linebreak()
                y = locations(fname, lname, destinations)
            elif decision == 'yes':
                pass
            return y

def flights()
    num_flights = ()

# Date Function
def date_time(y, num_flights):
    print("\nThere are currently {} bookable flights for {}:".format(num_flights, y))


                
                
                
            
