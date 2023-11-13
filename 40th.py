def nge_left_to_right(arr, query):
    n = len(arr)
    result = [-1] * n
    stack = []

    for i in range(n):
        while stack and arr[i] > arr[stack[-1]]:
            result[stack.pop()] = arr[i]
        stack.append(i)

    ans = []
    for q in query:
        ans.append(result[q])

    return ans

def nge_right_to_left(arr, query):
    n = len(arr)
    result = [-1] * n
    stack = []

    for i in range(n - 1, -1, -1):
        while stack and arr[i] > arr[stack[-1]]:
            result[stack.pop()] = arr[i]
        stack.append(i)

    ans = []
    for q in query:
        ans.append(result[q])

    return ans

def nse_left_to_right(arr, query):
    n = len(arr)
    result = [-1] * n
    stack = []

    for i in range(n):
        while stack and arr[i] < arr[stack[-1]]:
            result[stack.pop()] = arr[i]
        stack.append(i)

    ans = []
    for q in query:
        ans.append(result[q])

    return ans

def nse_right_to_left(arr, query):
    n = len(arr)
    result = [-1] * n
    stack = []

    for i in range(n - 1, -1, -1):
        while stack and arr[i] < arr[stack[-1]]:
            result[stack.pop()] = arr[i]
        stack.append(i)

    ans = []
    for q in query:
        ans.append(result[q])

    return ans

n = 5 
arr = [4, 2, 9, 5, 1]
m = 3
query = [1, 3, 4]

result1 = nse_right_to_left(arr, query)
print("NSE_RightToLeft:", end=" ")
for r in result1:
    print(r, end=" ")
print()

result2 = nse_left_to_right(arr, query)
print("NSE_LeftToRight:", end=" ")
for r in result2:
    print(r, end=" ")
print()

result3 = nge_right_to_left(arr, query)
print("NGE_RightToLeft:", end=" ")
for r in result3:
    print(r, end=" ")
print()

result4 = nge_left_to_right(arr, query)
print("NGE_LeftToRight:", end=" ")
for r in result4:
    print(r, end=" ")
print()
