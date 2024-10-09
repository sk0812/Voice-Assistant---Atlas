# imports required modules and functions
import requests
from speak import speak
import datetime
import geocoder

g = geocoder.ip('me')
lat = g.lat
lon = g.lng

if lat == 55.9561:
    if lon == -2.7833:
        town = "northwood"
else:
    town = g.city    

# openweather json site
url = f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&appid=24e4c072bb37a84df61ecc02544cdd99"
json_data = requests.get(url).json()

current_time = datetime.datetime.now()
day = (current_time.strftime("%A"))

# current weather


def current_weather():
    try:
        temp = json_data["current"]["temp"]
        temp = round(temp)
        temp = (temp - 273)
        temp = str(temp)

        description = json_data["current"]["weather"][0]["main"]

        if description == "Clouds":
            description = "cloudy skies"
        print(f"{temp} degrees")

        speak(
            f"currently in {town} it is {temp} degrees with {description}")

        min_temp = json_data["daily"][0]["temp"]["min"]
        max_temp = json_data["daily"][0]["temp"]["max"]

        min_temp = (min_temp - 273)
        max_temp = (max_temp - 273)

        min_temp = round(min_temp)
        max_temp = round(max_temp)

        max_temp = str(max_temp)
        min_temp = str(min_temp)

        description = json_data["daily"][0]["weather"][0]["description"]
        main = json_data["daily"][0]["weather"][0]["main"]

        if main == "Rain":
            misc = " Don't forget to carry an umbrella just incase"
        else:
            misc = ""

        if description == "clear":
            description = "sunny weather"

        if description == "scattered clouds":
            description = "partly sunny weather"

        print(min_temp, max_temp)
        speak(
            f"today's forecast you can expect {description} with a high of {max_temp} degrees and a low of {min_temp}")
        speak(misc)
    except:
        speak("sorry sir, i was unable to get the current weather. please check your internet connection and try again")


def today_weather():
    try:
        min_temp = json_data["daily"][0]["temp"]["min"]
        max_temp = json_data["daily"][0]["temp"]["max"]

        min_temp = (min_temp - 273)
        max_temp = (max_temp - 273)

        min_temp = round(min_temp)
        max_temp = round(max_temp)

        max_temp = str(max_temp)
        min_temp = str(min_temp)

        description = json_data["daily"][0]["weather"][0]["description"]
        main = json_data["daily"][0]["weather"][0]["main"]

        if main == "Rain":
            misc = " Don't forget to carry an umbrella just incase"

        if description == "clear":
            description = "sunny weather"

        if description == "scattered clouds":
            description = "partly sunny weather"

        print(min_temp, max_temp)
        speak(
            f"today's forecast you can expect {description} with a high of {max_temp} degrees and a low of {min_temp}")
        speak(misc)
    except:
        speak("sorry sir, i was unable to get today's weather forecast. please check your internet connection and try again")


# speaks the weather for the next 7 days depending on what the current day is


