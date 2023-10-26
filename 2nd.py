a = input("Enter a string : ")
cleaned_input = a.replace(" ", "").lower()
palindrome = True
for i in range(len(cleaned_input) // 2):
    if cleaned_input[i] != cleaned_input[-i - 1]:
        palindrome = False
        break
if palindrome:
    print("The input string is a palindrome.")
else:
    print("The input string is not a palindrome.")
