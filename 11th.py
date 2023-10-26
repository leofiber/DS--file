def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    less_than_pivot = [x for x in arr[1:] if x <= pivot]
    greater_than_pivot = [x for x in arr[1:] if x > pivot]

    return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)
arr = [64, 34, 25, 12, 22, 11, 90]
print("Unsorted array:", arr)

sorted_array = quick_sort(arr)

print("Sorted array:", sorted_array)