def next_week_weather():
    try:
        if day == "Monday":

            # tuesday weather
            max_temp = json_data["daily"][1]["temp"]["max"]
            max_temp = (max_temp - 273)
            max_temp = round(max_temp)
            max_temp = str(max_temp)

            description = json_data["daily"][1]["weather"][0]["description"]
            print(max_temp)

            if description == "clear":
                description = "sunny weather"

            if description == "scattered clouds":
                description = "partly sunny weather"

            [print(description)]

            speak(f"heres the weather forecast in {town} for the next 7 days")
            speak("On tuesday")
            speak(f"{max_temp} degrees and {description}")

            # wednesday
            max_temp = json_data["daily"][2]["temp"]["max"]
            max_temp = (max_temp - 273)
            max_temp = round(max_temp)
            max_temp = str(max_temp)

            description = json_data["daily"][2]["weather"][0]["description"]
            print(max_temp)

            if description == "clear":
                description = "sunny weather"

            if description == "scattered clouds":
                description = "partly sunny weather"

            [print(description)]

            speak("On wednesday")
            speak(f"{max_temp} degrees and {description}")

            # thursday
            max_temp = json_data["daily"][3]["temp"]["max"]
            max_temp = (max_temp - 273)
            max_temp = round(max_temp)
            max_temp = str(max_temp)

            description = json_data["daily"][3]["weather"][0]["description"]
            print(max_temp)

            if description == "clear":
                description = "sunny weather"

            if description == "scattered clouds":
                description = "partly sunny weather"

            [print(description)]

            speak("On thursday")
            speak(f"{max_temp} degrees and {description}")

            # friday
            max_temp = json_data["daily"][4]["temp"]["max"]
            max_temp = (max_temp - 273)
            max_temp = round(max_temp)
            max_temp = str(max_temp)

            description = json_data["daily"][4]["weather"][0]["description"]
            print(max_temp)

            if description == "clear":
                description = "sunny weather"

            if description == "scattered clouds":
                description = "partly sunny weather"

            [print(description)]

            speak("On friday")
            speak(f"{max_temp} degrees and {description}")

            # saturday
            max_temp = json_data["daily"][5]["temp"]["max"]
            max_temp = (max_temp - 273)
            max_temp = round(max_temp)
            max_temp = str(max_temp)

            description = json_data["daily"][5]["weather"][0]["description"]
            print(max_temp)

            if description == "clear":
                description = "sunny weather"

            if description == "scattered clouds":
                description = "partly sunny weather"

            [print(description)]

            speak("On saturday")
            speak(f"{max_temp} degrees and {description}")

            # sunday
            max_temp = json_data["daily"][6]["temp"]["max"]
            max_temp = (max_temp - 273)
            max_temp = round(max_temp)
            max_temp = str(max_temp)

            description = json_data["daily"][6]["weather"][0]["description"]
            print(max_temp)

            if description == "clear":
                description = "sunny weather"

            if description == "scattered clouds":
                description = "partly sunny weather"

            [print(description)]

            speak("On sunday")
            speak(f"{max_temp} degrees and {description}")

            # monday
            max_temp = json_data["daily"][7]["temp"]["max"]
            max_temp = (max_temp - 273)
            max_temp = round(max_temp)
            max_temp = str(max_temp)

            description = json_data["daily"][7]["weather"][0]["description"]
            print(max_temp)

            if description == "clear":
                description = "sunny weather"

            if description == "scattered clouds":
                description = "partly sunny weather"

            [print(description)]

            speak("On monday")
            speak(f"{max_temp} degrees and {description}")

        if day == "Tuesday":

            # Wednesday weather
            max_temp = json_data["daily"][1]["temp"]["max"]
            max_temp = (max_temp - 273)
            max_temp = round(max_temp)
            max_temp = str(max_temp)

            description = json_data["daily"][1]["weather"][0]["description"]
            print(max_temp)

            if description == "clear":
                description = "sunny weather"

            if description == "scattered clouds":
                description = "partly sunny weather"

            [print(description)]

            speak(f"heres the weather forecast in {town} for the next 7 days")
            speak("On wednesday")
            speak(f"{max_temp} degrees and {description}")

            # Thursday
            max_temp = json_data["daily"][2]["temp"]["max"]
            max_temp = (max_temp - 273)
            max_temp = round(max_temp)
            max_temp = str(max_temp)

            description = json_data["daily"][2]["weather"][0]["description"]
            print(max_temp)

            if description == "clear":
                description = "sunny weather"

            if description == "scattered clouds":
                description = "partly sunny weather"
            [print(description)]

            speak("On thursday")
            speak(f"{max_temp} degrees and {description}")

            # friday
            max_temp = json_data["daily"][3]["temp"]["max"]
            max_temp = (max_temp - 273)
            max_temp = round(max_temp)
            max_temp = str(max_temp)

            description = json_data["daily"][3]["weather"][0]["description"]
            print(max_temp)

            if description == "clear":
                description = "sunny weather"

            if description == "scattered clouds":
                description = "partly sunny weather"
            [print(description)]

            speak("On Friday")
            speak(f"{max_temp} degrees and {description}")

            # saturday
            max_temp = json_data["daily"][4]["temp"]["max"]
            max_temp = (max_temp - 273)
            max_temp = round(max_temp)
            max_temp = str(max_temp)

            description = json_data["daily"][4]["weather"][0]["description"]
            print(max_temp)

            if description == "clear":
                description = "sunny weather"

            if description == "scattered clouds":
                description = "partly sunny weather"
            [print(description)]

            speak("On Saturday")
            speak(f"{max_temp} degrees and {description}")

            # Sunday
            max_temp = json_data["daily"][5]["temp"]["max"]
            max_temp = (max_temp - 273)
            max_temp = round(max_temp)
            max_temp = str(max_temp)

            description = json_data["daily"][5]["weather"][0]["description"]
            print(max_temp)

            if description == "clear":
                description = "sunny weather"

            if description == "scattered clouds":
                description = "partly sunny weather"
            [print(description)]

            speak("On Sunday")
            speak(f"{max_temp} degrees and {description}")

            # Monday
            max_temp = json_data["daily"][6]["temp"]["max"]
            max_temp = (max_temp - 273)
            max_temp = round(max_temp)
            max_temp = str(max_temp)

            description = json_data["daily"][6]["weather"][0]["description"]
            print(max_temp)

            if description == "clear":
                description = "sunny weather"

            if description == "scattered clouds":
                description = "partly sunny weather"
            [print(description)]

            speak("On Monday")
            speak(f"{max_temp} degrees and {description}")

            # Tuesday
            max_temp = json_data["daily"][7]["temp"]["max"]
            max_temp = (max_temp - 273)
            max_temp = round(max_temp)
            max_temp = str(max_temp)

            description = json_data["daily"][7]["weather"][0]["description"]
            print(max_temp)

            if description == "clear":
                description = "sunny weather"

            if description == "scattered clouds":
                description = "partly sunny weather"
            [print(description)]

            speak("On Tuesday")
            speak(f"{max_temp} degrees and {description}")

        if day == "Wednesday":
            # thursday weather
            max_temp = json_data["daily"][1]["temp"]["max"]
            max_temp = (max_temp - 273)
            max_temp = round(max_temp)
            max_temp = str(max_temp)

            description = json_data["daily"][1]["weather"][0]["description"]
            print(max_temp)

            if description == "clear":
                description = "sunny weather"

            if description == "scattered clouds":
                description = "partly sunny weather"
            [print(description)]

            speak(f"heres the weather forecast in {town} for the next 7 days")
            speak("On thursday")
            speak(f"{max_temp} degrees and {description}")

            # Friday
            max_temp = json_data["daily"][2]["temp"]["max"]
            max_temp = (max_temp - 273)
            max_temp = round(max_temp)
            max_temp = str(max_temp)

            description = json_data["daily"][2]["weather"][0]["description"]
            print(max_temp)

            if description == "clear":
                description = "sunny weather"

            if description == "scattered clouds":
                description = "partly sunny weather"
            [print(description)]

            speak("On Friday")
            speak(f"{max_temp} degrees and {description}")

            # saturday
            max_temp = json_data["daily"][3]["temp"]["max"]
            max_temp = (max_temp - 273)
            max_temp = round(max_temp)
            max_temp = str(max_temp)

            description = json_data["daily"][3]["weather"][0]["description"]
            print(max_temp)

            if description == "clear":
                description = "sunny weather"

            if description == "scattered clouds":
                description = "partly sunny weather"
            [print(description)]

            speak("On saturday")
            speak(f"{max_temp} degrees and {description}")

            # sunday
            max_temp = json_data["daily"][4]["temp"]["max"]
            max_temp = (max_temp - 273)
            max_temp = round(max_temp)
            max_temp = str(max_temp)

            description = json_data["daily"][4]["weather"][0]["description"]
            print(max_temp)
            [print(description)]

            if description == "clear":
                description = "sunny weather"

            if description == "scattered clouds":
                description = "partly sunny weather"

            speak("On sunday")
            speak(f"{max_temp} degrees and {description}")

            # monday
            max_temp = json_data["daily"][5]["temp"]["max"]
            max_temp = (max_temp - 273)
            max_temp = round(max_temp)
            max_temp = str(max_temp)

            description = json_data["daily"][5]["weather"][0]["description"]
            print(max_temp)

            if description == "clear":
                description = "sunny weather"

            if description == "scattered clouds":
                description = "partly sunny weather"
            [print(description)]

            speak("On monday")
            speak(f"{max_temp} degrees and {description}")

            # tuesday
            max_temp = json_data["daily"][6]["temp"]["max"]
            max_temp = (max_temp - 273)
            max_temp = round(max_temp)
            max_temp = str(max_temp)

            description = json_data["daily"][6]["weather"][0]["description"]
            print(max_temp)

            if description == "clear":
                description = "sunny weather"

            if description == "scattered clouds":
                description = "partly sunny weather"
            [print(description)]

            speak("On tuesday")
            speak(f"{max_temp} degrees and {description}")

            # wednesday
            max_temp = json_data["daily"][7]["temp"]["max"]
            max_temp = (max_temp - 273)
            max_temp = round(max_temp)
            max_temp = str(max_temp)

            description = json_data["daily"][7]["weather"][0]["description"]
            print(max_temp)

            if description == "clear":
                description = "sunny weather"

            if description == "scattered clouds":
                description = "partly sunny weather"
            [print(description)]

            speak("On wednesday")
            speak(f"{max_temp} degrees and {description}")

        if day == "Thursday":

            # friday weather
            max_temp = json_data["daily"][1]["temp"]["max"]
            max_temp = (max_temp - 273)
            max_temp = round(max_temp)
            max_temp = str(max_temp)

            description = json_data["daily"][1]["weather"][0]["description"]
            print(max_temp)

            if description == "clear":
                description = "sunny weather"

            if description == "scattered clouds":
                description = "partly sunny weather"
            [print(description)]

            speak(f"heres the weather forecast in {town} for the next 7 days")
            speak("On friday")
            speak(f"{max_temp} degrees and {description}")

            # saturday
            max_temp = json_data["daily"][2]["temp"]["max"]
            max_temp = (max_temp - 273)
            max_temp = round(max_temp)
            max_temp = str(max_temp)

            description = json_data["daily"][2]["weather"][0]["description"]
            print(max_temp)

            if description == "clear":
                description = "sunny weather"

            if description == "scattered clouds":
                description = "partly sunny weather"
            [print(description)]

            speak("On saturday")
            speak(f"{max_temp} degrees and {description}")

            # sunday
            max_temp = json_data["daily"][3]["temp"]["max"]
            max_temp = (max_temp - 273)
            max_temp = round(max_temp)
            max_temp = str(max_temp)

            description = json_data["daily"][3]["weather"][0]["description"]
            print(max_temp)

            if description == "clear":
                description = "sunny weather"

            if description == "scattered clouds":
                description = "partly sunny weather"
            [print(description)]

            speak("On sunday")
            speak(f"{max_temp} degrees and {description}")

            # monday
            max_temp = json_data["daily"][4]["temp"]["max"]
            max_temp = (max_temp - 273)
            max_temp = round(max_temp)
            max_temp = str(max_temp)

            description = json_data["daily"][4]["weather"][0]["description"]
            print(max_temp)

            if description == "clear":
                description = "sunny weather"

            if description == "scattered clouds":
                description = "partly sunny weather"
            [print(description)]

            speak("On monday")
            speak(f"{max_temp} degrees and {description}")

            # tuesday
            max_temp = json_data["daily"][5]["temp"]["max"]
            max_temp = (max_temp - 273)
            max_temp = round(max_temp)
            max_temp = str(max_temp)

            description = json_data["daily"][5]["weather"][0]["description"]
            print(max_temp)

            if description == "clear":
                description = "sunny weather"

            if description == "scattered clouds":
                description = "partly sunny weather"
            [print(description)]

            speak("On tuesday")
            speak(f"{max_temp} degrees and {description}")

            # wednesday
            max_temp = json_data["daily"][6]["temp"]["max"]
            max_temp = (max_temp - 273)
            max_temp = round(max_temp)
            max_temp = str(max_temp)

            description = json_data["daily"][6]["weather"][0]["description"]
            print(max_temp)

            if description == "clear":
                description = "sunny weather"

            if description == "scattered clouds":
                description = "partly sunny weather"
            [print(description)]

            speak("On wednesday")
            speak(f"{max_temp} degrees and {description}")

            # thursday
            max_temp = json_data["daily"][7]["temp"]["max"]
            max_temp = (max_temp - 273)
            max_temp = round(max_temp)
            max_temp = str(max_temp)

            description = json_data["daily"][7]["weather"][0]["description"]
            print(max_temp)

            if description == "clear":
                description = "sunny weather"

            if description == "scattered clouds":
                description = "partly sunny weather"
            [print(description)]

            speak("On thursday")
            speak(f"{max_temp} degrees and {description}")

        if day == "Friday":

            # saturday weather
            max_temp = json_data["daily"][1]["temp"]["max"]
            max_temp = (max_temp - 273)
            max_temp = round(max_temp)
            max_temp = str(max_temp)

            description = json_data["daily"][1]["weather"][0]["description"]
            print(max_temp)

            if description == "clear":
                description = "sunny weather"

            if description == "scattered clouds":
                description = "partly sunny weather"
            [print(description)]

            speak(f"heres the weather forecast in {town} for the next 7 days")
            speak("On saturday")
            speak(f"{max_temp} degrees and {description}")

            # sun
            max_temp = json_data["daily"][2]["temp"]["max"]
            max_temp = (max_temp - 273)
            max_temp = round(max_temp)
            max_temp = str(max_temp)

            description = json_data["daily"][2]["weather"][0]["description"]
            print(max_temp)

            if description == "clear":
                description = "sunny weather"

            if description == "scattered clouds":
                description = "partly sunny weather"
            [print(description)]

            speak("On sunday")
            speak(f"{max_temp} degrees and {description}")

            # mon
            max_temp = json_data["daily"][3]["temp"]["max"]
            max_temp = (max_temp - 273)
            max_temp = round(max_temp)
            max_temp = str(max_temp)

            description = json_data["daily"][3]["weather"][0]["description"]
            print(max_temp)

            if description == "clear":
                description = "sunny weather"

            if description == "scattered clouds":
                description = "partly sunny weather"
            [print(description)]

            speak("On monday")
            speak(f"{max_temp} degrees and {description}")

            # tues
            max_temp = json_data["daily"][4]["temp"]["max"]
            max_temp = (max_temp - 273)
            max_temp = round(max_temp)
            max_temp = str(max_temp)

            description = json_data["daily"][4]["weather"][0]["description"]
            print(max_temp)

            if description == "clear":
                description = "sunny weather"

            if description == "scattered clouds":
                description = "partly sunny weather"
            [print(description)]

            speak("On tuesday")
            speak(f"{max_temp} degrees and {description}")

            # wednesday
            max_temp = json_data["daily"][5]["temp"]["max"]
            max_temp = (max_temp - 273)
            max_temp = round(max_temp)
            max_temp = str(max_temp)

            description = json_data["daily"][5]["weather"][0]["description"]
            print(max_temp)

            if description == "clear":
                description = "sunny weather"

            if description == "scattered clouds":
                description = "partly sunny weather"
            [print(description)]

            speak("On wednesday")
            speak(f"{max_temp} degrees and {description}")

            # thurs
            max_temp = json_data["daily"][6]["temp"]["max"]
            max_temp = (max_temp - 273)
            max_temp = round(max_temp)
            max_temp = str(max_temp)

            description = json_data["daily"][6]["weather"][0]["description"]
            print(max_temp)

            if description == "clear":
                description = "sunny weather"

            if description == "scattered clouds":
                description = "partly sunny weather"
            [print(description)]

            speak("On thursday")
            speak(f"{max_temp} degrees and {description}")

            # fri
            max_temp = json_data["daily"][7]["temp"]["max"]
            max_temp = (max_temp - 273)
            max_temp = round(max_temp)
            max_temp = str(max_temp)

            description = json_data["daily"][7]["weather"][0]["description"]
            print(max_temp)

            if description == "clear":
                description = "sunny weather"

            if description == "scattered clouds":
                description = "partly sunny weather"
            [print(description)]

            speak("On friday")
            speak(f"{max_temp} degrees and {description}")

        if day == "Saturday":

            # sunday weather
            max_temp = json_data["daily"][1]["temp"]["max"]
            max_temp = (max_temp - 273)
            max_temp = round(max_temp)
            max_temp = str(max_temp)

            description = json_data["daily"][1]["weather"][0]["description"]
            print(max_temp)

            if description == "clear":
                description = "sunny weather"

            if description == "scattered clouds":
                description = "partly sunny weather"
            [print(description)]

            speak(f"heres the weather forecast in {town} for the next 7 days")
            speak("On sunday")
            speak(f"{max_temp} degrees and {description}")

            # monday
            max_temp = json_data["daily"][2]["temp"]["max"]
            max_temp = (max_temp - 273)
            max_temp = round(max_temp)
            max_temp = str(max_temp)

            description = json_data["daily"][2]["weather"][0]["description"]
            print(max_temp)

            if description == "clear":
                description = "sunny weather"

            if description == "scattered clouds":
                description = "partly sunny weather"
            [print(description)]

            speak("On monday")
            speak(f"{max_temp} degrees and {description}")

            # tuesday
            max_temp = json_data["daily"][3]["temp"]["max"]
            max_temp = (max_temp - 273)
            max_temp = round(max_temp)
            max_temp = str(max_temp)

            description = json_data["daily"][3]["weather"][0]["description"]
            print(max_temp)

            if description == "clear":
                description = "sunny weather"

            if description == "scattered clouds":
                description = "partly sunny weather"
            [print(description)]

            speak("On tuesday")
            speak(f"{max_temp} degrees and {description}")

            # wed
            max_temp = json_data["daily"][4]["temp"]["max"]
            max_temp = (max_temp - 273)
            max_temp = round(max_temp)
            max_temp = str(max_temp)

            description = json_data["daily"][4]["weather"][0]["description"]
            print(max_temp)

            if description == "clear":
                description = "sunny weather"

            if description == "scattered clouds":
                description = "partly sunny weather"
            [print(description)]

            speak("On wednesday")
            speak(f"{max_temp} degrees and {description}")

            # thurs
            max_temp = json_data["daily"][5]["temp"]["max"]
            max_temp = (max_temp - 273)
            max_temp = round(max_temp)
            max_temp = str(max_temp)

            description = json_data["daily"][5]["weather"][0]["description"]
            print(max_temp)

            if description == "clear":
                description = "sunny weather"

            if description == "scattered clouds":
                description = "partly sunny weather"
            [print(description)]

            speak("On thursday")
            speak(f"{max_temp} degrees and {description}")

            # fri
            max_temp = json_data["daily"][6]["temp"]["max"]
            max_temp = (max_temp - 273)
            max_temp = round(max_temp)
            max_temp = str(max_temp)

            description = json_data["daily"][6]["weather"][0]["description"]
            print(max_temp)

            if description == "clear":
                description = "sunny weather"

            if description == "scattered clouds":
                description = "partly sunny weather"
            [print(description)]

            speak("On friday")
            speak(f"{max_temp} degrees and {description}")

            # sat
            max_temp = json_data["daily"][7]["temp"]["max"]
            max_temp = (max_temp - 273)
            max_temp = round(max_temp)
            max_temp = str(max_temp)

            description = json_data["daily"][7]["weather"][0]["description"]
            print(max_temp)

            if description == "clear":
                description = "sunny weather"

            if description == "scattered clouds":
                description = "partly sunny weather"
            [print(description)]

            speak("On saturday")
            speak(f"{max_temp} degrees and {description}")

        if day == "Sunday":

            # monday weather
            max_temp = json_data["daily"][1]["temp"]["max"]
            max_temp = (max_temp - 273)
            max_temp = round(max_temp)
            max_temp = str(max_temp)

            description = json_data["daily"][1]["weather"][0]["description"]
            print(max_temp)

            if description == "clear":
                description = "sunny weather"

            if description == "scattered clouds":
                description = "partly sunny weather"
            [print(description)]

            speak(f"heres the weather forecast in {town} for the next 7 days")
            speak("On monday")
            speak(f"{max_temp} degrees and {description}")

            # tuesday
            max_temp = json_data["daily"][2]["temp"]["max"]
            max_temp = (max_temp - 273)
            max_temp = round(max_temp)
            max_temp = str(max_temp)

            description = json_data["daily"][2]["weather"][0]["description"]
            print(max_temp)

            if description == "clear":
                description = "sunny weather"

            if description == "scattered clouds":
                description = "partly sunny weather"
            [print(description)]

            speak("On tuesday")
            speak(f"{max_temp} degrees and {description}")

            # wed
            max_temp = json_data["daily"][3]["temp"]["max"]
            max_temp = (max_temp - 273)
            max_temp = round(max_temp)
            max_temp = str(max_temp)

            description = json_data["daily"][3]["weather"][0]["description"]
            print(max_temp)

            if description == "clear":
                description = "sunny weather"

            if description == "scattered clouds":
                description = "partly sunny weather"
            [print(description)]

            speak("On wednesday")
            speak(f"{max_temp} degrees and {description}")

            # thurs
            max_temp = json_data["daily"][4]["temp"]["max"]
            max_temp = (max_temp - 273)
            max_temp = round(max_temp)
            max_temp = str(max_temp)

            description = json_data["daily"][4]["weather"][0]["description"]
            print(max_temp)

            if description == "clear":
                description = "sunny weather"

            if description == "scattered clouds":
                description = "partly sunny weather"
            [print(description)]

            speak("On thursday")
            speak(f"{max_temp} degrees and {description}")

            # fri
            max_temp = json_data["daily"][5]["temp"]["max"]
            max_temp = (max_temp - 273)
            max_temp = round(max_temp)
            max_temp = str(max_temp)

            description = json_data["daily"][5]["weather"][0]["description"]
            print(max_temp)

            if description == "clear":
                description = "sunny weather"

            if description == "scattered clouds":
                description = "partly sunny weather"
            [print(description)]

            speak("On friday")
            speak(f"{max_temp} degrees and {description}")

            # sat
            max_temp = json_data["daily"][6]["temp"]["max"]
            max_temp = (max_temp - 273)
            max_temp = round(max_temp)
            max_temp = str(max_temp)

            description = json_data["daily"][6]["weather"][0]["description"]
            print(max_temp)

            if description == "clear":
                description = "sunny weather"

            if description == "scattered clouds":
                description = "partly sunny weather"
            [print(description)]

            speak("On saturday")
            speak(f"{max_temp} degrees and {description}")

            # sun
            max_temp = json_data["daily"][7]["temp"]["max"]
            max_temp = (max_temp - 273)
            max_temp = round(max_temp)
            max_temp = str(max_temp)

            description = json_data["daily"][7]["weather"][0]["description"]
            print(max_temp)

            if description == "clear":
                description = "sunny weather"

            if description == "scattered clouds":
                description = "partly sunny weather"
            [print(description)]

            speak("On sunday")
            speak(f"{max_temp} degrees and {description}")
    except:
        speak("sorry sir, i was unable to get the weather forecast for the next 7 days. please check your internet connection and try again")
        # weather tomorrow


