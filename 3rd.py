arr = [1,2,3,4,5]
print("Current array:", arr)
operation = input("Enter 'insert' or 'delete': ")
if operation == 'insert':
    element = int(input("Enter the element to insert: "))
    position = int(input("Enter the position to insert at: "))
    if 0 <= position <= len(arr):
        arr.append(None)  
        for i in range(len(arr) - 1, position, -1):
            arr[i] = arr[i - 1]
        arr[position] = element
        print("Array after insertion:", arr)
    else:
        print("Invalid position for insertion.")
elif operation == 'delete':
    position = int(input("Enter the position to delete from: "))
    if 0 <= position < len(arr):
        deleted_element = arr[position]
        for i in range(position, len(arr) - 1):
            arr[i] = arr[i + 1]
        arr.pop() 
        print("Deleted element:", deleted_element)
        print("Array after deletion:", arr)
    else:
        print("Invalid position for deletion.")
else:
    print("Invalid operation. Please enter 'insert' or 'delete'.")
