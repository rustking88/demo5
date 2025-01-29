

# write a function that takes a list of numbers and returns the sum of the numbers

def sum_list(numbers):
    return sum(numbers)

print(sum_list([1, 2, 3, 4, 5]))

# 写一个二分查找算法
def binary_search(numbers, target):
    left, right = 0, len(numbers) - 1
    while left <= right:
        mid = (left + right) // 2
        if numbers[mid] == target:
            return mid
        elif numbers[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
