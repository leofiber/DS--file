class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

def buildTree(arr, index, n):
    if index < n and arr[index] is not None:
        root = Node(arr[index])
        root.left = buildTree(arr, 2 * index + 1, n)
        root.right = buildTree(arr, 2 * index + 2, n)
        return root
    return None

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        input_str = input().split()
        arr = [int(val) if val != "None" else None for val in input_str]
        n = len(arr)
        root = buildTree(arr, 0, n)
