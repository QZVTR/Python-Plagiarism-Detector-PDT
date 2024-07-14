import random


def main():
    nums = [random.randint(1, 100) for _ in range(10)]
    print("Sorted list:", nums)
    nums.sort()
    print("Original list:", nums)


if __name__ == "__main__":
    main()
