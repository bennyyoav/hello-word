class Node:

    def __init__(self, item, left=None, right=None):
        """(Node, object, Node, Node) -> NoneType
        Initialize this node to store item and have children left and right.
        """
        self.item = item
        self.left = left
        self.right = right

def depth(Node):
    if Node==None:
        return 0
    return 1 + max(depth(Node.left), depth(Node.right))
if __name__ =="__main__":
    root=Node(1)
    root.left=Node(2)
    root.left.left=Node(3)
    root.left.left.left=Node(4)
    root.left.left.left.left = Node(5)
    root.right=Node(1)
    print (depth(root))