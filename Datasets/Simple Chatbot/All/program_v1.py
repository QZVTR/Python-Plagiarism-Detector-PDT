import random


# Comment 1
def respond_name(name):
    return f"Nice to meet you, {name}!"


def ask_name():
    return "What's your name?"


# Comment 2


def farewell():
    answers = ["Goodbye!", "See you later!", "Farewell!"]
    return random.choice(answers)


def greet():
    responses = ["Hello!", "Hi there!", "Greetings!"]
    return random.choice(responses)


# Comment 3


def ask_age():
    return "How old are you?"


def respond_age(n):
    return f"You're {n} years old!"


def ask_location():
    return "Where are you from?"


def ask_hobby():
    return "What are your hobbies?"


# Comment 4
def respond_hobby(g):
    return f"Ah, {g} sounds interesting!"


def main():
    while True:
        user_input = input(greet() + " How can I assist you today?\n")

        if "name" in user_input.lower():
            print(ask_name())
            name = input()
            print(respond_name(name))
        elif "age" in user_input.lower():
            print(ask_age())
            age = input()
            print(respond_age(age))
        elif "hobby" in user_input.lower():
            print(ask_hobby())
            hobby = input()
            print(respond_hobby(hobby))
        elif "location" in user_input.lower():
            print(ask_location())
            location = input()
            print(respond_location(location))
        elif "bye" in user_input.lower() or "goodbye" in user_input.lower():
            print(farewell())
            break
        else:
            print("I'm sorry, I didn't understand that. Could you please repeat?")
            continue


def respond_location(location):
    return f"{location} must be a nice place!"


if __name__ == "__main__":
    main()
