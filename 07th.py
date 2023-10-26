list_size = int(input("Enter the size of the list: "))
my_list = []
for i in range(list_size):
    element = int(input(f"Enter element {i + 1}: "))
    my_list.append(element)

target = int(input("Enter the number to search for: "))

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

my_list.sort() #We can skip this if we know that the list is already sorted
result_binary = binary_search(my_list, target)
if result_binary != -1:
    print(f"Binary Search: Element {target} found at index {result_binary}")
else:
    print(f"Binary Search: Element {target} not found")