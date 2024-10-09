# imports required functions, variable and modules
from speak import speak
import webbrowser
from browser_path import browser_path
from speak import get_audio

# searches google


def searchGoogle(text):
    try:
        if "for" in text:
            text = text.replace("search google for", "")
        else:
            text = text.replace("search google", "")
        if text == "":
            speak("what would you like to search for")
            text = get_audio()
            url = (f"https://www.google.com/search?q={text}")
            speak(f"here is what i found for {text} on google.")
            webbrowser.get(browser_path).open(url)
        else:
            speak("searching...")
            url = (f"https://www.google.com/search?q={text}")
            speak(f"here is what i found for {text} on google.")
            webbrowser.get(browser_path).open(url)
    except:
        speak(f"sorry sir i was unable to search google for {text}. please try again")

# searches youtube


def searchYoutube(text):
    try:
        if "for" in text:
            text = text.replace("search youtube for", "")
        else:
            text = text.replace("search youtube", "")
        if text == "":
            speak("what would you like to search for")
            text = get_audio()
            url = (f"https://www.youtube.com/results?search_query={text}")
            speak(f"here is what i found for {text} on youtube.")
            webbrowser.get(browser_path).open(url)
        else:
            speak("searching...")
            url = (f"https://www.youtube.com/results?search_query={text}")
            speak(f"here is what i found for {text} on youtube.")
            webbrowser.get(browser_path).open(url)
    except:
        speak(f"sorry sir i was unable to search youtube for {text}. please try again")
# searches amazon


def searchAmazon(text):
    try:
        if "for" in text:
            text = text.replace("search amazon for", "")
        else:
            text = text.replace("search amazon", "")
        if text == "":
            speak("what would you like to search for")
            text = get_audio()
            url = (f"https://www.amazon.co.uk/s?k={text}")
            speak(f"here is what i found for {text} in amazon.")
            webbrowser.get(browser_path).open(url)
        else:
            speak("searching...")
            url = (f"https://www.amazon.co.uk/s?k={text}")
            speak(f"here is what i found for {text} in amazon.")
            webbrowser.get(browser_path).open(url)
    except:
        speak(f"sorry sir i was unable to search amazon for {text}")

# searches ebay


def searchEbay(text):
    try:
        if "for" in text:
            text = text.replace("search ebay for", "")
        else:
            text = text.replace("search ebay", "")
        if text == "":
            speak("what would you like to search for")
            text = get_audio()
            url = (
                f"https://www.ebay.co.uk/sch/i.html?_from=R40&_trksid=m570.l1313&_nkw={text}")
            speak("here is what i found for {text} in ebay")
            webbrowser.get(browser_path).open(url)
        else:
            speak("searching...")
            url = (
                f"https://www.ebay.co.uk/sch/i.html?_from=R40&_trksid=m570.l1313&_nkw={text}")
            speak("here is what i found for {text} in ebay")
            webbrowser.get(browser_path).open(url)
    except:
        speak(f"sorry sir, i was unable to search ebay for {text}. please try again")