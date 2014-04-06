__author__ = 'skamer'

from time import sleep


wrong_guess_count = 0
turncount = 1
playagain='y'

def choose_turn(turncount,player1,player2):
    ## alternate turns between player 1 and player 2
    turncount += 1
    if turncount%2 == 0:
        mysetter = player1
        myguesser = player2
    else:
        mysetter = player2
        myguesser = player1
    return mysetter,myguesser,turncount

print "Welcome to Hangman!\n"
player1 = raw_input("Player 1, what is your name?")
player2 = raw_input("Player 2, what is your name?")

while playagain=='y':
    whose_turn = choose_turn(turncount,player1,player2)
    setter = whose_turn[0]
    guesser = whose_turn[1]
    turncount = whose_turn[2]


    prompt = " > "
    print "%s, choose a phrase and %s will try to guess it" %(setter, guesser)
    phrase = raw_input(prompt)
    print "OK Got it - setting up hangman for the phrase \"%s\"" %(phrase)
    ## not using system clear function b/c i am running this from within IDE
    sleep(3)
    print "\n"*80
    phrase=list(phrase)

    def play_again():
        playagain = raw_input('Wanna play again? (y/n) >')
        if playagain=='y' or playagain=='Y':
            print "Great, let's switch..."
            playagain='y'
        else:
            playagain='n'
        return playagain

    def guessed_phrase(phrase):
        myphrase=[]
        for i in phrase:
            if i in [' ',':',',','\'','!','?','.']:
                myphrase.append(i)
            else:
                myphrase.append('_')
        return myphrase

    def update_display(phrase,myphrase,guessletter):
        for index,letter in enumerate(phrase):
            if letter == str.upper(guessletter):
                myphrase[index] = letter
            if letter == str.lower(guessletter):
                myphrase[index] = letter
        return myphrase


    myphrase=guessed_phrase(phrase)
    for i in myphrase:
        print i,

    all_guesses=[]
    wrong_guesses=[]
    print ''

    while '_' in myphrase:
        if wrong_guess_count > 6:
            exitphrase=''.join(phrase)
            print "\n\nSorry - you lose..."
            sleep(1)
            print "the answer was \"%s\"" %exitphrase
            sleep(1)
            playagain=play_again()
            if playagain == 'n':
                break

        print "\n%s, Guess a letter" %guesser,
        guessletter=raw_input(prompt)
        if (str.upper(guessletter) in all_guesses) or (str.lower(guessletter) in all_guesses):
            print "you already guessed %s" %guessletter
            continue
        if (str.upper(guessletter) not in phrase) and (str.lower(guessletter) not in phrase):
            wrong_guess_count += 1
            print "Nope.  %d chances remaining" %(7-wrong_guess_count)
            wrong_guesses.append(guessletter)
            all_guesses.append(guessletter)
            ## delete below, debugging
            print "Incorrect Guesses: "
            for i in wrong_guesses:
                print i,
            print "\n"
    #    print "The letter %s appears %d times" %(guessletter,lettercount)
        myphrase = update_display(phrase,myphrase,guessletter)
        all_guesses.append(guessletter)

        for i in myphrase:
            print i,
        if '_' not in myphrase:
            print "\n\nYou Got it!!!!"
            sleep(2)
            playagain=play_again()
            if playagain=='n':
                break

print "Thanks for playing... Goodbye!"
