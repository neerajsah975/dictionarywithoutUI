import json
from difflib import get_close_matches


def meaning(search):
    data = json.load(open("data.json"))
    if search.lower() in data:
        return data[search.lower()]
    elif search.title() in data:
        return data[search.title()]
    elif search.upper() in data:
        return data[search.upper()]
    elif len(get_close_matches(search, data.keys())) > 0:
        print("Did you mean %s instead\n " % get_close_matches(search, data.keys())[0])
        decide = input("Press y for yes or n for no: ")
        if decide == 'y' or 'Y':
            print(get_close_matches(search, data.keys())[0])
        elif decide == 'n' or 'N':
            print("You have entered the wrong word.")
        else:
            print('You have entered the wrong input. Please enter y or n')
    else:
        print("You have entered the wrong word.")


while True:
    print("\nWelcome to dictionary")
    print("Please choose the correct option:")
    print("Enter 1 to search a word ")
    print("Enter 0 to exit ")
    input_1 = input()
    if input_1 == '0':
        exit()
    elif input_1 == '1':
        word = input("Enter word to search dictionary: ")
        output = meaning(word)
        if type(output) == list:
            for text in output:
                print(text)
        else:
            print(output)
    else:
        print("You have entered the wrong option")
