class Node(object):
    def __init__(self,val,parent,left, right):
        self.val=val
        self.parent=parent
        self.left = left
        self.right = right
map_tree=dict() 
f = open("tree.txt", "rt")
for line in f: 
    st=(line.rstrip('\n')).split(",")
    k=dict() 
    k['p']=st[1] 
    k['l']=st[2]
    k['r']=st[3] 
    map_tree[st[0]]= k
    
    
start=list(map_tree)[0]

def make_tree(node):
    info=map_tree[node]
    if info['p']=='x':
        parent=None
    else:
        parent=info['p']
    if info['l']!='x':
        left=make_tree(info['l'])
    else:
        left=None
    if info['r']!='x':
        right=make_tree(info['r'])
    else:
        right=None
    return Node(node,parent,left,right)

def lca(root_node,val1,val2):
    
    if root_node==None:
        return None
    
    if root_node.val==val1 or root_node.val==val2:
        
        return root_node
    
    left=lca(root_node.left,val1,val2)
    right=lca(root_node.right,val1,val2)
    
    if left==None and right==None:
        return None
    
    if left!=None and right!=None:
        return root_node
    
    if left==None:
        return right
    
    else:
        return left
    
    
lca(root_main,'8','3').val    