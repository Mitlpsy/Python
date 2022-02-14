from glob import glob
import random
import sys

n = ""
min = ""
max = ""
UserGuess = True

def RamdomNum ():
    global n
    global min
    global max
    Min ()
    Max ()
    n = random.randint(min,max)

def Min ():
    global min
    try:
        min = int(input ("Please enter Min number:"))
    except :
        print ("Error!! You must put number : ")
        Min ()

def Max ():
    global max
    try:
        max = int(input ("Please enter Max number:"))
    except :
        print ("Error!! You must put number : ")
        Max ()

def myuser():
    global n
    global UserGuess
    while UserGuess != n :

        try:
            UserGuess = int(input(":"))
        except: 
            print ("")
            myuser()
        if UserGuess > n :
            print ("Tooooooo High")
        elif UserGuess < n :
            print ("Toooooooo low")
        elif UserGuess == n :
            print ("you won") 
            Restart()

def START():
    RamdomNum ()
    myuser()

def Restart ():
    res = input("Do you want to return? Ans Y or N : ")
    if res.upper() == "Y":
        START()
    elif res.upper() == "N":
        sys.exit("Thank you")
    else : 
        Restart()


START()

 


