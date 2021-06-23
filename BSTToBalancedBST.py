class Node:
    def __init__(self,data):
            self.data=data
            self.left=None
            self.right=None


def BST(root,nodes):
    if not root:
        return
	
    BST(root.left,nodes)
    nodes.append(root)
    BST(root.right,nodes)


def balancedBST(nodes,start,end):
	if start>end:
	    return None
	mid=(start+end)//2
	node=nodes[mid]

	
	node.left=balancedBST(nodes,start,mid-1)
	node.right=balancedBST(nodes,mid+1,end)
	return node


def buildTree(root):
    nodes=[]
    BST(root,nodes)
    n=len(nodes)
    return balancedBST(nodes,0,n-1)

def preOrder(root):
    if not root:
        return
    print('{} '.format(root.data),end="")
    preOrder(root.left)
    preOrder(root.right)


root = Node(30)
root.left = Node(20)
root.left.left = Node(10)
root = buildTree(root)
preOrder(root)
	

