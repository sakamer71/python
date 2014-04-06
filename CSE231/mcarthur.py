__author__ = 'skamer'
from calendar import month_name

## this is a program to guess someone's age and month they were born.
prompt=' > '



def verify_number_range(mytype,mynumber,myrange):
    while not mynumber.isdigit() or not 1 <= int(mynumber) <= myrange:
        print "you need to enter a digit value for %s between 1 and %d" %(mytype,myrange)
        mynumber=raw_input(prompt)
    return mynumber

def guess_month_and_age(number):
    ## based on prev logic, number will only either be a 3 or 4 digit number
    number=str(number)
    if len(number) == 4:
        Month = number[0:2]
        Age = number[2:4]
    else:
        Month = number[0:1]
        Age = number[1:3]
    return int(Month),int(Age)

print "Write the month you were born",
mymonth=raw_input(prompt)
mymonth=verify_number_range('month',mymonth,12)

doublemonth=int(mymonth) * 2
print "Now double that number, and you get %d" %doublemonth

addfive = doublemonth + 5
print "Next, add five to that total and you get %d" %addfive

timesfifty = addfive * 50
print "Ok, now take that number and multiply by 50 - that gives you %d" %timesfifty

print "Moving on, write down your age"
myage=raw_input(prompt)
myage=verify_number_range('age',myage,99)

age_plus_timesfifty=int(myage) + timesfifty
print "Almost Done.  Now add your age to previous number %d and you get %d" %(timesfifty, age_plus_timesfifty)

minus365 = age_plus_timesfifty - 365
print "Finally, subtract 365 from that number and you get %d" %minus365

plus115 = minus365 + 115
#print plus115

values = guess_month_and_age(plus115)
monthname = month_name[values[0]]
print "OK, my turn.  Using my magic powers, i can deduce from your number that... "
print "You were born in %s and your age is %d" %(monthname,values[1])