def tom_weather():
    try:
        max_temp = json_data["daily"][1]["temp"]["max"]
        min_temp = json_data["daily"][1]["temp"]["min"]

        max_temp = (max_temp - 273)
        min_temp = (min_temp - 273)

        max_temp = round(max_temp)
        min_temp = round(min_temp)

        max_temp = str(max_temp)
        min_temp = str(min_temp)

        description = json_data["daily"][1]["weather"][0]["description"]
        if description == "clear":
            description = "sunny weather"

        if description == "scattered clouds":
            description = "partly sunny weather"
        print(description)
        print(min_temp)
        print(max_temp)

        speak(
            f"tomorrow in {town} you can expect {description} with a high of {max_temp} degrees celsius and a low of {min_temp} degrees")
    except:
        speak("sorry sir, i was unable to get the weather forecast for tomorrow. please check your internet connection and try again")
    # weekend weather


def weekend_weather():
    try:
        print(day)
        if day == "Monday":
            max_temp = json_data["daily"][6]["temp"]["max"]
            max_temp = (max_temp - 273)
            max_temp = round(max_temp)
            max_temp = str(max_temp)

            description = json_data["daily"][6]["weather"][0]["description"]
            print("saturday", description, max_temp)
            speak(
                f"on saturday you can expect {description} with a high of {max_temp} degrees celsius.")

            max_temp = json_data["daily"][7]["temp"]["max"]
            max_temp = (max_temp - 273)
            max_temp = round(max_temp)
            max_temp = str(max_temp)

            description = json_data["daily"][6]["weather"][0]["description"]
            print("sunday", description, max_temp)
            speak(
                f"on Sunday you can expect {description} with a high of {max_temp} degrees.")

        if day == "Tuesday":
            max_temp = json_data["daily"][5]["temp"]["max"]
            max_temp = (max_temp - 273)
            max_temp = round(max_temp)
            max_temp = str(max_temp)

            description = json_data["daily"][5]["weather"][0]["description"]
            print("saturday", description, max_temp)
            speak(
                f"on Sunday you can expect {description} with a high of {max_temp} degrees.")

            max_temp = json_data["daily"][6]["temp"]["max"]
            max_temp = (max_temp - 273)
            max_temp = round(max_temp)
            max_temp = str(max_temp)

            description = json_data["daily"][6]["weather"][0]["description"]
            print("sunday", description, max_temp)
            speak(
                f"on Saturday you can expect {description} with a high of {max_temp} degrees.")

        if day == "Tuesday":
            max_temp = json_data["daily"][4]["temp"]["max"]
            max_temp = (max_temp - 273)
            max_temp = round(max_temp)
            max_temp = str(max_temp)

            description = json_data["daily"][4]["weather"][0]["description"]
            print("saturday", description, max_temp)
            speak(
                f"on Saturday you can expect {description} with a high of {max_temp} degrees celsius.")

            max_temp = json_data["daily"][5]["temp"]["max"]
            max_temp = (max_temp - 273)
            max_temp = round(max_temp)
            max_temp = str(max_temp)

            description = json_data["daily"][5]["weather"][0]["description"]
            print("sunday", description, max_temp)
            speak(
                f"on sunday you can expect {description} with a high of {max_temp} degrees")

        if day == "Wednesday":
            max_temp = json_data["daily"][3]["temp"]["max"]
            max_temp = (max_temp - 273)
            max_temp = round(max_temp)
            max_temp = str(max_temp)

            description = json_data["daily"][3]["weather"][0]["description"]
            print("saturday", description, max_temp)
            speak(
                f"on Saturday you can expect {description} with a high of {max_temp} degrees celsius.")

            max_temp = json_data["daily"][4]["temp"]["max"]
            max_temp = (max_temp - 273)
            max_temp = round(max_temp)
            max_temp = str(max_temp)

            description = json_data["daily"][4]["weather"][0]["description"]
            print("sunday", description, max_temp)
            speak(
                f"on Sunday you can expect {description} with a high of {max_temp} degrees.")

        if day == "Thursday":
            max_temp = json_data["daily"][2]["temp"]["max"]
            max_temp = (max_temp - 273)
            max_temp = round(max_temp)
            max_temp = str(max_temp)

            description = json_data["daily"][2]["weather"][0]["description"]
            print("saturday", description, max_temp)
            speak(
                f"on Saturday you can expect {description} with a high of {max_temp} degrees celsius.")

            max_temp = json_data["daily"][3]["temp"]["max"]
            max_temp = (max_temp - 273)
            max_temp = round(max_temp)
            max_temp = str(max_temp)

            description = json_data["daily"][3]["weather"][0]["description"]
            print("sunday", description, max_temp)
            speak(
                f"on Sunday you can expect {description} with a high of {max_temp} degrees.")

        if day == "Friday":
            max_temp = json_data["daily"][1]["temp"]["max"]
            max_temp = (max_temp - 273)
            max_temp = round(max_temp)
            max_temp = str(max_temp)

            description = json_data["daily"][1]["weather"][0]["description"]
            print("saturday", description, max_temp)
            speak(
                f"on Saturday you can expect {description} with a high of {max_temp} degrees celsius.")

            max_temp = json_data["daily"][2]["temp"]["max"]
            max_temp = (max_temp - 273)
            max_temp = round(max_temp)
            max_temp = str(max_temp)

            description = json_data["daily"][2]["weather"][0]["description"]
            print("sunday", description, max_temp)
            speak(
                f"on Sunday you can expect {description} with a high of {max_temp} degrees.")

        if day == "saturday":
            max_temp = json_data["daily"][0]["temp"]["max"]
            max_temp = (max_temp - 273)
            max_temp = round(max_temp)
            max_temp = str(max_temp)

            description = json_data["daily"][0]["weather"][0]["description"]
            print("today", description, max_temp)
            speak(
                f"today you can expect {description} with a high of {max_temp} degrees celsius")

            max_temp = json_data["daily"][1]["temp"]["max"]
            max_temp = (max_temp - 273)
            max_temp = round(max_temp)
            max_temp = str(max_temp)

            description = json_data["daily"][1]["weather"][0]["description"]
            print("tomorrow", description, max_temp)
            speak(
                f"tomorrow you can expect {description} with a high of {max_temp} degrees")

        if day == "Sunday":
            max_temp = json_data["daily"][7]["temp"]["max"]
            max_temp = (max_temp - 273)
            max_temp = round(max_temp)
            max_temp = str(max_temp)

            description = json_data["daily"][7]["weather"][0]["description"]
            print("saturday", description, max_temp)
            speak(
                f"Saturday you can expect {description} with a high of {max_temp} degrees celsius")

            max_temp = json_data["daily"][8]["temp"]["max"]
            max_temp = (max_temp - 273)
            max_temp = round(max_temp)
            max_temp = str(max_temp)

            description = json_data["daily"][8]["weather"][0]["description"]
            print("sunday", description, max_temp)
            speak(
                f"on Sunday you can expect {description} with a high of {max_temp} degrees")
    except:
        speak("sorry sir, i was unable to get the weather forecast for the weekend. please check your internet connection and try again")


