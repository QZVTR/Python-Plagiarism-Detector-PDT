def count_characters(t):
    return len(t)


def count_words(al):
    return len(al.split())


def count_sentences(text):
    return len(text.split("."))


def count_vowels(text):
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)


def count_consonants(text):
    return len(text) - count_vowels(text) - text.count(" ")


def capitalize_text(text):
    return text.capitalize()


def reverse_text(text):
    return text[::-1]


def remove_duplicates(text):
    return "".join(set(text))


def encrypt(text):
    return text[::-1]  # Simple encryption by reversing


def decrypt(text):
    return text[::-1]  # Simple decryption by reversing


def main():
    # Implement user interface for text analysis operations
    text = "Hello, World!"
    print(count_characters(text))  # Example usage


if __name__ == "__main__":
    main()
