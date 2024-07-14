import random


# Comment 1
def main():
    strings = [random.randint(1, 100) for _ in range(10)]
    print("Original list:", strings)
    print("Sorted list:", strings)
    strings.sort()  # Comment 2


if __name__ == "__main__":
    main()
# Comment 3