# weather for each indivual day
# weather for each indivual day


def monday_weather():
    try:
        # day monday
        if day == "Monday":

            max_temp = json_data["daily"][7]["temp"]["max"]
            max_temp = (max_temp - 273)
            max_temp = round(max_temp)
            max_temp = str(max_temp)

            description = json_data["daily"][7]["weather"][0]["description"]
            print(max_temp)

            if description == "clear":
                description = "sunny weather"

            if description == "scattered clouds":
                description = "partly sunny weather"

            [print(description)]

            speak(
                f"next Monday you can expect a high of {max_temp} degrees and {description}")

        if day == "Tuesday":

            max_temp = json_data["daily"][6]["temp"]["max"]
            max_temp = (max_temp - 273)
            max_temp = round(max_temp)
            max_temp = str(max_temp)

            description = json_data["daily"][6]["weather"][0]["description"]
            print(max_temp)

            if description == "clear":
                description = "sunny weather"

            if description == "scattered clouds":
                description = "partly sunny weather"

            [print(description)]

            speak(
                f"next Monday you can expect a high of {max_temp} degrees and {description}")

        if "day" == "Wednesday":

            max_temp = json_data["daily"][5]["temp"]["max"]
            max_temp = (max_temp - 273)
            max_temp = round(max_temp)
            max_temp = str(max_temp)

            description = json_data["daily"][5]["weather"][0]["description"]
            print(max_temp)

            if description == "clear":
                description = "sunny weather"

            if description == "scattered clouds":
                description = "partly sunny weather"

            [print(description)]

            speak(
                f"next Monday you can expect a high of {max_temp} degrees and {description}")

        if day == "Thursday":

            max_temp = json_data["daily"][4]["temp"]["max"]
            max_temp = (max_temp - 273)
            max_temp = round(max_temp)
            max_temp = str(max_temp)

            description = json_data["daily"][4]["weather"][0]["description"]
            print(max_temp)

            if description == "clear":
                description = "sunny weather"

            if description == "scattered clouds":
                description = "partly sunny weather"

            [print(description)]

            speak(
                f"next Monday you can expect a high of {max_temp} degrees and {description}")

        if day == "Friday":

            max_temp = json_data["daily"][3]["temp"]["max"]
            max_temp = (max_temp - 273)
            max_temp = round(max_temp)
            max_temp = str(max_temp)

            description = json_data["daily"][3]["weather"][0]["description"]
            print(max_temp)

            if description == "clear":
                description = "sunny weather"

            if description == "scattered clouds":
                description = "partly sunny weather"

            [print(description)]

            speak(
                f"next Monday you can expect a high of {max_temp} degrees and {description}")

        if day == "Saturday":

            max_temp = json_data["daily"][2]["temp"]["max"]
            max_temp = (max_temp - 273)
            max_temp = round(max_temp)
            max_temp = str(max_temp)

            description = json_data["daily"][2]["weather"][0]["description"]
            print(max_temp)

            if description == "clear":
                description = "sunny weather"

            if description == "scattered clouds":
                description = "partly sunny weather"

            [print(description)]

            speak(
                f"next Monday you can expect a high of {max_temp} degrees and {description}")

        if day == "sunday":

            max_temp = json_data["daily"][1]["temp"]["max"]
            max_temp = (max_temp - 273)
            max_temp = round(max_temp)
            max_temp = str(max_temp)

            description = json_data["daily"][1]["weather"][0]["description"]
            print(max_temp)

            if description == "clear":
                description = "sunny weather"

            if description == "scattered clouds":
                description = "partly sunny weather"

            [print(description)]

            speak(
                f"next Monday you can expect a high of {max_temp} degrees and {description}")
    except:
        speak("sorry sir, i was unable to get the weather forecast for Monday. please check your internet connection and try again")


