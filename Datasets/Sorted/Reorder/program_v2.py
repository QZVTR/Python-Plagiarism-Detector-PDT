import random


def main():
    nums = [random.randint(1, 100) for _ in range(10)]
    print("Original list:", nums)
    print("Sorted list:", nums)
    nums.sort()


if __name__ == "__main__":
    main()
