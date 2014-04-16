__author__ = 'skamer'
from optparse import OptionParser
parser  = OptionParser()
parser.add_option("-m", "--meal",dest="meal", help="meal price")
parser.add_option("-t", "--tax",dest="tax", help="tax rate")
parser.add_option("-g", "--gratuity",dest="tip", help="gratuity (tip) rate", default=.18)
(options, args) = parser.parse_args()

meal = options.meal
tax = options.tax
tip = options.tip

#from sys import argv

#if len(argv) != 4:
#    print "This script requires 3 arguments, meal amount, tax rate, tip rate"
#    exit(1)

#meal = argv[1]
#tax = argv[2]
#tip = argv[3]

'''
if meal.isdigit():
        meal = int(meal)
else:
    print "You need to supply an integer number for meal cost, try again"
    exit()
'''

def exit_script(exitcode):
    if exitcode != 0:
        exit(exitcode)

## ensure that tip is a decimal less than 1
def eval_for_percentage_decimal(name,val,lessthanone):
    #print "my raw value for {} is {}".format(name,val)
    exitcode = 0
    try:
        float_val = float(val)
        #print "my floated value for {} is {}".format(name,float_val)
        if lessthanone == 'yes':
            if float_val >= 1:
                print "You need to supply a super decimal number less than 1 for {} rate, try again".format(name)
                exitcode = 1
    except:
        ## the arg provided is not float-able, i.e. it is not a number
        if lessthanone == 'yes':
            print "You need to supply a decimal number less than 1 for {} rate, try again".format(name)
        else:
            print "You need to supply a number  for {} price, try again".format(name)
        exit()
    exit_script(exitcode)
    return float_val

meal = eval_for_percentage_decimal('meal',meal,'no')
tax = eval_for_percentage_decimal('tax',tax,'yes')
tip = eval_for_percentage_decimal('tip',tip,'yes')

tax_value = meal * tax
meal_with_tax = meal + tax_value
tip_value = (meal + tax_value) * tip
total = meal_with_tax + tip_value

print "The tax on a ${} meal with tax rate of {:.0%} is ${:.2f}".format(meal,tax,tax_value)
print 'The tip on a ${} meal with tip rate of {:.0%} is ${:.2f}'.format(meal,tip,tip_value)
print 'The total price of a ${} meal with {:.0%} tax and {:.0%} tip is ' \
      '${:.2f}'.format(meal,tax,tip,total)