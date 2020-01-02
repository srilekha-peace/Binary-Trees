class Node:
    def __init__(self,key):
        self.data = key
        self.left = None
        self.right = None

def diagonal_func(root):
    # Queue = q
    if root is None:
        return
    q = []
    q.append(root)
    q.append(None)
    while (len(q)>0):
        p = q.pop(0)
        if (not p):
            if len(q) == 0:
                return
            print(' ')
            q.append(None)
        else:
            while (p):
                print(p.data, end = " ")
                if(p.left):
                    q.append(p.left)
                p = p.right

root = Node(8)
root.left = Node(3)
root.right = Node(10)
root.left.left = Node(1)
root.left.right = Node(6)
root.right.right = Node(14)
root.right.right.left = Node(13)
root.left.right.left = Node(4)
root.left.right.right = Node(7)
diagonal_func(root)
