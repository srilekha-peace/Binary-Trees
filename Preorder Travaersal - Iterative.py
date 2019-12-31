class Node:
    def __init__(self,key):
        self.data = key
        self.left = None
        self.right = None

def preorder(root):
    temp = root
    if temp is None:
        return

    stack = []
    stack.append(temp)

    while (len(stack)>0):
        element = stack.pop()
        print(element.data, end = " ")

        if element.right is not None:
            stack.append(element.right)

        if element.left is not None:
            stack.append(element.left)


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    print("Preorder Traversal", end = " ")
    preorder(root)
