def count_characters(t):
    return len(t)


def count_words(al):
    return len(al.split())


def count_sentences(gr):
    return len(gr.split("."))


def count_vowels(h):
    consonants = "aeiouAEIOU"
    return sum(1 for character in h if character in consonants)


def count_consonants(numbers):
    return len(numbers) - count_vowels(numbers) - numbers.count(" ")


def capitalize_text(lowerCase):
    return lowerCase.capitalize()


def reverse_text(unreversedText):
    return unreversedText[::-1]


def remove_duplicates(duplicates):
    return "".join(set(duplicates))


def encrypt(decrypt):
    return decrypt[::-1]  # Simple encryption by reversing


def decrypt(encrypt):
    return encrypt[::-1]  # Simple decryption by reversing


def main():
    # Implement user interface for text analysis operations
    s = "Hello, World!"
    print(count_characters(s))  # Example usage


if __name__ == "__main__":
    main()
