def find_floor(arr, target):
    n = len(arr)
    left, right = 0, n - 1
    floor = -1
    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return arr[mid]
        elif arr[mid] < target:
            floor = arr[mid]
            left = mid + 1
        else:
            right = mid - 1
    return floor
def find_ceil(arr, target):
    n = len(arr)
    left, right = 0, n - 1
    ceil = -1
    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return arr[mid]
        elif arr[mid] < target:
            left = mid + 1
        else:
            ceil = arr[mid]
            right = mid - 1
    return ceil
def find_peak(arr):
    n = len(arr)
    left, right = 0, n - 1

    while left < right:
        mid = (left + right) // 2

        if arr[mid] > arr[mid + 1]:
            return arr[mid]
        elif arr[mid] < arr[mid + 1]:
            left = mid + 1
        else:
            right = mid

    return arr[left]

def find_minimum(arr):
    n = len(arr)
    left, right = 0, n - 1

    while left < right:
        mid = (left + right) // 2

        if arr[mid] > arr[right]:
            left = mid + 1
        else:
            right = mid

    return arr[left]
arr = [30, 40, 50, 10, 20]
target = 15
print("Floor:", find_floor(arr, target))
print("Ceil:", find_ceil(arr, target))
print("Peak:", find_peak(arr))
print("Minimum:", find_minimum(arr))
