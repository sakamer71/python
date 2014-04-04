__author__ = 'skamer'
from time import sleep

def reverse_num(number):
    revnum = number[2] + number[1] + number[0]
    return revnum

def big_minus_small(num1,num2):
    if num1 > num2:
        big=num1
        small=num2
    else:
        big=num2
        small=num1
    difference = big - small
    return big,small,difference


prompt = " > "
print "What is your name",
name = raw_input(prompt)

print """
%s, I'm about to show you a number game that will blow your mind.
You give me a number and run a few calculations, and then
I guarantee that your new number will be 1089
""" %name

print "%s, pick any 3 digit number\nBe sure that the \
1st and 3rd digits are at least 2 numbers apart" %name,

mynumber=raw_input(prompt)

## check for a 3 digit number
while (len(mynumber) != 3) or not mynumber.isdigit():
    print "you need to select a 3 digit number!"
    print "Try again",
    mynumber=raw_input(prompt)

## check that 1st and 3rd digits are 2 or more numbers apart
while abs(int(mynumber[0]) - int(mynumber[2])) < 2:
    print "You need to select a number whose 1st and 3rd digits are 2 or more numbers apart!"
    print "Try again",
    mynumber=raw_input(prompt)

mydigit=int(mynumber)

print "If i ask you to reverse your number %s, you will get" %mynumber,
reverse1 = int(reverse_num(mynumber))
print reverse1

print "Now, subtract the bigger number from the smaller number..."
mytuple = big_minus_small(mydigit,reverse1)
print "%d minus %d equals %d" %(mytuple[0],mytuple[1],mytuple[2])
newnum=mytuple[2]

print "Now, reverse the new number %d " %newnum,
reverse2 = int(reverse_num(str(newnum)))
print "and you get %s" %reverse2

print "Finally, Add these two numbers together and what do you get..."
sleep(1)
print "Wait for it..."
sleep(1)
print "Wait for it..."
sleep(1)
print "Wait for it..."
sleep(1)
print "%d + %d = %d" %(newnum,reverse2,newnum+reverse2)