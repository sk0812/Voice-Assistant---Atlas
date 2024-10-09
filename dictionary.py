#imports required functions and modules
from PyDictionary import PyDictionary
from speak import speak, get_audio
import random

#PyDictionary
dictionary = PyDictionary()


#definition of words
def definition(text):
    try:
        QUERY_LIST = text.split()
        unwanted_words = {"define", "definition", "meaning", "of",
                "mean", "does", "what", "is", "the", "word", "give", "me", "some"}
        QUERY_LIST = {word for word in QUERY_LIST if word not in unwanted_words}
        obj_count = len(QUERY_LIST)
        print(QUERY_LIST)
        print(obj_count)
        text = " ".join(QUERY_LIST)
        if obj_count > 2:
            speak(f"sorry sir, you have given me {obj_count} words to define, please try again")
        else:
            print(dictionary.meaning(text))
            speak(f"sir, the definition of {text} is")
            speak(dictionary.meaning(text))
    except:
        speak(f"sorry sir, i was unable to find the definition of {text}. please try again")

#synonym of words
def synonym(text):
    try:
        QUERY_LIST = text.split()
        unwanted_words = {"synonym", "synonyms", "for", "give", "me", "a", "what", "is", "word", "similar", "to", "few", "are", "some"}
        QUERY_LIST = {word for word in QUERY_LIST if word not in unwanted_words}
        obj_count = len(QUERY_LIST)
        print(obj_count)
        print(QUERY_LIST)
        text = " ".join(QUERY_LIST)
        if obj_count > 2:
            speak(f"sorry sir, you have given me {obj_count} words to find the synonyms for, please try again")
        else:
            synonym = dictionary.synonym(text)
            random_word = random.sample(synonym, 3)
            print(random_word)
            speak(f"sir, Synonyms for {text} include")
            speak(random_word)
    except:
        speak(f"sorry sir, i was unable to find synonyms for {text}. please try again")


#antonyms of words
def antonym(text):
    try:
        QUERY_LIST = text.split()
        unwanted_words = {"antonym", "antonyms", "for", "give", "me", "a", "word", "opposite", "to", "an", "are", "some", "few"}
        QUERY_LIST = {word for word in QUERY_LIST if word not in unwanted_words}
        obj_count = len(QUERY_LIST)
        print(obj_count)
        print(QUERY_LIST)
        text = " ".join(QUERY_LIST)
        if obj_count > 2:
            speak(f"sorry sir, you have given me {obj_count} words to find the antonyms for, please try again")
        else:
            antonym = dictionary.antonym(text)
            random_word = random.sample(antonym, 3)
            print(random_word)
            speak(f"sir, Antonyms for {text} include")
            speak(random_word)
    except:
        speak(f"sorry sir, i was unable to find antonyms for {text}. please try again")