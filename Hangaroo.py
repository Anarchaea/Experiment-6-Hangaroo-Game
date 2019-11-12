import random
import time
words=['rice','chicken','park','skateboard','ball','computer','inductor','transformer']
secretWord = random.choice(words)
wl = len(secretWord)
lettersGuessed =[]
alp='abcdefghijklmnopqrstuvwxyz'
word=""
string=""


def start():
    print ("Welcome to Hangaroo!")
    print ("Let's play together!")
    time.sleep(2)


start()

def secw():
    secretWord=random.choice(words)
    wl=len(secretWord)
    ch=2*wl
    print("Guess the word with ", wl, "letters")
    print("You have ", ch, "tries!")
    time.sleep(2)
    
def Hangaroo():
    secretWord=random.choice(words)
    wl=len(secretWord)
    ch=2*wl
    word=""
    string=""
    i=0
    alp='abcdefghijklmnopqrstuvwxyz'
    secretWord = random.choice(words)
    lettersGuessed =[]

    while i<ch:
        x = input("Enter a letter: ").lower()
       
        for x in secretWord:
           if x not in lettersGuessed:
               word+=" _ "
               print("Oh no!")
       	   else:
               word+=x
               print("Nice")
        return word
        for x in alp:
           if x in lettersGuessed:
               alp.replace(x," ")
           else:
               string+=x
        return string
        ch+=1
                
secw()
Hangaroo()

print("You lose!")