import datetime
import subprocess
from speak import speak

def note(text):
    try:
        date = datetime.datetime.now()
        file_name = str(date).replace(":", "-") + "-note.txt"
        with open(file_name, "w") as f:
            f.write(text)

        subprocess.Popen(["notepad.exe", file_name])
    except:
        speak("sorry sir, i was unable to make a note")