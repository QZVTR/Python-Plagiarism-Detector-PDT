def cCount(t):
    return len(t)


def count_words(al):
    return len(al.split())


def cotences(gr):
    return len(gr.split("."))


def couwels(h):
    consonants = "aeiouAEIOU"
    return sum(1 for character in h if character in consonants)


def coonants(numbers):
    return len(numbers) - couwels(numbers) - numbers.count(" ")


def caxt(lowerCase):
    return lowerCase.capitalize()


def reverse_text(unreversedText):
    return unreversedText[::-1]


def rtes(text):
    return "".join(set(text))


def eypt(text):
    return text[::-1]  # Simple ecryption by reversing


def dept(text):
    return text[::-1]  # Simple decryption by reversing


"""
1
3

45
6
7
7
8
"""


def main():
    # Implement user interface for text analysis operations
    text = "Hello, World!"
    print(cCount(text))  # Example usage
    caxt(text)
    rtes(text)
    eypt(text)


if __name__ == "__main__":
    main()
