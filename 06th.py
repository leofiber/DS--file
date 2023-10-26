list_size = int(input("Enter the size of the list: "))
my_list = []
for i in range(list_size):
    element = int(input(f"Enter element {i + 1}: "))
    my_list.append(element)

target = int(input("Enter the number to search for: "))

def linear_search(arr, target):
    for i, element in enumerate(arr):
        if element == target:
            return i
    return -1

result_linear = linear_search(my_list, target)
if result_linear != -1:
    print(f"Linear Search: Element {target} found at index {result_linear}")
else:
    print(f"Linear Search: Element {target} not found")
