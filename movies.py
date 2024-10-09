import imdb
from speak import speak, get_audio
import re


moviesDB = imdb.IMDb()


def search_movie(text):
    try:
        if "about" in text:
            QUERY_LIST = text.split()
            unwanted_words = {"tell", "me", "some",
                              "movie", "information", "about"}
            QUERY_LIST = {
                word for word in QUERY_LIST if word not in unwanted_words}
            print(QUERY_LIST)
            text = " ".join(QUERY_LIST)
            movie_name = text
            speak(
                f"okay sir, i am searching for {movie_name} in the imdb database")
            movies = moviesDB.search_movie(movie_name)
            id = movies[0].getID()
            movie = moviesDB.get_movie(id)
            title = movie['title']
            year = movie['year']
            rating = movie['rating']
            plot = movie['plot']
            plot = str(plot)
            plot = ' '.join(re.split(r'(?<=[.:;])\s', plot)[:2])
            speak(f"here is some information about {title}")
            print(title)
            print(year)
            print(rating)
            print(plot)
            if rating > 7.5:
                rating_comment = ("has a very good rating of")
            elif rating < 6.5:
                rating_comment = ("has a not so great rating of")
            else:
                rating_comment = ("has a rating of")
            speak(f"{title} was released in {year} and {rating_comment} {rating}")
            speak(f"{title} is about {plot}")
        else:
            speak("what movie would you like to search for?")
            movie_name = get_audio()
            speak(
                f"okay sir, i am searching for {movie_name} in the imdb database")
            movies = moviesDB.search_movie(movie_name)
            id = movies[0].getID()
            movie = moviesDB.get_movie(id)
            title = movie['title']
            year = movie['year']
            rating = movie['rating']
            plot = movie['plot']
            plot = str(plot)
            plot = ' '.join(re.split(r'(?<=[.:;])\s', plot)[:2])
            speak(f"here is some information about {title}")
            print(title)
            print(year)
            print(rating)
            print(plot)
            if rating > 7.5:
                rating_comment = ("has a very good rating of")
            elif rating < 6.5:
                rating_comment = ("has a not so great rating of")
            else:
                rating_comment = ("has a rating of")
            speak(f"{title} was released in {year} and {rating_comment} {rating}")
            speak(f"{title} is about {plot}")
    except Exception as e:
        speak(
            f"sorry sir, i was unable to search for the movie {movie_name}, please try again")
        print(e)



def top_movies():
    speak("the top ten movies are:")
    top = moviesDB.get_top250_movies()
    for movie in top[0:9]:
        print(movie)
        speak(movie)

def worst_movies():
    speak("the top ten worst movies are:")
    top = moviesDB.get_bottom100_movies()
    for movie in top[0:9]:
        print(movie)
        speak(movie)
