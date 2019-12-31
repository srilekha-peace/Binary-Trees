class Bnode:
    def __init__(self,key):
        self.data = key
        self.left = None
        self.right = None

def height(root):
    if root == None:
        return -1

    return max(height(root.left),height(root.right)) + 1

if __name__ == '__main__':
    root = Bnode(10)
    root.left = Bnode(20)
    root.left.left = Bnode(30)
    root.right = Bnode(40)
    root.right.left = Bnode(50)
    root.right.right = Bnode(60)
    root.left.left.left = Bnode(70)
    print("The height of the given tree:",height(root))
