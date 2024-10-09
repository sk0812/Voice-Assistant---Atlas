from speak import speak, get_audio
from tinydb import TinyDB, Query



db = TinyDB("wish_list.json")
List = Query()


def add_item(text):
    try:
        QUERY_LIST = text.split()
        print(QUERY_LIST)
        wordsCount = len(QUERY_LIST)
        if wordsCount > 4:
            unwanted_words = {"add", "to", "my", "wishlist", "the"}
            item = (' '.join(i for i in text.split() if i not in unwanted_words))
            print(item)
            search = db.search(List.item == item)
            if not search:
                db.insert({"item": item})
                speak(f"okay sir, i have added {item} to your wish list")
            else:
                speak(
                    f"sorry sir, i was unable to add {item} to your wish list. it appears that {item} already exists")
        else:
            speak("what would you like to add to your wish list")
            item = get_audio()
            print(item)
            search = db.search(List.item == item)
            if not search:
                db.insert({"item": item})
                speak(f"okay sir, i have added {item} to your wish list")
            else:
                speak(
                    f"sorry sir, i was unable to add {item} to your wish list. it appears that {item} already exists")
    except:
        speak(f"sorry sir, i was unable to add {item} to your wishlist")


def remove_item(text):
    try:
        WORDS = text.split()
        print(WORDS)
        wordsCount = len(WORDS)
        if wordsCount > 4:
            unwanted_words = {"remove", "from", "my", "wishlist", "the"}
            item = (' '.join(i for i in text.split() if i not in unwanted_words))
            print(item)
            search = db.search(List.item == item)
            if not search:
                speak(
                    f"sorry sir, i was unable to remove {item} from your wish list. it appears that {item} does not exist")

            else:
                db.remove(List.item == item)
                speak(f"okay sir, i have removed {item} from your wish list")

        else:
            speak("what would you like to remove from your wish list")
            item = get_audio()
            print(item)
            search = db.search(List.item == item)
            if not search:
                speak(
                    f"sorry sir, i was unable to remove {item} from your wish list. it appears that {item} does not exist")

            else:
                db.remove(List.item == item)
                speak(f"okay sir, i have removed {item} from your wish list")
    except:
        speak(f"sorry sir, i was unable to remove {item} from your wish list")

        speak(f"sorry sir, i was unable to search for your item. please try again")


def deleteAll():
    try:
        speak("are you sure you want to delete all the items in your wishlist")
        answer = get_audio()
        if "yes" in answer:
            db.truncate()
            speak("okay sir, i have removed all the items from your wishlist")
        else:
            speak("okay sir")
    except:
        speak("sorry sir, i was unable to empty your wish list")


def countItems():
    count_items = len(db.all())
    speak(f"there are {count_items} items in your wishlist")
