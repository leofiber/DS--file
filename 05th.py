my_list = [10, 20, 30, 40, 50]
print("Current list:", my_list)
operation = input("Enter 'insert' or 'delete': ")
if operation == 'insert':
    element = int(input("Enter the element to insert: "))
    my_list.append(None)  
    my_list[-1] = element
    print("List after insertion at the end:", my_list)
elif operation == 'delete':
    if len(my_list) > 0:
        deleted_element = my_list.pop()
        print("Deleted element from the end:", deleted_element)
        print("List after deletion from the end:", my_list)
    else:
        print("The list is empty, so nothing to delete.")
else:
    print("Invalid operation. Please enter 'insert' or 'delete'.")
