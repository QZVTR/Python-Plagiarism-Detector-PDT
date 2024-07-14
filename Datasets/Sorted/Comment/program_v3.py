# Iteration 1
# This is a new comment added in iteration 1
import random
def main():
    nums = [random.randint(1, 100) for _ in range(10)]
    print('Original list:', nums)
    nums.sort()
# This is a new comment added in iteration 2
    print('Sorted list:', nums)
if __name__ == '__main__':
    main()