def tuesday_weather():
    try:
        # day monday
        if day == "Tuesday":

            max_temp = json_data["daily"][7]["temp"]["max"]
            max_temp = (max_temp - 273)
            max_temp = round(max_temp)
            max_temp = str(max_temp)

            description = json_data["daily"][7]["weather"][0]["description"]
            print(max_temp)

            if description == "clear":
                description = "sunny weather"

            if description == "scattered clouds":
                description = "partly sunny weather"

            [print(description)]

            speak(
                f"next tuesday you can expect a high of {max_temp} degrees and {description}")

        if day == "Wednesday":

            max_temp = json_data["daily"][6]["temp"]["max"]
            max_temp = (max_temp - 273)
            max_temp = round(max_temp)
            max_temp = str(max_temp)

            description = json_data["daily"][6]["weather"][0]["description"]
            print(max_temp)

            if description == "clear":
                description = "sunny weather"

            if description == "scattered clouds":
                description = "partly sunny weather"

            [print(description)]

            speak(
                f"next tuesday you can expect a high of {max_temp} degrees and {description}")

        if "day" == "Thursday":

            max_temp = json_data["daily"][5]["temp"]["max"]
            max_temp = (max_temp - 273)
            max_temp = round(max_temp)
            max_temp = str(max_temp)

            description = json_data["daily"][5]["weather"][0]["description"]
            print(max_temp)

            if description == "clear":
                description = "sunny weather"

            if description == "scattered clouds":
                description = "partly sunny weather"

            [print(description)]

            speak(
                f"next tuesday you can expect a high of {max_temp} degrees and {description}")

        if day == "Friday":

            max_temp = json_data["daily"][4]["temp"]["max"]
            max_temp = (max_temp - 273)
            max_temp = round(max_temp)
            max_temp = str(max_temp)

            description = json_data["daily"][4]["weather"][0]["description"]
            print(max_temp)

            if description == "clear":
                description = "sunny weather"

            if description == "scattered clouds":
                description = "partly sunny weather"

            [print(description)]

            speak(
                f"next tuesday you can expect a high of {max_temp} degrees and {description}")

        if day == "Saturday":

            max_temp = json_data["daily"][3]["temp"]["max"]
            max_temp = (max_temp - 273)
            max_temp = round(max_temp)
            max_temp = str(max_temp)

            description = json_data["daily"][3]["weather"][0]["description"]
            print(max_temp)

            if description == "clear":
                description = "sunny weather"

            if description == "scattered clouds":
                description = "partly sunny weather"

            [print(description)]

            speak(
                f"next tuesday you can expect a high of {max_temp} degrees and {description}")

        if day == "Sunday":

            max_temp = json_data["daily"][2]["temp"]["max"]
            max_temp = (max_temp - 273)
            max_temp = round(max_temp)
            max_temp = str(max_temp)

            description = json_data["daily"][2]["weather"][0]["description"]
            print(max_temp)

            if description == "clear":
                description = "sunny weather"

            if description == "scattered clouds":
                description = "partly sunny weather"

            [print(description)]

            speak(
                f"next tuseday you can expect a high of {max_temp} degrees and {description}")

        if day == "Monday":

            max_temp = json_data["daily"][1]["temp"]["max"]
            max_temp = (max_temp - 273)
            max_temp = round(max_temp)
            max_temp = str(max_temp)

            description = json_data["daily"][1]["weather"][0]["description"]
            print(max_temp)

            if description == "clear":
                description = "sunny weather"

            if description == "scattered clouds":
                description = "partly sunny weather"

            [print(description)]

            speak(
                f"tomorrow you can expect a high of {max_temp} degrees and {description}")
    except:
        speak("sorry sir, i was unable to get the weather forecast for Tuesday. please check your internet connection and try again")


