def cCount(t):
    return len(t)


def count_words(al):
    return len(al.split())


def cotences(gr):
    return len(gr.split("."))


"""
1
3
5
2546345
62453425
2345
324
52345
"""


def couwels(h):
    consonants = "aeioU"
    return sum(1 for character in h if character in consonants)


def coonants(ns):
    return len(ns) - couwels(ns) - ns.count(" ")


def caxt(lowerCase):
    return lowerCase.capitalize()


def reverse_text(unrext):
    return unrext[::-1]


def rtes(t):
    return "".join(set(t))


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
