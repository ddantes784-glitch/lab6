def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
sorted_nums = [12, 15, 18, 122, 126, 233, 338, 556]
print(binary_search(sorted_nums, 233))