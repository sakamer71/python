__author__ = 'skamer'

from time import sleep

#import os
wrong_guess_count = 0
turncount = 1

def choose_turn(turncount,player1,player2):
    ## alternate turns between player 1 and player 2
    turncount += 1
    if turncount%2 == 0:
        mysetter = player1
        myguesser = player2
    else:
        mysetter = player2
        myguesser = player1
    return mysetter,myguesser


print "Welcome to Hangman!\n"
player1 = raw_input("Player 1, what is your name?")
player2 = raw_input("Player 2, what is your name?")

whose_turn = choose_turn(turncount,player1,player2)
setter = whose_turn[0]
guesser = whose_turn[1]


prompt = " > "
print "%s, choose A phrase and we will try to guess it" %setter
phrase = raw_input(prompt)
print "OK Got it - setting up hangman for the phrase \"%s\"" %(phrase)
## not using system clear function b/c i am running this from within IDE
sleep(3)
print "\n"*4
#phrase=list(phrase)


def build_initial_phrase(phrase):
    global myphrase
    myphrase=[]
    for i in phrase:
        if i in [' ',':',',','\'','!','?','.']:
            myphrase.append(i)
            #print i,
        else:
            myphrase.append('_')
        #return myphrase
        #for i in myphrase:
            #print i,

build_initial_phrase(phrase)
for i in myphrase:
    print i,

all_guesses=[]
wrong_guesses=[]
print ''
print "Guess a letter",
guessletter=raw_input(prompt)
lettercount=phrase.count(guessletter)
if lettercount == 0:
    wrong_guess_count += 1
    print "Nope.  %d chances remaining" %(7-wrong_guess_count)
    wrong_guesses.append(guessletter)

print "The letter %s appears %d times" %(guessletter,lettercount)