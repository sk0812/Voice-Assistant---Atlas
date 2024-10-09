# imports required function and modules
import random
from speak import speak

# random number between 2 numbers


def random_number(text):
    try:
        QUERY_LIST = text.split()
        unwanted_query = {"choose", "a", "random",
                        "number", "between", "and", "give", "me"}
        QUERY_LIST = [ele for ele in QUERY_LIST if ele not in unwanted_query]
        number1 = int(QUERY_LIST[0])
        number2 = int(QUERY_LIST[1])
        speak(random.randint(number1, number2))
    except:
        speak(f"sorry sir, i was unable to generate a random number between {number1} and {number2}. please try again")

