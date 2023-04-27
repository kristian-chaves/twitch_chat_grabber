# takes from word list, checks for words, 5 inputs
# 
import time

import random
import re # grep
import colorama
from colorama import Fore
from colorama import init
init(autoreset=True)

global words_list
global valid_words_list

def intialize_elements():
    global valid_words_list
    global words_list
    valid_words_list = {}
    # save all valid words
    words = open("words_valid.txt")
    for i in words.readlines():
        i = i.strip()
        q = {i: i}
        valid_words_list.update(q);
    
    # save all words
    words_list = open("words_list.txt").read().splitlines()

def user_guess():
    # lets user guess a word, checks if user's guess is valid, returns user guess if valid
    valid_input = False
    inputs = []
    # parse through inputs, if length 5 save them
    words = open("Output.txt", encoding="utf8")
    for i in words.readlines():
        i = i.split(":")
        i = i[2].strip()    
        if(len(i) == 5):
            inputs.append(i)
    words.close()

    while valid_input == False:
        guess = random.choice(inputs)
        if(guess in valid_words_list):
            #re-write Output.txt
            file = open('Output.txt', 'w')
            file.write("q:q: spade")
            file.close()
            return guess
        print(Fore.RED + "invalid word\n")

def word_compare(word, guess):
    # compares the characters in the guess and word, outputs squares
    n = 0
    # go through letters, create process to ensure correct number of yellow letters
    letter_list = []
    for x in word:
        letter_list.append(x)
    for x in guess:
        if word[n] == x:
            #print green square
            print(Fore.GREEN + x, end = "")
            letter_list.remove(x)
        elif x in letter_list:
            #print yellow square
            print(Fore.YELLOW + x, end = "")
            letter_list.remove(x)
        else:
            #print grey square
            print(Fore.WHITE + x, end = "")
        n +=1 
    print("\n")
    if word == guess:
        return True
    else:
        return False


if __name__ == "__main__":
    word = intialize_elements()
    play = "Y"
    while(play == "Y"):
        word = random.choice(words_list)
        word_found = False
        guesses = 0
        while guesses < 6 and word_found == False:
            guesses += 1
            print(f"guess: {guesses}/6")
            time.sleep(15)
            guess = user_guess()
            word_found = word_compare(word, guess)
            
        if word_found == True:
            print("you win!")
        else:
            print("you lose")
        
        play = input("Do you want to continue? Y/N: ")
        print("\n")

    
        