class Bnode:
    def __init__(self,key):
        self.data = key
        self.left = None
        self.right = None

def print_leaf(root):
    
    if root is None:
        return

    if root.left is None and root.right is None:
        print(root.data, end = " ")

    print_leaf(root.left)
    print_leaf(root.right)


if __name__ == '__main__':
    root = Bnode(10)
    root.left = Bnode(20)
    root.left.left = Bnode(30)
    root.right = Bnode(50)
    root.right.left = Bnode(60)
    root.right.right = Bnode(70)
    root.left.right = Bnode(40)
    root.left.right.left = Bnode(80)
    print_leaf(root)
