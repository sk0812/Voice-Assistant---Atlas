# imports required functions and mmodules
from speak import speak, get_audio
import os

# shutsdown pc


def shutDown():
    speak("Are you sure you want to shut down the computer?")
    user_command = get_audio()
    if user_command == "yes":
        try:
            speak("ok, sir i am shutting down the computer")
            os.system("shutdown /s /t 1")
        except:
            speak(("sorry sir, i was unable to shut down the computer please try again"))
    else:
        print("ok sir, i won't shut down the computer")

# puts the computer to sleep


def sleep():
    speak("Are you sure you want to sleep the computer?")
    user_command = get_audio()
    if user_command == "yes":
        try:
            speak("ok, sir i am putting the computer to sleep")
            os.startfile(
                "C:/Users/siddh.HOME-DESKTOP.000/Documents/IMPORTANT/macro keyboard/scripts/sleep.exe")
        except:
            speak(
                "sorry sir, i was unable to put the computer to sleep. please try again")
    else:
        print("ok sir, i wont put the computer to sleep")

# locks and switches of the monitor


def lockMonitor():
    try:
        speak("ok, sir i am locking and turning of the monitor")
        os.startfile(
            "C:/Users/siddh.HOME-DESKTOP.000/Documents/IMPORTANT/macro keyboard/scripts/lock and turn off monitor.exe")
    except:
        speak(
            "sorry sir, i was unable to lock and and turn of the monitor. please try again")

# restarts the com[uter]


def restart():
    speak("Are you sure you want to restart the computer?")
    user_command = get_audio()
    if user_command == "yes":
        try:
            speak("ok sir, i am restarting the computer")
            os.system("shutdown /r /t 1")
        except:
            speak("sorry sir, i was unable to restart the computer. please try again")
    else:
        print("ok sir, i won't restart the computer")
