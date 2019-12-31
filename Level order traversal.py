class Bnode:
    def __init__(self,key):
        self.data = key
        self.left = None
        self.right = None

def level_order_traversal(root):
    if root is None:
        return

    queue = []
    queue.append(root)

    while (len(queue) > 0):
        element = queue.pop(0)
        print(element.data, end = " ")

        if element.left is not None:
            queue.append(element.left)

        if element.right is not None:
            queue.append(element.right)

if __name__ == '__main__':
    root = Bnode(1)
    root.left = Bnode(2)
    root.right = Bnode(3)
    root.left.left = Bnode(4)
    root.left.right = Bnode(5)
    root.right.left = Bnode(6)
    root.right.right = Bnode(7)
    level_order_traversal(root)
