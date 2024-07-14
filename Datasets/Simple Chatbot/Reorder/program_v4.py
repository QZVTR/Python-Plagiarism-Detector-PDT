import random


def ask_name():
    return "What's your name?"


def farewell():
    responses = ["Goodbye!", "See you later!", "Farewell!"]
    return random.choice(responses)


def greet():
    responses = ["Hello!", "Hi there!", "Greetings!"]
    return random.choice(responses)


def respond_name(name):
    return f"Nice to meet you, {name}!"


def ask_age():
    return "How old are you?"


def respond_age(age):
    return f"You're {age} years old!"


def ask_hobby():
    return "What are your hobbies?"


def respond_hobby(hobby):
    return f"Ah, {hobby} sounds interesting!"


def ask_location():
    return "Where are you from?"


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