#imports modules and fucntions
import random
from speak import speak

#flips a coin
def flipCoin():
    try:
        flip_side = random.randint(0, 2)
        if flip_side == 1:
            speak("heads")
        else:
            speak("tails")
    except:
        speak("sorry sir, i was unable to flip a coin. please try again")