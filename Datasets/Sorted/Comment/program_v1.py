# Iteration 1
import random
def main():
    nums = [random.randint(1, 100) for _ in range(10)]
    print('Original list:', nums)
    nums.sort()
    print('Sorted list:', nums)
if __name__ == '__main__':
    main()
