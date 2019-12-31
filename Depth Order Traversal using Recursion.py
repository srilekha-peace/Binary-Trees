class Node:
    def __init__(self,key):
        self.data = key
        self.left = None
        self.right = None

#left, root,right
def inorder(temp):
    if (not temp):
        return

    inorder(temp.left)
    print(temp.data, end = " ")
    inorder(temp.right)

#root, left, right
def preorder(temp):
    if (not temp):
        return

    print(temp.data, end = " ")
    preorder(temp.left)
    preorder(temp.right)

#left,right, root
def postorder(temp):
    if (not temp):
        return

    postorder(temp.left)
    postorder(temp.right)
    print(temp.data, end = " ")

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
    print("\n")
    print("Preorder Traversal", end = " ")
    preorder(root)
    print("\n")
    print("Postorder Traversal", end = " ")
    postorder(root)