def wednesday_weather():
    try:
        if day == "wednesday":

            max_temp = json_data["daily"][7]["temp"]["max"]
            max_temp = (max_temp - 273)
            max_temp = round(max_temp)
            max_temp = str(max_temp)

            description = json_data["daily"][7]["weather"][0]["description"]
            print(max_temp)

            if description == "clear":
                description = "sunny weather"

            if description == "scattered clouds":
                description = "partly sunny weather"

            [print(description)]

            speak(
                f"next wednesday you can expect a high of {max_temp} degrees and {description}")

        if day == "thursday":

            max_temp = json_data["daily"][6]["temp"]["max"]
            max_temp = (max_temp - 273)
            max_temp = round(max_temp)
            max_temp = str(max_temp)

            description = json_data["daily"][6]["weather"][0]["description"]
            print(max_temp)

            if description == "clear":
                description = "sunny weather"

            if description == "scattered clouds":
                description = "partly sunny weather"

            [print(description)]

            speak(
                f"next wednesday you can expect a high of {max_temp} degrees and {description}")

        if "day" == "Friday":

            max_temp = json_data["daily"][5]["temp"]["max"]
            max_temp = (max_temp - 273)
            max_temp = round(max_temp)
            max_temp = str(max_temp)

            description = json_data["daily"][5]["weather"][0]["description"]
            print(max_temp)

            if description == "clear":
                description = "sunny weather"

            if description == "scattered clouds":
                description = "partly sunny weather"

            [print(description)]

            speak(
                f"next wednesday you can expect a high of {max_temp} degrees and {description}")

        if day == "Saturday":

            max_temp = json_data["daily"][4]["temp"]["max"]
            max_temp = (max_temp - 273)
            max_temp = round(max_temp)
            max_temp = str(max_temp)

            description = json_data["daily"][4]["weather"][0]["description"]
            print(max_temp)

            if description == "clear":
                description = "sunny weather"

            if description == "scattered clouds":
                description = "partly sunny weather"

            [print(description)]

            speak(
                f"next wednesday you can expect a high of {max_temp} degrees and {description}")

        if day == "Sunday":

            max_temp = json_data["daily"][3]["temp"]["max"]
            max_temp = (max_temp - 273)
            max_temp = round(max_temp)
            max_temp = str(max_temp)

            description = json_data["daily"][3]["weather"][0]["description"]
            print(max_temp)

            if description == "clear":
                description = "sunny weather"

            if description == "scattered clouds":
                description = "partly sunny weather"

            [print(description)]

            speak(
                f"next wednesday you can expect a high of {max_temp} degrees and {description}")

        if day == "Monday":

            max_temp = json_data["daily"][2]["temp"]["max"]
            max_temp = (max_temp - 273)
            max_temp = round(max_temp)
            max_temp = str(max_temp)

            description = json_data["daily"][2]["weather"][0]["description"]
            print(max_temp)

            if description == "clear":
                description = "sunny weather"

            if description == "scattered clouds":
                description = "partly sunny weather"

            [print(description)]

            speak(
                f"next wednesday you can expect a high of {max_temp} degrees and {description}")

        if day == "Tuseday":

            max_temp = json_data["daily"][1]["temp"]["max"]
            max_temp = (max_temp - 273)
            max_temp = round(max_temp)
            max_temp = str(max_temp)

            description = json_data["daily"][1]["weather"][0]["description"]
            print(max_temp)

            if description == "clear":
                description = "sunny weather"

            if description == "scattered clouds":
                description = "partly sunny weather"

            [print(description)]

            speak(
                f"next Tuesday you can expect a high of {max_temp} degrees and {description}")
    except:
        speak("sorry sir, i was unable to get the weather forecast for Wednesday. please check your internet connection and try again")


