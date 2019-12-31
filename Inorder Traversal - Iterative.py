class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

def inorder(root):
    temp = root
    if temp is None:
        return

    stack = []
    set = 0

    while(not set):
        if temp is not None:
            stack.append(temp)
            temp = temp.left
        else:
            if(len(stack) > 0):
                temp = stack.pop()
                print(temp.data, end = " ")
                temp = temp.right
            else:
                set = 1

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    print("Inorder Traversal", end = " ")
    inorder(root)
