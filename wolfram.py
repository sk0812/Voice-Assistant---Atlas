# imports the required modules and functions
import wolframalpha
from speak import speak

# wolfram api
client = wolframalpha.Client('L99JJA-3JH7E7TVTJ')

# gets the input from the user and gives an output from wolframaplha


def wolfram(text):
    try:
        res = client.query(text)
        output = next(res.results).text
        speak(output)
        print(output)
    except:
            speak("sorry sir, i was unable to solve that at the moment.")