def thursday_weather():
    try:
        if day == "thursday":

            max_temp = json_data["daily"][7]["temp"]["max"]
            max_temp = (max_temp - 273)
            max_temp = round(max_temp)
            max_temp = str(max_temp)

            description = json_data["daily"][7]["weather"][0]["description"]
            print(max_temp)

            if description == "clear":
                description = "sunny weather"

            if description == "scattered clouds":
                description = "partly sunny weather"

            [print(description)]

            speak(
                f"next thursday you can expect a high of {max_temp} degrees and {description}")

        if day == "friday":

            max_temp = json_data["daily"][6]["temp"]["max"]
            max_temp = (max_temp - 273)
            max_temp = round(max_temp)
            max_temp = str(max_temp)

            description = json_data["daily"][6]["weather"][0]["description"]
            print(max_temp)

            if description == "clear":
                description = "sunny weather"

            if description == "scattered clouds":
                description = "partly sunny weather"

            [print(description)]

            speak(
                f"next thursday you can expect a high of {max_temp} degrees and {description}")

        if "day" == "saturday":

            max_temp = json_data["daily"][5]["temp"]["max"]
            max_temp = (max_temp - 273)
            max_temp = round(max_temp)
            max_temp = str(max_temp)

            description = json_data["daily"][5]["weather"][0]["description"]
            print(max_temp)

            if description == "clear":
                description = "sunny weather"

            if description == "scattered clouds":
                description = "partly sunny weather"

            [print(description)]

            speak(
                f"next thursday you can expect a high of {max_temp} degrees and {description}")

        if day == "sunday":

            max_temp = json_data["daily"][4]["temp"]["max"]
            max_temp = (max_temp - 273)
            max_temp = round(max_temp)
            max_temp = str(max_temp)

            description = json_data["daily"][4]["weather"][0]["description"]
            print(max_temp)

            if description == "clear":
                description = "sunny weather"

            if description == "scattered clouds":
                description = "partly sunny weather"

            [print(description)]

            speak(
                f"next thursday you can expect a high of {max_temp} degrees and {description}")

        if day == "monday":

            max_temp = json_data["daily"][3]["temp"]["max"]
            max_temp = (max_temp - 273)
            max_temp = round(max_temp)
            max_temp = str(max_temp)

            description = json_data["daily"][3]["weather"][0]["description"]
            print(max_temp)

            if description == "clear":
                description = "sunny weather"

            if description == "scattered clouds":
                description = "partly sunny weather"

            [print(description)]

            speak(
                f"next thursday you can expect a high of {max_temp} degrees and {description}")

        if day == "Tuesday":

            max_temp = json_data["daily"][2]["temp"]["max"]
            max_temp = (max_temp - 273)
            max_temp = round(max_temp)
            max_temp = str(max_temp)

            description = json_data["daily"][2]["weather"][0]["description"]
            print(max_temp)

            if description == "clear":
                description = "sunny weather"

            if description == "scattered clouds":
                description = "partly sunny weather"

            [print(description)]

            speak(
                f"next thursday you can expect a high of {max_temp} degrees and {description}")

        if day == "wednesday":

            max_temp = json_data["daily"][1]["temp"]["max"]
            max_temp = (max_temp - 273)
            max_temp = round(max_temp)
            max_temp = str(max_temp)

            description = json_data["daily"][1]["weather"][0]["description"]
            print(max_temp)

            if description == "clear":
                description = "sunny weather"

            if description == "scattered clouds":
                description = "partly sunny weather"

            [print(description)]

            speak(
                f"tomorrow you can expect a high of {max_temp} degrees and {description}")
    except:
        speak("sorry sir, i was unable to get the weather forecast for Thursday. please check your internet connection and try again")


def friday_weather():
    try:
        if day == "friday":

            max_temp = json_data["daily"][7]["temp"]["max"]
            max_temp = (max_temp - 273)
            max_temp = round(max_temp)
            max_temp = str(max_temp)

            description = json_data["daily"][7]["weather"][0]["description"]
            print(max_temp)

            if description == "clear":
                description = "sunny weather"

            if description == "scattered clouds":
                description = "partly sunny weather"

            [print(description)]

            speak(
                f"next friday you can expect a high of {max_temp} degrees and {description}")

        if day == "Saturday":

            max_temp = json_data["daily"][6]["temp"]["max"]
            max_temp = (max_temp - 273)
            max_temp = round(max_temp)
            max_temp = str(max_temp)

            description = json_data["daily"][6]["weather"][0]["description"]
            print(max_temp)

            if description == "clear":
                description = "sunny weather"

            if description == "scattered clouds":
                description = "partly sunny weather"

            [print(description)]

            speak(
                f"next friday you can expect a high of {max_temp} degrees and {description}")

        if "day" == "Sunday":

            max_temp = json_data["daily"][5]["temp"]["max"]
            max_temp = (max_temp - 273)
            max_temp = round(max_temp)
            max_temp = str(max_temp)

            description = json_data["daily"][5]["weather"][0]["description"]
            print(max_temp)

            if description == "clear":
                description = "sunny weather"

            if description == "scattered clouds":
                description = "partly sunny weather"

            [print(description)]

            speak(
                f"next friday you can expect a high of {max_temp} degrees and {description}")

        if day == "Monday":

            max_temp = json_data["daily"][4]["temp"]["max"]
            max_temp = (max_temp - 273)
            max_temp = round(max_temp)
            max_temp = str(max_temp)

            description = json_data["daily"][4]["weather"][0]["description"]
            print(max_temp)

            if description == "clear":
                description = "sunny weather"

            if description == "scattered clouds":
                description = "partly sunny weather"

            [print(description)]

            speak(
                f"next friday you can expect a high of {max_temp} degrees and {description}")

        if day == "Tuesday":

            max_temp = json_data["daily"][3]["temp"]["max"]
            max_temp = (max_temp - 273)
            max_temp = round(max_temp)
            max_temp = str(max_temp)

            description = json_data["daily"][3]["weather"][0]["description"]
            print(max_temp)

            if description == "clear":
                description = "sunny weather"

            if description == "scattered clouds":
                description = "partly sunny weather"

            [print(description)]

            speak(
                f"next friday you can expect a high of {max_temp} degrees and {description}")

        if day == "Wednesday":

            max_temp = json_data["daily"][2]["temp"]["max"]
            max_temp = (max_temp - 273)
            max_temp = round(max_temp)
            max_temp = str(max_temp)

            description = json_data["daily"][2]["weather"][0]["description"]
            print(max_temp)

            if description == "clear":
                description = "sunny weather"

            if description == "scattered clouds":
                description = "partly sunny weather"

            [print(description)]

            speak(
                f"next friday you can expect a high of {max_temp} degrees and {description}")

        if day == "Thursday":

            max_temp = json_data["daily"][1]["temp"]["max"]
            max_temp = (max_temp - 273)
            max_temp = round(max_temp)
            max_temp = str(max_temp)

            description = json_data["daily"][1]["weather"][0]["description"]
            print(max_temp)

            if description == "clear":
                description = "sunny weather"

            if description == "scattered clouds":
                description = "partly sunny weather"

            [print(description)]

            speak(
                f"tomorrow you can expect a high of {max_temp} degrees and {description}")
    except:
        speak("sorry sir, i was unable to get the weather forecast for Friday. please check your internet connection and try again")


