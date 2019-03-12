# Code to implement a binary search tree 
# Programmed by Diego Quinones
# Last modified March 10, 2019

class BST(object):
    # Constructor
    def __init__(self, item, left=None, right=None):  
        self.item = item
        self.left = left 
        self.right = right      
        
def Insert(T,newItem):
    if T == None:
        T =  BST(newItem)
    elif T.item > newItem:
        T.left = Insert(T.left,newItem)
    else:
        T.right = Insert(T.right,newItem)
    return T

def Delete(T,del_item):
    if T is not None:
        if del_item < T.item:
            T.left = Delete(T.left,del_item)
        elif del_item > T.item:
            T.right = Delete(T.right,del_item)
        else:  # del_item == T.item
            if T.left is None and T.right is None: # T is a leaf, just remove it
                T = None
            elif T.left is None: # T has one child, replace it by existing child
                T = T.right
            elif T.right is None:
                T = T.left    
            else: # T has two chldren. Replace T by its successor, delete successor
                m = Smallest(T.right)
                T.item = m.item
                T.right = Delete(T.right,m.item)
    return T
         
def InOrder(T):
    # Prints items in BST in ascending order
    if T is not None:
        InOrder(T.left)
        print(T.item,end = ' ')
        InOrder(T.right)
  
def InOrderD(T,space):
    # Prints items and structure of BST
    if T is not None:
        InOrderD(T.right,space+'   ')
        print(space,T.item)
        InOrderD(T.left,space+'   ')
  
def SmallestL(T):
    # Returns smallest item in BST. Returns None if T is None
    if T is None:
        return None
    while T.left is not None:
        T = T.left
    return T   
 
def Smallest(T):
    # Returns smallest item in BST. Error if T is None
    if T.left is None:
        return T
    else:
        return Smallest(T.left)

def Largest(T):
    # Returns largest item in BST. Error if T is None
    if T.right is None:
        return T
    else:
        return Largest(T.right)   

def Find(T,k):
    # Returns the address of k in BST, or None if k is not in the tree
    if T is None or T.item == k:
        return T
    if T.item<k:
        return Find(T.right,k)
    return Find(T.left,k)

def iterativeSearch(T, k):
    # Set current to root of binary tree 
    if T is None:
        #return -1 if empty
        return -1
    while T is not None:
        #moves to each side depending if less or more
        if T.item>k:
            T=T.left
        elif T.item==k:
            return 1
        elif T.item<k:
            T=T.right
    #return -1 is not found
    return -1
    
def FindAndPrint(T,k):
    f = Find(T,k)
    if f is not None:
        print(f.item,'found')
    else:
        print(k,'not found')
        
def Extract(T,L):
    if T is not None:
        #moves to left child
        InOrder(T.left)
        #adds item to a BST
        L.append(T.item)
        #moves to the right child
        InOrder(T.right)
    return L

def PrintAtDepth(T):
  NewList=[T]
  count=0
  while NewList:
      #list that will store remaining values
      NewList2=[]
      #prints text and number of depth
      print('Keys at: ',count)
      for i in NewList:
          print(i.item)
          if i.left:
              #values being used get stored
              NewList2.append(i.left)
          if i.right:
              NewList2.append(i.right)
      count=count+1
      #NewList is reset with the remaining values
      NewList=NewList2
          
def BalancedTree(L):
    if not L: 
        #if list is empty return none
        return None 
    mid = round((len(L)) / 2)
    #divide by the middle
    T1 = BST(L[mid]) 
    #moves values to the left and right accordingly
    T1.left = BalancedTree(L[:mid]) 
    T1.right = BalancedTree(L[mid+1:]) 
    return T1
              
# Code to test the functions above
T = None
A = [70, 50, 90, 130, 150, 40, 10, 30, 100, 180, 45, 60, 140, 42]
for a in A:
    T = Insert(T,a)
    
InOrder(T)
print()
InOrderD(T,'')
print()

print('Iterative Search',end=' ')
findvalue=11
find=iterativeSearch(T,findvalue)
print()
if find==1:
    print(findvalue,'Value was found')
else:
    print(findvalue,'Value was not found')


print()
print('Extract',end=' ')
print()
L=[]
L=Extract(T,L)
for i in L:
    print(i, end=' ')
print()   

print()
PrintAtDepth(T)
print()
print('Balanced Tree')
print()
L1=[3,5,7,20]
T1=BalancedTree(L1)
InOrder(T1)
print()
InOrderD(T1,' ')






