__author__ = 'skamer'
from sys import argv
meal = argv[1]
#while True:
#    meal = raw_input("Enter the meal amount before tax: ")
if meal.isdigit():
        meal = int(meal)
else:
    print "You need to supply an integer number for meal cost, try again"
    exit()

tax = 0.15
tip = 0.15
tax_value = meal * tax
meal_with_tax = meal + tax_value
tip_value = (meal + tax_value) * tip
total = meal_with_tax + tip_value

print "The tax on {} dollar meal with tax rate of {:.0%} is ${:.2f}".format(meal,tax,tax_value)
print 'The tip on {} dollar meal with tip rate of {:.0%} is ${:.2f}'.format(meal,tip,tip_value)
print 'The total price of a {} dollar meal with {:.0%} tax and {:.0%} tip is ' \
      '${:.2f}'.format(meal,tax,tip,total)