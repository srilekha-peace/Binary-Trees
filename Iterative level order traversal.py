class Bnode:
    def __init__(self,key):
        self.data = key
        self.left = None
        self.right = None

def height_func(root):
    if root is None:
        return 0
    else:
        left_ht = height_func(root.left)
        right_ht = height_func(root.right)
        if left_ht > right_ht:
            return left_ht + 1
        else:
            return right_ht + 1

def print_order(root):
    h = height_func(root)
    for i in range(1, h+1):
        print_level_func(root,i)

def print_level_func(root,level):
    if root is None:
        return
    if level == 1:
        print(root.data, end = " ")

    elif level > 1:
        print_level_func(root.left, level-1)
        print_level_func(root.right, level-1)

if __name__ == '__main__':
    root = Bnode(10)
    root.left = Bnode(20)
    root.right = Bnode(30)
    root.left.left = Bnode(40)
    root.left.right = Bnode(50)
    root.right.left = Bnode(60)
    root.right.right = Bnode(70)
    print_order(root)
