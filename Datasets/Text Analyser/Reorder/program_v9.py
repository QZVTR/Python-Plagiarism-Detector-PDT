def main():
    # Implement user interface for text analysis operations
    text = "Hello, World!"
    print(count_characters(text))  # Example usage


def count_words(text):
    return len(text.split())


def count_sentences(text):
    return len(text.split("."))


def count_characters(text):
    return len(text)


def reverse_text(text):
    return text[::-1]


def count_vowels(text):
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)


def count_consonants(text):
    return len(text) - count_vowels(text) - text.count(" ")


def capitalize_text(text):
    return text.capitalize()


def decrypt(text):
    return text[::-1]  # Simple decryption by reversing


def encrypt(text):
    return text[::-1]  # Simple encryption by reversing


def remove_duplicates(text):
    return "".join(set(text))


if __name__ == "__main__":
    main()
