import re

# Linebreak Function (for clarity and aesthetics)
def linebreak(): 
    print   ('''================================================================================
''')

# Intro Function (establishes names)
def intro():
    print("\nWelcome, and thank you for flying with Waikato Air today.")
    print("\n(Only 3-28 characters are allowed.)")
    fname = input("\nPlease input your First Name: ")
    while not re.match("[A-z]*$", fname):
        fname = input("Error! Please re-type your name. ")
        if re.match("[A-z]*$", fname):
            if len(fname) > 2 or len(fname) < 29:
                pass
    while len(fname) < 3 or len(fname) > 28:
        fname = input("Error! Please re-type your name. ")
        if len(fname) > 2 or len(fname) < 29:
            if re.match("[A-z]*$", fname):
                pass
    else: 
        pass
    lname = input("\nPlease input your Surname: ")
    while not re.match("[A-z]*$", lname):
        lname = input("error! Please re-type your name. ")
        if re.match("[A-z]*$", lname):
            if len(fname) > 2 or len(fname) < 29:
                pass
    while len(lname) < 3 or len(lname) > 28:
        lname = input("Error! Please re-type your name. ")
        if len(lname) > 2 or len(lname) < 29:
            if re.match("[A-z]*$", fname):
                pass
    else:
        pass
    return fname.capitalize(), lname.capitalize()

# Location choosing Function (and also establishes the price after discount)
def locations(fname, lname, destinations, discount):
    print("\n{} {}, please choose a destination from the avaliable list (Using numbers):\n".format(fname, lname))
    linebreak()
    for x in destinations.keys():
        for y in destinations[x].keys():
            print('{}: ({}): ${}'.format(x, y, destinations[x][y]))
    linebreak()
    choice = input("(Choose Here): ")
    if choice in destinations.keys():
        for y in destinations[choice].keys():
            print("\nIs {} your chosen destination? Type 'Yes' or 'No'\n".format(y))
            decision = input("(Choose Here): ")
            price = destinations[choice][y]
            if decision == 'no':
                print("\nPlease re-choose your destination:")
                linebreak()
                y = locations(fname, lname, destinations, discount)
                return y
                break
            elif decision == 'yes':
                pass
                discounted_price = round(price - (price * discount), 3)
                destination = y
            return destination, price, discounted_price

# Date/Time choosing Function (and displays the discounted price to the user)
def date_time(destination, num_flights, flights, discount, price, discounted_price):
    linebreak()
    visible_discount = str(discount * 100)
    print("Current Date/Time: (16/11/2021: 2:00pm)\n\nThere are currently {} bookable flights for {} at [${}]. We are offering a discounted price of [${}] for any bookings tomorrow (17th):".format(num_flights, destination, price, discounted_price))
    for x in flights.keys():
        if num_flights >= x:
            for y in flights[x].keys():                
                if flights[x][y] is discount: 
                    print("{}: ({}): ({}% Discount)".format(x, y, (visible_discount).rstrip('1, 2, 3, 4, 5, 6, 7, 8, 9,').rstrip('0').rstrip('.')))
                elif print("{}: ({})".format(x, y)):
                    pass
    print("\nPlease choose a Date/Time you'd like to fly (Using numbers):")
    linebreak()
    time_choice = int(input("\n(Choose Here): "))
    if time_choice in flights.keys():
        if time_choice <= num_flights:
            for y in flights[time_choice].keys():
                print("\nIs ({}) your chosen time? Type 'Yes or 'No'".format(y))
                pass
        decision = input("\n(Choose Here): ")
        linebreak()
        if decision == 'no':
            print("\nPlease re-choose your Date/Time:")
            y = date_time(y, num_flights, flights, discount, price, discounted_price)
            return y
        elif decision == 'yes':
            pass
        booking = y
        return time_choice, booking

def confirmation(time_choice, fname, lname, destination, flights, discount, price, discounted_price, booking):
    for x in flights.keys():
        if x is time_choice:
            for y in flights[time_choice].keys():
                if flights[time_choice][y] is discount:
                    print("{} {},\nYou've booked a flight to {} for [${}]. Departure time is ({})\nIs this information correct? Please type 'Yes' to confirm, or 'No' to cancel. If you cancel, you are able to re-enter your information.".format(fname, lname, destination, discounted_price, booking))
                    pass
                elif print("{} {},\nYou've booked a flight to {} for [${}]. Departure time is ({})\nIs this information correct? Please type 'Yes' to confirm, or 'No' to cancel. If you cancel, you are able to re-enter your information.".format(fname, lname, destination, price, booking)):
                    pass
                decision = input('\n(Choose Here): ')
                linebreak()
                if decision == 'no': 
                    print("\nAlright, you're now able to re-enter your booking information. Just re initiate the booking program.")
                    linebreak()
                elif decision == 'yes':
                    print("Your information has been registered. Thank you for flying with Waikato Air.")
                    linebreak()