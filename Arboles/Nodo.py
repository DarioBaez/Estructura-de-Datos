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

#print("\nPostorder")
#postorder(root)
print("\nPreorder")
preorder(root)
#print("\nInorder")
#inorder(root)