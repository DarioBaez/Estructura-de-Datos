class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


def preorder(node):
    if node:
        print(node.data)
        preorder(node.left)
        preorder(node.right)

def inorder(node):
    if node:
        inorder(node.left)
        print(node.data)
        inorder(node.right)

def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.data)

root = Node("ALimentos")
root.left = Node("Vegetales")
root.right = Node("Frutas")
root.left.left = Node("Lechuga")
root.left.right = Node("Cebolla")

root2 = Node(10)
root2.left = Node(14)
root2.right = Node(5)
root2.left.left = Node(21)
root2.left.right = Node(15)
root2.right.left = Node(25)
root2.right.right = Node(6)
root2.left.left.left = Node(40)
root2.left.left.right = Node(22)
root2.right.left.left = Node(35)
root2.right.left.right = Node(78)
root2.right.right.left = Node(90)
root2.right.right.right = Node(15)


#print("\nPostorder")
#postorder(root)
print("\nPreorder")
postorder(root2)
#print("\nInorder")
#inorder(root)