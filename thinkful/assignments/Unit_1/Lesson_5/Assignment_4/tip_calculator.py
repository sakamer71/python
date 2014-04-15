__author__ = 'skamer'
#meal = 20
while True:
    meal = raw_input("What is the cost of your meal before tax? ")
    if meal.isdigit():
        meal=int(meal)
        break
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