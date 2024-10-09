# imports required modules
import datetime
import os
import os.path
import subprocess
import webbrowser
import sys
import configparser


# imports functions and variables from other files
from browser_path import browser_path
from speak import speak, get_audio
from applications import *
from websites import *


config = configparser.ConfigParser()
config.read('config.ini')

assistantName = config['assistant']['name']
userName = config['user']['name']
userAge = config['user']['age']
wakeMessage = config['assistant']['wake_message']

WAKE = config['assistant']['wakeWord']

print("Start")

# carries the program running


while True:
    try:
        print("Listening")
        text = get_audio()

        # when you say the wake word it will speak ready
        if text.count(WAKE) > 0:
            speak(wakeMessage)
            text = get_audio()


            # weather
            from weather import current_weather, weekend_weather, tom_weather, next_week_weather, today_weather, monday_weather, tuesday_weather, wednesday_weather, thursday_weather, friday_weather, Saturday_weather, sunday_weather, location_weather
            WEATHER_STRS = ["weather"]
            for phrase in WEATHER_STRS:
                if phrase in text:
                    print("weather module")
                    QUERY_LIST = text.split()
                    unwanted_words = {"weather", "how", "is",   "the",
                                      "what", "how's", "what's", "next", "was", "on"}
                    QUERY_LIST = {
                        word for word in QUERY_LIST if word not in unwanted_words}
                    print(QUERY_LIST)
                    if "current" in QUERY_LIST:
                        current_weather()

                    elif "today" in QUERY_LIST:
                        today_weather()

                    elif "week" in QUERY_LIST:
                        next_week_weather()

                    elif "weekend" in QUERY_LIST:
                        weekend_weather()

                    elif "tomorrow" in QUERY_LIST:
                        tom_weather()

                    elif "monday" in QUERY_LIST:
                        monday_weather()

                    elif "tuesday" in QUERY_LIST:
                        tuesday_weather()

                    elif "wednesday" in QUERY_LIST:
                        wednesday_weather()

                    elif "thursday" in QUERY_LIST:
                        thursday_weather()

                    elif "friday" in QUERY_LIST:
                        friday_weather()

                    elif "saturday" in QUERY_LIST:
                        Saturday_weather()

                    elif "sunday" in QUERY_LIST:
                        sunday_weather()
                        
                    elif "in" in QUERY_LIST:
                        location_weather(text)

                    elif not QUERY_LIST:
                        current_weather()
                    subprocess.call(sys.executable + ' "' +
                                    os.path.realpath(__file__) + '"')

            from wish_list_db import add_item, deleteAll, remove_item, countItems
            WISH_LIST_STRS = ["wishlist"]
            for phrase in WISH_LIST_STRS:
                if phrase in text:
                    print("wish list module")
                    if "add" in text:
                        add_item(text)
                    elif "delete all" in text:
                        deleteAll()
                    elif "remove" in text:
                        remove_item(text)
                    elif "how many items" in text:
                        countItems()
                    subprocess.call(sys.executable + ' "' +
                                    os.path.realpath(__file__) + '"')

            SPEAK_RANDOM_STRS = ["speak" and "random"]
            for phrase in SPEAK_RANDOM_STRS:
                if phrase in text:
                    speak("okay sir, i will speak something completely random, The quick brown fox jumps over the lazy dog. A fun fact about that sentence is that it contains every letter in the alphabet")
                    subprocess.call(sys.executable + ' "' +
                                    os.path.realpath(__file__) + '"')
            # misc
            # reply to thanks you
            THANK_STRS = ["thanks", "thank you"]
            for phrase in THANK_STRS:
                if phrase in text:
                    speak("Your welcome! Always happy to help")
                    subprocess.call(sys.executable + ' "' +
                                    os.path.realpath(__file__) + '"')

                # reply to good morning
            MORNING_STRS = ["good morning", "morning"]
            for phrase in MORNING_STRS:
                if phrase in text:
                    speak("good morning boss, hope you have a good day")
                    subprocess.call(sys.executable + ' "' +
                                    os.path.realpath(__file__) + '"')

                # reply to good afternoon
            AFTERNOON_STRS = ["good afternoon", "afternoon"]
            for phrase in AFTERNOON_STRS:
                if phrase in text:
                    speak(
                        "Good afternoon boss, hope you are having a good day. Let me know if you need any help")
                    subprocess.call(sys.executable + ' "' +
                                    os.path.realpath(__file__) + '"')
                # reply to good evening
            EVENING_STRS = ["evening", "good evening"]
            for phrase in EVENING_STRS:
                if phrase in text:
                    speak("Good evening, hope you had a great day")
                    subprocess.call(sys.executable + ' "' +
                                    os.path.realpath(__file__) + '"')
                # reply to good night
            NIGHT_STRS = ["good night", "night"]
            for phrase in NIGHT_STRS:
                if phrase in text:
                    speak("Good night! sweet dreams!")
                    subprocess.call(sys.executable + ' "' +
                                    os.path.realpath(__file__) + '"')

                # better then other voice assistants
            BETTER_STRS = ["are you better than google", "are you better than alexa",
                           "are you better than siri", "are you better than cortana"]
            for phrase in BETTER_STRS:
                if phrase in text:
                    speak(
                        "Is that even a question to ask? Of course I am, because i got programmed by the best")
                    subprocess.call(sys.executable + ' "' +
                                    os.path.realpath(__file__) + '"')
                # name
            NAME_STRS = ["your name", "what is your name"]
            for phrase in NAME_STRS:
                if phrase in text:
                    speak(
                        f"my name is {assistantName}, your personal assistant")
                    subprocess.call(sys.executable + ' "' +
                                    os.path.realpath(__file__) + '"')

                # who are you
            WHO_ARE_YOU_STRS = ["who are you"]
            for phrase in WHO_ARE_YOU_STRS:
                if phrase in text:
                    speak(
                        f"Hello, i am {assistantName}. your personal assistant. I am hear to make your life easier. You can command me to perform various tasks such as opening websites and applications. To find out more about what i can do say: Atlas, what can you do?")
                    subprocess.call(sys.executable + ' "' +
                                    os.path.realpath(__file__) + '"')
            import random
            from whatCanYouDo import what_can_you_do
            WHAT_CAN_YOU_DO_SRS = ["what can you do"]
            for phrase in WHAT_CAN_YOU_DO_SRS:
                if phrase in text:
                    print("what can you do module")
                    items = random.sample(what_can_you_do, k=3)
                    speak("A few things you can ask me are")
                    print(items)
                    speak(items)
                    subprocess.call(sys.executable + ' "' +
                                    os.path.realpath(__file__) + '"')

            CURRENT_DAY = ["day"]
            if phrase in CURRENT_DAY:
                if phrase in text:
                    print("day module")
                    current = datetime.datetime.now()
                    day = current.strftime("%A")
                    speak(f"today is {day}, sir")
                    subprocess.call(sys.executable + ' "' +
                                    os.path.realpath(__file__) + '"')

            WHAT_IS_MY_NAME_STRS = ["what is my name"]
            for phrase in WHAT_IS_MY_NAME_STRS:
                if phrase in text:
                    speak(f"You are {userName}, how could you forget that!!")
                    subprocess.call(sys.executable + ' "' +
                                    os.path.realpath(__file__) + '"')

            HOW_OLD_AM_I_STRS = ["how old am i", "what is my age"]
            for phrase in HOW_OLD_AM_I_STRS:
                if phrase in text:
                    speak(f"you are {userAge} years old, sir")

            HOW_ARE_YOU_STRS = ["how are you"]
            for phrase in HOW_ARE_YOU_STRS:
                if phrase in text:
                    speak(
                        "i am doing very well. thank you for asking. How are you doing, boss?")

            # current time
            TIME_STRS = ["the time"]
            for phrase in TIME_STRS:
                if phrase in text:
                    print("time module")
                    strTime = datetime.datetime.now().strftime("%H:%M")
                    ran_number = random.randint(1, 10)
                    if ran_number == 1:
                        speak("time to get a watch")
                        speak(f"haha, just joking it is {strTime}")
                    else:
                        speak(f", the time is {strTime}")
                    subprocess.call(sys.executable + ' "' +
                                    os.path.realpath(__file__) + '"')

            from movies import search_movie, top_movies, worst_movies
            MOVIE_INFO_STRS = ["movie"]
            for phrase in MOVIE_INFO_STRS:
                if phrase in text:
                    if "movie" and "information" in text:
                        search_movie(text)
                    elif "top" in text:
                        top_movies()
                    elif "bottom" or "worst" in text:
                        worst_movies()

                    subprocess.call(sys.executable + ' "' +
                                    os.path.realpath(__file__) + '"')

                # exits programz
            EXIT_STRS = ["exit", "power off"]
            for phrase in EXIT_STRS:
                if phrase in text:
                    speak("exitting")
                    speak("come back soon")
                    exit()

                # make a note
            from note import note
            NOTE_STRS = ["make a note", "write this down", "remember this"]
            for phrase in NOTE_STRS:
                if phrase in text:
                    print("notes module")
                    speak("What would you like me to write down?")
                    note_text = get_audio()
                    note(note_text)
                    speak("ok sir, I've made a note of that.")
                    subprocess.call(sys.executable + ' "' +
                                    os.path.realpath(__file__) + '"')

                # search module
                # search google
            from search import searchGoogle
            SEARCH_GOOGLE_STRS = ["search google", "search the web"]
            for phrase in SEARCH_GOOGLE_STRS:
                if phrase in text:
                    print("google search")
                    searchGoogle(text)
                    subprocess.call(sys.executable + ' "' +
                                    os.path.realpath(__file__) + '"')

                # search youtube
            from search import searchYoutube
            SEARCH_YOUTUBE_STRS = ["search youtube"]
            for phrase in SEARCH_YOUTUBE_STRS:
                if phrase in text:
                    print("youtube search")
                    searchYoutube(text)
                    subprocess.call(sys.executable + ' "' +
                                    os.path.realpath(__file__) + '"')

                # search amazon
            from search import searchAmazon
            SEARCH_AMAZON_STRS = ["search amazon"]
            for phrase in SEARCH_AMAZON_STRS:
                if phrase in text:
                    print("amazon search")
                    searchAmazon(text)
                    subprocess.call(sys.executable + ' "' +
                                    os.path.realpath(__file__) + '"')

                # search ebay
            from search import searchEbay
            SEARCH_EBAY_STRS = ["search ebay"]
            for phrase in SEARCH_EBAY_STRS:
                if phrase in text:
                    print("ebay search")
                    searchEbay(text)
                    subprocess.call(sys.executable + ' "' +
                                    os.path.realpath(__file__) + '"')

                # dictionary module

                # definitions
            from dictionary import definition
            DEFINITIONS_STRS = ["meaning", "definition", "mean", "define"]
            for phrase in DEFINITIONS_STRS:
                if phrase in text:
                    print("defintion module")
                    definition(text)
                    subprocess.call(sys.executable + ' "' +
                                    os.path.realpath(__file__) + '"')

                # synonyms
            from dictionary import synonym
            SYNONYM_STRS = ["synonyms", "synonym",
                            "words similar to", "word similar to"]
            for phrase in SYNONYM_STRS:
                if phrase in text:
                    print("synonym module")
                    synonym(text)
                    subprocess.call(sys.executable + ' "' +
                                    os.path.realpath(__file__) + '"')

                # antonyms
            from dictionary import antonym
            ANTONYM_STRS = ["antonyms", "antonym",
                            "words opposite to", "word opposite to"]
            for phrase in ANTONYM_STRS:
                if phrase in text:
                    print("antonym module")
                    synonym(text)
                    subprocess.call(sys.executable + ' "' +
                                    os.path.realpath(__file__) + '"')

                # dice roll
            DICE_ROLL_STRS = ["roll a dice", "dice roll"]
            for phrase in DICE_ROLL_STRS:
                if phrase in text:
                    print("roll a dice module")
                    speak(random.randint(1, 6))
                    subprocess.call(sys.executable + ' "' +
                                    os.path.realpath(__file__) + '"')

                # coin toss
            from flip_coin import flipCoin
            COIN_TOSS_STRS = ["flip a coin",
                              "coin toss", "coin flip", "toss a coin"]
            for phrase in COIN_TOSS_STRS:
                if phrase in text:
                    print("coin flip module")
                    flipCoin()
                    subprocess.call(sys.executable + ' "' +
                                    os.path.realpath(__file__) + '"')

                # random number
            from random_number import random_number
            RANDOM_NUMBER_STRS = ["random number"]
            for phrase in RANDOM_NUMBER_STRS:
                if phrase in text:
                    print("random number module")
                    random_number(text)
                    subprocess.call(sys.executable + ' "' +
                                    os.path.realpath(__file__) + '"')

            from joke import jokes
            JOKE_STRS = ["joke"]
            for phrase in JOKE_STRS:
                if phrase in text:
                    print("joke module")
                    try:
                        joke = random.choice(jokes)
                        print(joke)
                        speak(joke)
                        subprocess.call(sys.executable + ' "' +
                                        os.path.realpath(__file__) + '"')
                    except:
                        speak(
                            "sorry sir, i was unable to tell you a joke. please try again")
                # opens youtube
            YOUTUBE_STRS = ["youtube"]
            for phrase in YOUTUBE_STRS:
                if phrase in text:
                    try:
                        speak(
                            "ok i am opening youtube, but you can also ask to search youtube by saying search youtube for")
                        url = youtube
                        webbrowser.get(browser_path).open(url)
                        subprocess.call(sys.executable + ' "' +
                                        os.path.realpath(__file__) + '"')
                    except:
                        speak("sorry sir, i was unable to open youtube")

                # opens habsnet
            HABSNET_STRS = ["habsnet"]
            for phrase in HABSNET_STRS:
                if phrase in text:
                    try:
                        speak("ok i am opening habsnet")
                        url = habsnet
                        webbrowser.get(browser_path).open(url)
                        subprocess.call(sys.executable + ' "' +
                                        os.path.realpath(__file__) + '"')
                    except:
                        speak("sorry sir, i was unable to open habsnet")

                # opens outlook
            SCHOOL_EMAIl_STRS = ["school email",
                                 "school email" "open my school emails"]
            for phrase in SCHOOL_EMAIl_STRS:
                if phrase in text:
                    try:
                        speak("ok i am opening your school email")
                        url = outlook
                        webbrowser.get(browser_path).open(url)
                        subprocess.call(sys.executable + ' "' +
                                        os.path.realpath(__file__) + '"')
                    except:
                        speak("sorry sir, i was unable to open your school emails")

            BBC_BITESIZE = ["bbc bitesize"]
            if phrase in BBC_BITESIZE:
                if phrase in text:
                    try:
                        speak("ok sir, opening  BBC Bitesize")
                        url = bbcBitesize
                        webbrowser.get(browser_path).open(url)
                        subprocess.call(sys.executable + ' "' +
                                        os.path.realpath(__file__) + '"')
                    except:
                        speak("sorry sir, i was unable to open bbc bitesize")

            GOOGLE_STRS = ["google"]
            if phrase in GOOGLE_STRS:
                if phrase in text:
                    try:
                        speak(
                            "ok sir, i am opening google, but you can also ask me to search google by saying search google for")
                        url = google
                        webbrowser.get(browser_path).open(url)
                        subprocess.call(sys.executable + ' "' +
                                        os.path.realpath(__file__) + '"')
                    except:
                        speak("sorry sir, i was unable to open google")

            GITHUB_STRS = ["github"]
            if phrase in GITHUB_STRS:
                if phrase in text:
                    try:
                        speak("ok sir, i am opening github")
                        url = github
                        webbrowser.get(browser_path).open(url)
                        subprocess.call(sys.executable + ' "' +
                                        os.path.realpath(__file__) + '"')
                    except:
                        speak("sorry sir, i was unable to open github")

            GOOGLE_DRIVE_STRS = ["drive"]
            if phrase in GOOGLE_DRIVE_STRS:
                if phrase in text:
                    try:
                        speak("ok sir, i am opening your google drive")
                        url = googleDrive
                        webbrowser.get(browser_path).open(url)
                        subprocess.call(sys.executable + ' "' +
                                        os.path.realpath(__file__) + '"')
                    except:
                        speak("sorry sir, i was unable to open google drive")

            BBC_STRS = ["bbc"]
            if phrase in BBC_STRS:
                if phrase in text:
                    try:
                        url = bbc
                        speak("ok sir, i am opening bbc")
                        webbrowser.get(browser_path).open(url)
                        subprocess.call(sys.executable + ' "' +
                                        os.path.realpath(__file__) + '"')
                    except:
                        speak("sorry sir, i was unable to open bbc")

            IMDB_STRS = ["imdb"]
            if phrase in IMDB_STRS:
                if phrase in text:
                    try:
                        url = imdb
                        speak("ok sir, i am opening imdb")
                        webbrowser.get(browser_path).open(url)
                        subprocess.call(sys.executable + ' "' +
                                        os.path.realpath(__file__) + '"')
                    except:
                        speak("sorry sir, i was unable to open imdb")

            TWITTER_STRS = ["twitter"]
            if phrase in TWITTER_STRS:
                if phrase in text:
                    try:
                        speak("ok sir, i am opening twitter")
                        url = twitter
                        webbrowser.get(browser_path).open(url)
                        subprocess.call(sys.executable + ' "' +
                                        os.path.realpath(__file__) + '"')
                    except:
                        speak("sorry sir, i was unable to open twitter")

            FACEBOOK_STRS = ["facebook"]
            if phrase in FACEBOOK_STRS:
                if phrase in text:
                    try:
                        speak("ok sir, i am opening facebook")
                        url = facebook
                        webbrowser.get(browser_path).open(url)
                        subprocess.call(sys.executable + ' "' +
                                        os.path.realpath(__file__) + '"')
                    except:
                        speak("sorry sir, i was unable to open facebook")

            YELP_STRS = ["yelp"]
            if phrase in YELP_STRS:
                if phrase in text:
                    try:
                        speak("ok sir, i am opening yelp")
                        url = yelp
                        webbrowser.get(browser_path).open(url)
                        subprocess.call(sys.executable + ' "' +
                                        os.path.realpath(__file__) + '"')
                    except:
                        speak("sorry sir, i was unable to open yelp")

            REDDIT_STRS = ["reddit"]
            if phrase in REDDIT_STRS:
                if phrase in text:
                    try:
                        speak("ok sir, i am opening reddit")
                        url = reddit
                        webbrowser.get(browser_path).open(url)
                        subprocess.call(sys.executable + ' "' +
                                        os.path.realpath(__file__) + '"')
                    except:
                        speak("sorry sir, i was unable to open reddit")

            PINTEREST_STRS = ["pinterest"]
            if phrase in PINTEREST_STRS:
                if phrase in text:
                    try:
                        speak("ok sir, i am opening pinterest")
                        url = pinterest
                        webbrowser.get(browser_path).open(url)
                        subprocess.call(sys.executable + ' "' +
                                        os.path.realpath(__file__) + '"')
                    except:
                        speak("sorry sir, i was unable to open pinterest")

            TRIPADVISOR_STRS = ["tripadvisor"]
            if phrase in TRIPADVISOR_STRS:
                if phrase in text:
                    try:
                        speak("ok sir, i am opening tripadvisor")
                        url = tripadvisor
                        webbrowser.get(browser_path).open(url)
                        subprocess.call(sys.executable + ' "' +
                                        os.path.realpath(__file__) + '"')
                    except:
                        speak("sorry sir i was unable to open tripadvisor")

            ETSY_STRS = ["etsy"]
            if phrase in ETSY_STRS:
                if phrase in text:
                    try:
                        speak("ok sir, i am opening etsy")
                        url = etsy
                        webbrowser.get(browser_path).open(url)
                        subprocess.call(sys.executable + ' "' +
                                        os.path.realpath(__file__) + '"')
                    except:
                        speak("sorry sir i was unable to open etsy")

            QUORA_STRS = ["quora"]
            if phrase in QUORA_STRS:
                if phrase in text:
                    try:
                        speak("ok sir, i am opening quora")
                        url = quora
                        webbrowser.get(browser_path).open(url)
                        subprocess.call(sys.executable + ' "' +
                                        os.path.realpath(__file__) + '"')
                    except:
                        speak("sorry sir i was unable to open quora")

            NETFLIX_STRS = ["netflix"]
            if phrase in NETFLIX_STRS:
                if phrase in text:
                    try:
                        speak("ok sir, i am opening netflix")
                        url = netflix
                        webbrowser.get(browser_path).open(url)
                        subprocess.call(sys.executable + ' "' +
                                        os.path.realpath(__file__) + '"')
                    except:
                        speak("sorry sir i was unable to open netflix")

            PAYPAL_STRS = ["paypal"]
            if phrase in PAYPAL_STRS:
                if phrase in text:
                    try:
                        speak("ok sir, i am opening paypal")
                        url = paypal
                        webbrowser.get(browser_path).open(url)
                        subprocess.call(sys.executable + ' "' +
                                        os.path.realpath(__file__) + '"')
                    except:
                        speak("sorry sir i was unable to open paypal")

                # openes smhw
            SMHW_STRS = ["what homework do I have",
                         "what homework has been set", "show my homework"]
            for phrase in SMHW_STRS:
                if phrase in text:
                    try:
                        speak("ok sir, opening your homeworks")
                        url = smhw
                        webbrowser.get(browser_path).open(url)
                        subprocess.call(sys.executable + ' "' +
                                        os.path.realpath(__file__) + '"')
                    except:
                        speak("sorry sir, i was unable to open show my homework")

                # opens downloads folder
            DOWNLOADS_STRS = ["downloads folder",
                              "show my downloads", "open downloads folder"]
            for phrase in DOWNLOADS_STRS:
                if phrase in text:
                    try:
                        speak("ok sir, i am opening your downloads folder")
                        os.startfile(download_path)
                        subprocess.call(sys.executable + ' "' +
                                        os.path.realpath(__file__) + '"')
                    except:
                        speak("sorry sir, i was unable to open your downloads folder")

                # opens folder called important
            IMPORTANT_STRS = ["important folder",
                              "show my important folder", "open important folder"]
            for phrase in IMPORTANT_STRS:
                if phrase in text:
                    try:
                        speak("ok sir, i am opening your important folder")
                        os.startfile(important_path)
                        subprocess.call(sys.executable + ' "' +
                                        os.path.realpath(__file__) + '"')
                    except:
                        speak("sorry sir, i was unable to open your important folder")

                # open school folder
            SCHOOL_FOLDER_STRS = ["school folder", "open my school folder"]
            for phrase in SCHOOL_FOLDER_STRS:
                if phrase in text:
                    try:
                        speak("ok sir, opening your school folder")
                        os.startfile(school_path)
                        subprocess.call(sys.executable + ' "' +
                                        os.path.realpath(__file__) + '"')
                    except:
                        speak("sorry sir, i was unable to open your school folder")

                # opens amazon
            AMAZON_STRS = ["amazon"]
            for phrase in AMAZON_STRS:
                if phrase in text:
                    try:
                        speak("ok sir, opening amazon")
                        url = amazon
                        webbrowser.get(browser_path).open(url)
                        subprocess.call(sys.executable + ' "' +
                                        os.path.realpath(__file__) + '"')
                    except:
                        speak("sorry sir, i was unable to open amazon")
                # opens ebay
            EBAY_STRS = ["eBay"]
            for phrase in EBAY_STRS:
                if phrase in text:
                    try:
                        speak("ok sir, opening ebay")
                        url = ebay
                        webbrowser.get(browser_path).open(url)
                        subprocess.call(sys.executable + ' "' +
                                        os.path.realpath(__file__) + '"')
                    except:
                        speak("sorry sir, i was unable to open ebay")

            AIM_TRAINER_STRS = ["3d aim trainer",
                                "aim trainer", "play aim trainer", "train my aim"]
            for phrase in AIM_TRAINER_STRS:
                if phrase in text:
                    try:
                        speak("ok sir, opening 3d Aim trainer ")
                        url = aim_trainer
                        webbrowser.get(browser_path).open(url)
                        subprocess.call(sys.executable + ' "' +
                                        os.path.realpath(__file__) + '"')
                    except:
                        speak("sorry sir, i was unable to open 3d aim trainer")

                # opens gmail
            GMAIL_STRS = ["open gmail", "open my personal emails"]
            for phrase in GMAIL_STRS:
                if phrase in text:
                    try:
                        speak("ok sir, i am opening your gmail")
                        url = gmail
                        webbrowser.get(browser_path).open(url)
                        subprocess.call(sys.executable + ' "' +
                                        os.path.realpath(__file__) + '"')
                    except:
                        speak("sorry sir, i was unable to open your gmail")


            from emails import choose_email
            EMAILS_STRS = ["open my email", "open my emails",
                           "open email", "open emails"]
            for phrase in EMAILS_STRS:
                if phrase in text:
                    choose_email()
                    subprocess.call(sys.executable + ' "' +
                                    os.path.realpath(__file__) + '"')

                # restart python script
            RESTART_CODE_STRS = ["restart"]
            if phrase in RESTART_CODE_STRS:
                if phrase in text:
                    speak("okay, rebooting")
                    subprocess.call(sys.executable + ' "' +
                                    os.path.realpath(__file__) + '"')

                # power module
            from power import shutDown
            # shuts down
            SHUTDOWN_STRS = ["shut down the computer"]
            for phrase in SHUTDOWN_STRS:
                if phrase in text:
                    shutDown()
                    subprocess.call(sys.executable + ' "' +
                                    os.path.realpath(__file__) + '"')

                # sleeps pc
            from power import sleep
            SLEEP_STRS = ["sleep the computer"]
            for phrase in SLEEP_STRS:
                if phrase in text:
                    sleep()
                    subprocess.call(sys.executable + ' "' +
                                    os.path.realpath(__file__) + '"')

                # locks and switch of monitor
            from power import lockMonitor
            LOCK_MONITOR_STRS = ["turn off monitor", "lock monitor"]
            for phrase in LOCK_MONITOR_STRS:
                if phrase in text:
                    lockMonitor()
                    subprocess.call(sys.executable + ' "' +
                                    os.path.realpath(__file__) + '"')

                # restarts pc
            from power import restart
            RESTART_STRS = ["restart the computer"]
            for phrase in RESTART_STRS:
                if phrase in text:
                    restart()
                    subprocess.call(sys.executable + ' "' +
                                    os.path.realpath(__file__) + '"')

                    # wolfram
            # from wolfram_words import wolfram_trigger
            from wolfram import wolfram
            from wolfram_words import wolfram_trigger
            WOLFRAM_STRS = wolfram_trigger
            for phrase in WOLFRAM_STRS:
                if phrase in text:
                    wolfram(text)
                    subprocess.call(sys.executable + ' "' +
                                    os.path.realpath(__file__) + '"')
            EMPTY_STRS = [""]
            if phrase in EMPTY_STRS:
                if phrase in text:
                    pass

    except Exception as e:
        speak("sorry sir, there was an error. please try again")
        print("Exception: " + str(e))
