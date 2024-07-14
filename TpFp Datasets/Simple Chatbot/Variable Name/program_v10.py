import random


def a():
    res = ["lo!", "H", "Gres!"]
    return random.choice(res)


def farell():  # Comment
    r = ["Green!", "d!", "Comment!"]
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


def ation():
    return "Where are you from?"  # Comment


# Comment
def resption(geocation):
    return f"{geocation} must be a nice place!"


"""
1
3
4
5a
x
"""
# Comment


# Comment
def mai():
    while True:
        output = input(a() + " How can I assist you today?\n")

        if "name" in output.lower():
            print(asme())
            name = input()
            print(resame(name))
        elif "hobby" in output.lower():
            print(ask_hobby())
            hobby = input()
            print(respbby(hobby))
        elif "age" in output.lower():
            print(ae())
            age = input()
            print(resage(age))
        elif "bye" in output.lower() or "goodbye" in output.lower():
            print(farell())
        elif "location" in output.lower():
            print(ation())
            location = input()
            print(resption(location))

            break
        else:
            print("I'm sorry, I didn't understand that. Could you please repeat?")
            continue


if __name__ == "__main__":
    mai()
