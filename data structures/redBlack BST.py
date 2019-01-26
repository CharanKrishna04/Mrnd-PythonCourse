class node:
    def __init__(self,color,key,left=None,right=None,p=None):
        self.color=color
        self.key=key
        self.left=left
        self.right=right
        self.p=p
class RBTree:
    def __init__(self):
        self.Nil=node('black',None,None,None,None)
        self.root=self.Nil
    
    def leftRotate(self,x):
        y=x.right
        x.right=y.left
        if y.left != self.Nil:
            y.left.p=x
        y.p=x.p
        if x.p==self.Nil:
            self.root=y
        elif x==x.p.left:
            x.p.left=y
        else:
            x.p.right=y
        y.left=x
        x.p=y
    def rightRotate(self,x):
        y=x.left
        x.left=y.right
        if y.right != self.Nil:
            y.right.p=x
        y.p=x.p
        if x.p==self.Nil:
            self.root=y
        elif x==x.p.left:
            x.p.left=y
        else:
            x.p.right=y
        y.right=x
        x.p=y
    def rbInsert(self,z):
        y=self.Nil
        x=self.root
        while x != self.Nil:
            y=x
            if z.key<x.key:
                x=x.left
            else:
                x=x.right
        z.p=y
        if y==self.Nil:
            self.root=z
        elif z.key < y.key:
            y.left=z
        else:
            y.right=z
        z.left=self.Nil
        z.right=self.Nil
        z.color='red'
        self.rbInsertFixup(z)
        
    def rbInsertFixup(self,z):
        while z.p.color == 'red':
            if z.p == z.p.p.left:
                y=z.p.p.right
                if y.color == 'red':
                    z.p.color='black'
                    y.color='black'
                    z.p.p.color='red'
                    z=z.p.p
                else:
                    if z== z.p.right:
                        z=z.p
                        self.leftRotate(z)
                    z.p.color='black'
                    z.p.p.color='red'
                    self.rightRotate(z.p.p)
            else:
                y=z.p.p.left
                if y.color == 'red':
                    z.p.color='black'
                    y.color='black'
                    z.p.p.color='red'
                    z=z.p.p
                else:
                    if z== z.p.left:
                        z=z.p
                        self.rightRotate(z)
                    z.p.color='black'
                    z.p.p.color='red'
                    self.leftRotate(z.p.p)
        self.root.color='black'
            
    def search(self,z):
        x=self.root
        while x != self.Nil:
            if z == x.key:
                return x
            elif z<x.key:
                x=x.left
            else:
                x=x.right
        return self.Nil
        
for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().strip().split()))
    T=RBTree()
    for i in range(n):
        T.rbInsert(node('red',l[i]))
    for i in range(n):
        count=0
        x=T.search(l[i])
        while x.left != T.Nil:
            count+=1
            x=x.left
        print('Smaller Elements on right side of ',l[i],' : ',count,sep='')
    print()
        
        