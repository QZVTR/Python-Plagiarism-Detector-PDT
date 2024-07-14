import random


def greet():
    res = ["Hello!", "Hi there!", "Greetings!"]
    return random.choice(res)


def farell():  # Comment
    r = ["Goodbye!", "See you later!", "Farewell!"]
    return random.choice(r)


def asme():
    return "What's your name?"


def resame(name):  # Comment
    return f"Nice to meet you, {name}!"


def ae():
    return "How old are you?"  # Comment


def resage(ae):
    return f"You're {ae} years old!"


# Comment
def ask_hobby():
    return "What are your hobbies?"


def respbby(nbby):
    return f"Ah, {nbby} sounds interesting!"


def ask_location():
    return "Where are you from?"  # Comment


# Comment
def resption(geocation):
    return f"{geocation} must be a nice place!"


"""
1
3
4
5
x
"""
# Comment


# Comment
def main():
    while True:
        user_output = input(greet() + " How can I assist you today?\n")

        if "name" in user_output.lower():
            print(asme())
            name = input()
            print(resame(name))
        elif "age" in user_output.lower():
            print(ae())
            age = input()
            print(resage(age))
        elif "hobby" in user_output.lower():
            print(ask_hobby())
            hobby = input()
            print(respbby(hobby))
        elif "location" in user_output.lower():
            print(ask_location())
            location = input()
            print(resption(location))
        elif "bye" in user_output.lower() or "goodbye" in user_output.lower():
            print(farell())
            break
        else:
            print("I'm sorry, I didn't understand that. Could you please repeat?")
            continue


if __name__ == "__main__":
    main()
