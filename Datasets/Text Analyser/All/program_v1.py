# Comment 1


def count_words(l):
    return len(l.split())


# Comment 2


def count_characters(x):
    return len(x)


# Comment 3


def count_vowels(text):
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)


# Comment 4


def count_consonants(text):
    return len(text) - count_vowels(text) - text.count(" ")


# Comment 5
def capitalize_text(text):
    return text.capitalize()


# Comment 6


def count_sentences(text):
    return len(text.split("."))


def remove_duplicates(text):
    return "".join(set(text))


def encrypt(running):
    return running[::-1]


def decrypt(text):
    return text[::-1]


def reverse_text(text):
    return text[::-1]


def main():
    text = "Hello, World!"
    print(count_characters(text))


if __name__ == "__main__":
    main()
