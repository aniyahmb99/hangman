import random
import time
import os

# HangMan

 
    
def hangman(word):
    display = '_' * len(word)
    count = 0
    limit = 5
    letters = list(word)
    guessed = []
    while count > limit:
        guess = input(f'Hangman Word: {display} Enter your guess: \n')
        print(guess)
        
    
hangman('hello')
    
    
    
# def playGame():

def playAgain():
    question = 'Do you want to play again? y = yes, n = no \n'
    responses = ['y', 'n']
    answer = input(question)
      
    if answer.lower() == 'y':
        return True
    elif answer.lower() not in responses:
        raise ValueError('Please respond with y or n')
        
    else:
        return False    
playAgain() 
    