def Saturday_weather():
    try:
        if day == "Saturday":

            max_temp = json_data["daily"][7]["temp"]["max"]
            max_temp = (max_temp - 273)
            max_temp = round(max_temp)
            max_temp = str(max_temp)

            description = json_data["daily"][7]["weather"][0]["description"]
            print(max_temp)

            if description == "clear":
                description = "sunny weather"

            if description == "scattered clouds":
                description = "partly sunny weather"

            [print(description)]

            speak(
                f"next saturday you can expect a high of {max_temp} degrees and {description}")

        if day == "Sunday":

            max_temp = json_data["daily"][6]["temp"]["max"]
            max_temp = (max_temp - 273)
            max_temp = round(max_temp)
            max_temp = str(max_temp)

            description = json_data["daily"][6]["weather"][0]["description"]
            print(max_temp)

            if description == "clear":
                description = "sunny weather"

            if description == "scattered clouds":
                description = "partly sunny weather"

            [print(description)]

            speak(
                f"next saturday you can expect a high of {max_temp} degrees and {description}")

        if "day" == "Monday":

            max_temp = json_data["daily"][5]["temp"]["max"]
            max_temp = (max_temp - 273)
            max_temp = round(max_temp)
            max_temp = str(max_temp)

            description = json_data["daily"][5]["weather"][0]["description"]
            print(max_temp)

            if description == "clear":
                description = "sunny weather"

            if description == "scattered clouds":
                description = "partly sunny weather"

            [print(description)]

            speak(
                f"next saturday you can expect a high of {max_temp} degrees and {description}")

        if day == "Tuesday":

            max_temp = json_data["daily"][4]["temp"]["max"]
            max_temp = (max_temp - 273)
            max_temp = round(max_temp)
            max_temp = str(max_temp)

            description = json_data["daily"][4]["weather"][0]["description"]
            print(max_temp)

            if description == "clear":
                description = "sunny weather"

            if description == "scattered clouds":
                description = "partly sunny weather"

            [print(description)]

            speak(
                f"next Saturday you can expect a high of {max_temp} degrees and {description}")

        if day == "Wednesday":

            max_temp = json_data["daily"][3]["temp"]["max"]
            max_temp = (max_temp - 273)
            max_temp = round(max_temp)
            max_temp = str(max_temp)

            description = json_data["daily"][3]["weather"][0]["description"]
            print(max_temp)

            if description == "clear":
                description = "sunny weather"

            if description == "scattered clouds":
                description = "partly sunny weather"

            [print(description)]

            speak(
                f"next saturday you can expect a high of {max_temp} degrees and {description}")

        if day == "Thursday":

            max_temp = json_data["daily"][2]["temp"]["max"]
            max_temp = (max_temp - 273)
            max_temp = round(max_temp)
            max_temp = str(max_temp)

            description = json_data["daily"][2]["weather"][0]["description"]
            print(max_temp)

            if description == "clear":
                description = "sunny weather"

            if description == "scattered clouds":
                description = "partly sunny weather"

            [print(description)]

            speak(
                f"next saturday you can expect a high of {max_temp} degrees and {description}")

        if day == "Friday":

            max_temp = json_data["daily"][1]["temp"]["max"]
            max_temp = (max_temp - 273)
            max_temp = round(max_temp)
            max_temp = str(max_temp)

            description = json_data["daily"][1]["weather"][0]["description"]
            print(max_temp)

            if description == "clear":
                description = "sunny weather"

            if description == "scattered clouds":
                description = "partly sunny weather"

            [print(description)]

            speak(
                f"tomorrow you can expect a high of {max_temp} degrees and {description}")
    except:
        speak("sorry sir, i was unable to get the weather forecast for Saturday. please check your internet connection and try again")


def sunday_weather():
    try:
        if day == "sunday":

            max_temp = json_data["daily"][7]["temp"]["max"]
            max_temp = (max_temp - 273)
            max_temp = round(max_temp)
            max_temp = str(max_temp)

            description = json_data["daily"][7]["weather"][0]["description"]
            print(max_temp)

            if description == "clear":
                description = "sunny weather"

            if description == "scattered clouds":
                description = "partly sunny weather"

            [print(description)]

            speak(
                f"next sunday you can expect a high of {max_temp} degrees and {description}")

        if day == "Monday":

            max_temp = json_data["daily"][6]["temp"]["max"]
            max_temp = (max_temp - 273)
            max_temp = round(max_temp)
            max_temp = str(max_temp)

            description = json_data["daily"][6]["weather"][0]["description"]
            print(max_temp)

            if description == "clear":
                description = "sunny weather"

            if description == "scattered clouds":
                description = "partly sunny weather"

            [print(description)]

            speak(
                f"next sunday you can expect a high of {max_temp} degrees and {description}")

        if "day" == "Tuesday":

            max_temp = json_data["daily"][5]["temp"]["max"]
            max_temp = (max_temp - 273)
            max_temp = round(max_temp)
            max_temp = str(max_temp)

            description = json_data["daily"][5]["weather"][0]["description"]
            print(max_temp)

            if description == "clear":
                description = "sunny weather"

            if description == "scattered clouds":
                description = "partly sunny weather"

            [print(description)]

            speak(
                f"next sunday you can expect a high of {max_temp} degrees and {description}")

        if day == "Wednesday":

            max_temp = json_data["daily"][4]["temp"]["max"]
            max_temp = (max_temp - 273)
            max_temp = round(max_temp)
            max_temp = str(max_temp)

            description = json_data["daily"][4]["weather"][0]["description"]
            print(max_temp)

            if description == "clear":
                description = "sunny weather"

            if description == "scattered clouds":
                description = "partly sunny weather"

            [print(description)]

            speak(
                f"next sunday you can expect a high of {max_temp} degrees and {description}")

        if day == "Thursday":

            max_temp = json_data["daily"][3]["temp"]["max"]
            max_temp = (max_temp - 273)
            max_temp = round(max_temp)
            max_temp = str(max_temp)

            description = json_data["daily"][3]["weather"][0]["description"]
            print(max_temp)

            if description == "clear":
                description = "sunny weather"

            if description == "scattered clouds":
                description = "partly sunny weather"

            [print(description)]

            speak(
                f"next sunday you can expect a high of {max_temp} degrees and {description}")

        if day == "Friday":

            max_temp = json_data["daily"][2]["temp"]["max"]
            max_temp = (max_temp - 273)
            max_temp = round(max_temp)
            max_temp = str(max_temp)

            description = json_data["daily"][2]["weather"][0]["description"]
            print(max_temp)

            if description == "clear":
                description = "sunny weather"

            if description == "scattered clouds":
                description = "partly sunny weather"

            [print(description)]

            speak(
                f"next sunday you can expect a high of {max_temp} degrees and {description}")

        if day == "Saturday":

            max_temp = json_data["daily"][1]["temp"]["max"]
            max_temp = (max_temp - 273)
            max_temp = round(max_temp)
            max_temp = str(max_temp)

            description = json_data["daily"][1]["weather"][0]["description"]
            print(max_temp)

            if description == "clear":
                description = "sunny weather"

            if description == "scattered clouds":
                description = "partly sunny weather"

            [print(description)]

            speak(
                f"tomorrow you can expect a high of {max_temp} degrees and {description}")
    except:
        speak("sorry sir, i was unable to get the weather forecast for Sunday. please check your internet connection and try again")


def location_weather(text):
    try:
        QUERY_LIST = text.split()
        unwanted_words = {"how", "is", "the", "weather", "in", "tell", "me", "in", "how's"}
        QUERY_LIST = {word for word in QUERY_LIST if word not in unwanted_words}
        print(QUERY_LIST)
        text = " ".join(QUERY_LIST)
        g = geocoder.google(text)
        lat = g.lat
        lon = g.lon 
        url = f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&appid=24e4c072bb37a84df61ecc02544cdd99"
        json_data = requests.get(url).json()
        temp = json_data["current"]["temp"]
        temp = round(temp)
        temp = (temp - 273)
        temp = str(temp)

        description = json_data["current"]["weather"][0]["main"]

        if description == "Clouds":
            description = "cloudy skies"
        print(f"{temp} degrees")

        speak(
            f"currently in {text} it is {temp} degrees with {description}")

        min_temp = json_data["daily"][0]["temp"]["min"]
        max_temp = json_data["daily"][0]["temp"]["max"]

        min_temp = (min_temp - 273)
        max_temp = (max_temp - 273)

        min_temp = round(min_temp)
        max_temp = round(max_temp)

        max_temp = str(max_temp)
        min_temp = str(min_temp)

        description = json_data["daily"][0]["weather"][0]["description"]
        if description == "clear":
            description = "sunny weather"

        if description == "scattered clouds":
            description = "partly sunny weather"

        print(min_temp, max_temp)
        speak(
            f"today in {text} you can expect {description} with a high of {max_temp} degrees and a low of {min_temp}")
    except Exception as e:
        speak(f"sorry sir, i was unable to get the current weather of {text}. please check your internet connection and try again")
        print("Exception: " + str(e))