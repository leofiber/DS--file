my_list = [10, 20, 30, 40, 50]
print("Current list:", my_list)
operation = input("Enter 'insert' or 'delete': ")
if operation == 'insert':
    element = int(input("Enter the element to insert: "))
    my_list.append(None) 
    for i in range(len(my_list) - 1, 0, -1):
        my_list[i] = my_list[i - 1]
    my_list[0] = element
    print("List after insertion at the beginning:", my_list)
elif operation == 'delete':
    if len(my_list) > 0:
        deleted_element = my_list[0]
        for i in range(1, len(my_list)):
            my_list[i - 1] = my_list[i]
        my_list.pop()  
        print("Deleted element from the beginning:", deleted_element)
        print("List after deletion from the beginning:", my_list)
    else:
        print("The list is empty, so nothing to delete.")
else:
    print("Invalid operation. Please enter 'insert' or 'delete'.")
