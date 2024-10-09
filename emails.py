# imports functions and modules
from speak import speak, get_audio
from websites import outlook, gmail
from browser_path import browser_path
import webbrowser

# chooses between school or personal emails


def choose_email():
    try:
        speak(
            "which one would you like me to open: your school email or your personal email")
        text = get_audio()
        if "school" in text:
            speak("opening your school emails")
            url = outlook
            webbrowser.get(browser_path).open(url)
        elif "personal" in text:
            speak("opening your personal emails")
            url = gmail
            webbrowser.get(browser_path).open(url)
    except:
        speak("sorry sir i was unable to open your email")