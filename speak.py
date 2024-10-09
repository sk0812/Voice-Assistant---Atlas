# imports pyaudio and google speech recgonition
import pyttsx3
import speech_recognition as sr
import configparser


engine = pyttsx3.init()

config = configparser.ConfigParser()
config.read('config.ini')
rate = config['assistant']['speechRate']
rate = int(rate)
voices = engine.getProperty('voices')

# speak function
def speak(text):
    engine.setProperty('rate', rate)
    engine.say(text)
    engine.runAndWait()


# gets audio from user
def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Exception: " + str(e))

    return said.lower()


print("start")

while True:
    speak("ready")
    text = get_audio()
    print(text)