class Bnode:
    def __init__(self,key):
        self.data = key
        self.left = None
        self.right = None

def sprial_order(root):
    if root is None:
        return

    stack1 = []
    stack2 = []
    stack1.append(root)

    while (len(stack1)>0) or (len(stack2)>0):
        while (len(stack1)>0):
            element = stack1.pop(-1)
            print(element.data, end = " ")
            if element.right is not None:
                stack2.append(element.right)
            if element.left is not None:
                stack2.append(element.left)
        while (len(stack2)>0):
            element = stack2.pop(-1)
            print(element.data, end = " ")
            if element.left is not None:
                stack1.append(element.left)
            if element.right is not None:
                stack1.append(element.right)

if __name__ == '__main__':
    root = Bnode(1)
    root.left = Bnode(2)
    root.right = Bnode(3)
    root.left.left = Bnode(4)
    root.left.right = Bnode(5)
    root.right.left = Bnode(6)
    root.right.right = Bnode(7)
    root.left.left.left = Bnode(8)
    root.right.left.right = Bnode(9)
    sprial_order(root)
