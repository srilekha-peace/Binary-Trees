class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


def inorder(temp):
    if (not temp):
        return

    inorder(temp.left)
    print(temp.data, end = " ")
    inorder(temp.right)

def insert(temp,key):
    que = []
    que.append(temp)
    while(len(que)):
        temp = que[0]
        que.pop(0)

        if(not temp.left):
            temp.left = Node(key)
            break
        else:
            que.append(temp.left)

        if(not temp.right):
            temp.right = Node(key)
            break
        else:
            que.append(temp.right)

if __name__ == '__main__':
    root = Node(10)
    root.left =Node(20)
    root.left.left = Node(30)
    root.right = Node(40)
    root.right.left = Node(50)
    root.right.right = Node(60)
    print("Inorder Traversal before Insertion:", end= " ")
    inorder(root)
    key = 70
    insert(root, key)
    print("\n")
    print("Inorder Traversal after Insertion:", end= " ")
    inorder(root)
