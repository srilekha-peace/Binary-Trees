class Bnode:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

def right_view(root):
    max_level = [0]
    util_func(root, 1, max_level)

def util_func(root,level,max_level):
    if root is None:
        return

    if max_level[0] < level:
        print(root.data, end = " ")
        max_level[0] = level

    util_func(root.right, level+1, max_level)
    util_func(root.left, level+1, max_level)


if __name__ == '__main__':
    root = Bnode(10)
    root.left = Bnode(20)
    root.right = Bnode(30)
    root.left.left = Bnode(40)
    root.left.right = Bnode(50)
    root.right.left =Bnode(60)
    root.right.right =Bnode(70)
    root.right.left.left = Bnode(80)
    root.right.right.left =Bnode(90)
    root.right.right.right =Bnode(100)
    root.right.right.left.left =Bnode(110)
    right_view(root)
