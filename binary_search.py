import random
random.seed(0)

def binary_search(arr, item):
    arr = sorted(arr)
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

my_list = [random.randint(0, 100) for _ in range(10)]
print(sorted(my_list))

print(binary_search(my_list, 38)) # => 1
print(binary_search(my_list, -1)) # => None
print(binary_search(my_list, 62)) # => None
