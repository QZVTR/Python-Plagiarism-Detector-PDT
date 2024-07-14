import random


def main():
    strings = [random.randint(1, 100) for _ in range(10)]
    print("Original list:", strings)
    strings.sort()
    print("Sorted list:", strings)


if __name__ == "__main__":
    main()
