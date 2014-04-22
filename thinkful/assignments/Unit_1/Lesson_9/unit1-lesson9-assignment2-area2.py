__author__ = 'skamer'

def hello():
    print 'Hello!'


def print_welcome(name):
    print 'Welcome,', name

def print_options():
    print "Options:"
    print " 'p' print options"
    print " 's' calculate the area of a square"
    print " 'r' calculate the area of a rectangle"
    print " 'c' calculate the area of a circle"
    print " 'q' quit the program"

def area_square(length):
    '''Calculates the area of a square, based on length of one side
    '''
    return int(length) ** 2

def area_rectangle(length,width):
    '''Calculates the area of a rectangle, based on length and width
    '''
    return int(length) * int(width)

def area_circle(radius):
    '''Calculates area of a circle based on the radius
    '''
    return (int(radius) ** 2) * 3.14

def validate(length):
    valid = 'no'
    while valid == 'no':
        if not length.isdigit():
            length = raw_input('Must be a positive integer, try again: ')
        elif int(length) < 1:
            length = raw_input('Must be a positive integer, try again: ')
        else: valid = 'yes'
    return length




name = raw_input('Your Name: ')
hello(),
print_welcome(name)
print "This script will calculate the area of a square, rectangle, or circle."

choice = 'p'
while choice != 'q':
    if choice == 's':
        length = raw_input("Enter length of 1 side of the square: ")
        length = validate(length)
        area = area_square(length)
        print "Area of a square with side {} is {}".format(length,area)
    elif choice == 'r':
        length = raw_input("Enter the length of the rectangle: ")
        length = validate(length)
        width = raw_input("Enter the width of the rectangle: ")
        width = validate(width)
        area = area_rectangle(length,width)
        print "Area of a rectangle with sides {} and {} is {}".format(length,width,area)
    elif choice == 'c':
        radius = raw_input("Enter the radius of the circle: ")
        radius = validate(radius)
        area = area_circle(radius)
        print "Area of a circle with radius {} is {}".format(radius,area)
    elif choice == 'p':
        pass
    print_options()
    choice = raw_input("Enter your Choice:")