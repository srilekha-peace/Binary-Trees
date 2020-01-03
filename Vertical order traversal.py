class Bnode:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None

def vertical_func(root):
    if root is None:
        return

    m = {}
    hd = 0
    Util_func(root, hd, m)
    for index, value in m.items():
        print(index, value)

def Util_func(root, d, m):
    if root is None:
        return
    try:
        m[d].append(root.data)
    except:
        m[d] = [root.data]

    Util_func(root.left, d-1, m)
    Util_func(root.right, d+1, m)


if __name__ =='__main__':
    root = Bnode("A")
    root.left = Bnode("B")
    root.right = Bnode("C")
    root.left.left = Bnode("D")
    root.left.right = Bnode("E")
    root.right.left = Bnode("F")
    root.right.right = Bnode("G")
    root.left.left.left = Bnode("H")
    root.left.left.right = Bnode("I")
    root.left.right.left = Bnode("J")
    root.left.right.right = Bnode("K")
    root.right.right.left = Bnode("L")
    root.right.right.right = Bnode("M")
    vertical_func(root)
