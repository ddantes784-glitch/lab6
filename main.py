def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    opor = arr[len(arr) // 2]
    left = [x for x in arr if x < opor]
    middle = [x for x in arr if x == opor]
    right = [x for x in arr if x > opor]
    return quick_sort(left) + middle + quick_sort(right)
print(quick_sort([20, 712, 8, 29, 13, 25]))