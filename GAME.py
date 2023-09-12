#!usr/bin/python3
#random number guess game
#make by :USMAN
#---------------import-Modules------------------#
import os,random,time
from os import system as Jagu
from time import sleep as USMAN
from random import randint as Shuffle
#-------------------Colours---------------------#
green = "\033[1;32m"
white = "\033[1;37m"
yellow = "\033[1;33m"
purple = "\033[1;35m"
red = "\033[1;31m"
asmani = "\033[1;36m"
#---------------Logo-or-Banner------------------#
logo = f'''{yellow}____ _  _ ____ ____ ____ 
| __ |  | |___ [__  [__  
|__] |__| |___ ___] ___] GAME {red}2.0
{yellow}————————————————————————————————————————
       {asmani}-:Guess The Random Number:-
{yellow}————————————————————————————————————————{white}'''
#---------------Owner-Security------------------#
def security():
    Jagu('clear');print(logo)
    print(f'[{green}!{white}] {asmani}Password Access Needed!{white}')
    print(40*f'{yellow}—{white}')
    passJxR = input(f'[{green}?{white}] {asmani}Enter Password:{white}')
    if passJxR in ['USMAN','USMAN ']:
        print('')
        print(f'{green}             Access Granted!{white}')
        USMAN(1.5);USMAN()
    else:
        print('')
        print(f'             \a{red}Access Denied!{white}')
        USMAN(1.5);security()
#------------------Main-Menu--------------------#
def USMAN():
    Jagu('clear');print(logo)
    print(f"[{green}01{white}] {asmani}Let's play{white}")
    print(f"[{green}02{white}] {asmani}How to play{white}")
    print(f"[{green}03{white}] {asmani}About levels [Easy/Medium/Hard]{white}")
    print(f"[{green}04{white}] {asmani}Back To Security{white}")
    print(f"[{green}00{white}] {asmani}Exit From The Program{white}")
    print(40*f'{yellow}—{white}')
    jagu = input(f'[{green}?{white}] {asmani}Choose:{white}')
    if jagu in ['01','1']:
        choose()
    elif jagu in ['02','2']:
        inst()
    elif jagu in ['03','3']:
        level()
    elif jagu in ['04','4']:
        security()
    elif jagu in ['00','0']:
        quit(f"[{green}•{white}] {asmani}Thanks For Playing:){white}")
    else:
        print(f'[{green}!{white}] \a{red}Choose a valid option!{white}')
        USMAN(2);USMAN()      
#----------------About-Levels-------------------#
def level():
    Jagu('clear');print(logo)
    print(f'    {purple}In "Easy" level you have to find')
    print(f'   a random number between 1 upto 100{white}')
    print(40*f'{yellow}—{white}')
    print(f'    {purple}In "Medium" level you have to find')
    print(f'   a random number between 1 upto 200{white}')
    print(40*f'{yellow}—{white}')
    print(f'    {purple}In "Hard" level you have to find')
    print(f'   a random number between 1 upto 300{white}')
    print(40*f'{yellow}—{white}')
    back = input(f'{asmani}Press enter for main menu{white}')
    Jagu('clear');print(logo);USMAN()
#-------------Important-Instructions------------#
def inst():
    Jagu('clear');print(logo)
    print(f'      {purple}Some importants instructions.{white}')
    print(40*f'{yellow}—{white}')
    print(f'    {purple}You have to guess a random number')
    print(f' depend on your level if number is high')
    print(f'  then put a lower number, if number')
    print(f'       is low put a higher number{white}')
    print(40*f'{yellow}—{white}')
    clear = input(f'{asmani}Press enter for main menu{white}')
    Jagu('clear');print(logo);USMAN()
#----------------Levels-Category----------------#
def choose():
    Jagu('clear');print(logo)
    print(f'[{green}01{white}] {asmani}Easy     "10 lives"{white}')
    print(f'[{green}02{white}] {asmani}Medium   "12 lives"{white}')
    print(f'[{green}03{white}] {asmani}Hard     "15 lives"{white}')
    print(f'[{green}00{white}] {asmani}Back to main menu{white}')
    print(40*f'{yellow}—{white}')
    chose = input(f'[{green}?{white}] {asmani}Choose:{white}')
    if chose in ['01','1']:
        easy()
    elif chose in ['02','2']:
        medium()
    elif chose in ['03','3']:
        hard()
    elif chose in ['00','0']:
        USMAN()
    else:
        print(f'[{green}?{white}] \a{red}Choose valid option!{white}')
        USMAN(2);choose()
#--------------------Easy-----------------------#
def easy():
    Jagu('clear');print(logo)
    print(f'{asmani}Category: {green}Easy{white}')
    print('')
    secretNumber = Shuffle(1,100)
    print(f'{asmani}Im thinking a number between {purple}1{asmani} and {purple}100{white}')

    for guessesTaken in range(1,10):
        guess = int(input(f'{asmani}Take a guess: {white}'))
        
        if guess < secretNumber:
            print(f'{red}Your guess is low{white}')
        elif guess > secretNumber:
            print(f'{red}Your guess is high{white}')
        else:
            break
        
    if guess == secretNumber:
        print(f'{green}Wow! you guessed my number in ' + str(guessesTaken) + ' guesses')
    else:
        print(f'{red}Nope! number i was thinking of is ' + str(secretNumber))
    USMAN(3)
    Jagu('clear');print(logo);choose()
#-------------------Medium----------------------#
def medium():
    Jagu('clear');print(logo)
    print(f'{asmani}Category: {green}Medium{white}')
    print('')
    secretNumber = Shuffle(1,200)
    print(f'{asmani}Im thinking a number betwe;en {purple}1{asmani} and {purple}200{white}')

    for guessesTaken in range(1,12):
        guess = int(input(f'{asmani}Take a guess: {white}'))
    
        if guess < secretNumber:
            print(f'{red}Your guess is low{white}')
        elif guess > secretNumber:
            print(f'{red}Your guess is high{white}')
        else:
            break
        
    if guess == secretNumber:
        print(f'{green}Wow! you guessed my number in ' + str(guessesTaken) + ' guesses')
    else:
        print(f'{red}Nope! number i was thinking of is ' + str(secretNumber))
    USMAN(3)
    Jagu('clear');print(logo);choose()
#--------------------Hard-----------------------#
def hard():   
    Jagu('clear');print(logo)
    print(f'{asmani}Category: {green}Hard{white}')
    print('')
    secretNumber = Shuffle(1,300)
    print(f'{asmani}Im thinking a number between {purple}1{asmani} and {purple}300{white}')

    for guessesTaken in range(1,15):
        guess = int(input(f'{asmani}Take a guess: {white}'))
    
        if guess < secretNumber:
            print(f'{red}Your guess is low{white}')
        elif guess > secretNumber:
            print(f'{red}Your guess is high{white}')
        else:
            break
        
    if guess == secretNumber:
        print(f'{green}Wow! you guessed my number in ' + str(guessesTaken) + ' guesses')
    else:
        print(f'{red}Nope! number i was thinking of is ' + str(secretNumber))
    USMAN(3)
    Jagu('clear');print(logo);choose()

security()
    