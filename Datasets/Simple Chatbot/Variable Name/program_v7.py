import random


def greet():
    res = ["Hello!", "Hi there!", "Greetings!"]
    return random.choice(res)


def farewell():
    r = ["Goodbye!", "See you later!", "Farewell!"]
    return random.choice(r)


def ask_name():
    return "What's your name?"


def respond_name(a):
    return f"Nice to meet you, {a}!"


def ask_age():
    return "How old are you?"


def respond_age(b):
    return f"You're {b} years old!"


def ask_hobby():
    return "What are your hobbies?"


def respond_hobby(not_a_hobby):
    return f"Ah, {not_a_hobby} sounds interesting!"


def ask_location():
    return "Where are you from?"


def respond_location(geo_location):
    return f"{geo_location} must be a nice place!"


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


if __name__ == "__main__":
    main()
