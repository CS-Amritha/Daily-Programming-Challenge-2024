class Node:
    def __init__(self, v=0, l=None, r=None):
        self.v = v
        self.l = l
        self.r = r

def isBST(root: Node) -> bool:
    def chk(n, lo=float('-inf'), hi=float('inf')):
        if not n:
            return True
        if not (lo < n.v < hi):
            return False
        return chk(n.l, lo, n.v) and chk(n.r, n.v, hi)

    return chk(root)
root = Node(2)
root.l = Node(1)
root.r = Node(3)

print(isBST(root))  
