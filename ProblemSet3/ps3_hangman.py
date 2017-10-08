# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------
# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    swlistcopy = secretWord
    for i in secretWord:
        if i in lettersGuessed:
            swlistcopy = swlistcopy.replace(i, '')

    if swlistcopy == '':
        return True
    else:
        return False

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    wordcopy = secretWord
    for i in secretWord:
        if i not in lettersGuessed:
            if i in wordcopy:
                wordcopy = wordcopy.replace(i, '_ ')
    return wordcopy

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    alphabet = string.ascii_lowercase
    for i in lettersGuessed:
        if i in alphabet:
            alphabet = alphabet.replace(i, '')
    return alphabet

def hangman(secretWord):

    # Declare local variables
    guessedlist = []
    guesstimes = 8
    word = '_ ' * len(secretWord)
    availableltr = string.ascii_lowercase

    # Greeting
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is %d letters long.' % len(secretWord))
    print('------------')

    # start while loop
    while guesstimes > 0 and isWordGuessed(secretWord, guessedlist) == False:

    # report game situation
        print('You have %d guesses left' % guesstimes)
        print('Available letters: ' + availableltr)
        guessltr = input('Please guess a letter: ')

    # Outcome
        if guessltr in guessedlist:
            print("Oops! You've already guessed that letter: "+ word)
            print('------------')

        elif guessltr in secretWord:
            guessedlist.append(guessltr)
            word = getGuessedWord(secretWord, guessedlist)
            availableltr = getAvailableLetters(guessedlist)

            print('Good guess: ' + word)
            print('------------')

        elif guessltr not in secretWord:
            guessedlist.append(guessltr)
            availableltr = getAvailableLetters(guessedlist)
            guesstimes -= 1


            print('Oops! That letter is not in my word: ' + word)
            print('------------')

    if guesstimes > 0:
        print('Congratulations, you won!')

    else:
        print('Sorry, you ran out of guesses. The word was '+ secretWord +'.')

secretWord = chooseWord(loadWords()).lower()
hangman(secretWord)
# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord = chooseWord(wordlist).lower()
# hangman(secretWord)
