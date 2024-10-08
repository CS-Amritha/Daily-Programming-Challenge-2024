class Node:
    def __init__(self, v=0, l=None, r=None):
        self.val = v
        self.left = l
        self.right = r
def is_sym(root):
    def mirror(t1, t2):
        if not t1 and not t2: 
            return True
        if not t1 or not t2:   
            return False
        return (t1.val == t2.val) and mirror(t1.left, t2.right) and mirror(t1.right, t2.left)
    return mirror(root, root)
def build_tree(lst):
    if not lst:
        return None    
    root = Node(lst[0])
    q = [root]
    i = 1
    while i < len(lst):
        cur = q.pop(0)        
        if lst[i] is not None:
            cur.left = Node(lst[i])
            q.append(cur.left)
        i += 1
        
        if i < len(lst) and lst[i] is not None:
            cur.right = Node(lst[i])
            q.append(cur.right)
        i += 1
    
    return root
vals = [1, 2, 2, 3, 4, 4, 3]
root = build_tree(vals)
print(is_sym(root))
