import math
from collections import deque
class node:
    def __init__(self):
        self.lchild=None
        self.rchild=None
        
b=[0,1,2,3,4,5,  6, 7,8 ,9 ,10]
a=[9,3,7,1,8,12,10,20,15,18,5]
l=len(a)
left=[]
right=[]
stk=deque()

for i in range(l):
    while stk and a[stk[-1]]>a[i]:
        stk.pop()
    if stk:
        left.append(stk[-1])
        stk.append(i)
    else:
        stk.append(i)
        left.append(None)
stk.clear()

for i in range(1,l+1):
    while stk and a[stk[-1]]>a[-i]:
        stk.pop()
    if stk:
        right.append(stk[-1])
        stk.append(l-i)
    else:
        stk.append(l-i)
        right.append(None)
right.reverse()
cartesian_tree=[node() for i in range(l)]
root=None
for i in range(l):
    if left[i]!=None:
        if right[i]!=None:
            if a[left[i]]>a[right[i]]:
                if left[i]>i:
                    cartesian_tree[left[i]].lchild=i
                else:
                    cartesian_tree[left[i]].rchild=i
            else:
                if right[i]>i:
                    cartesian_tree[right[i]].lchild=i
                else:
                    cartesian_tree[right[i]].rchild=i
        else:
            if left[i]>i:
                cartesian_tree[left[i]].lchild=i
            else:
                cartesian_tree[left[i]].rchild=i
    else:
        if  right[i]!=None:
            if right[i]>i:
                cartesian_tree[right[i]].lchild=i
            else:
                cartesian_tree[right[i]].rchild=i
        else:
            root=i
print(root)
for i in range(l):
    print(cartesian_tree[i].lchild,cartesian_tree[i].rchild)
