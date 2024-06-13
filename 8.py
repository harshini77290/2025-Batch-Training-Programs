'''Problem Statement No. 3: Lexi String
Little JIll Jumbled up the order of the letters in our dictionary.
Now, Jack uses this list to find the smallest lexicographical string that
can be made out of this new order, Can you help him?You are given a string P
that denotes the new order of letters in the English dictionary.
You need to print the smallest lexicographic string made from the
given string S.
Constraints: 1 <= T <= 1000
Length (P) = 262 <= length (S) <= 100
All characters In the string S, P are in lowercase
Input Format:
The first line contains number of test cases T
The second line has the string P The third line has the string S
Output:
Print a single string in a new line for every test case giving the result


t=int(input("Enter no of test cases:"))
for _ in range(1,t+1):
    p=input("Enter dictionary:")
    s=input("Enter string:")
    temp=""
    for i in p:
        if i in s:
            temp+=i
    print(temp)


Postorder:
    if(root==NULL) return;
    postorder(root->left);
    postorder(root->right);
    print('%d->',root->data)
    
Preorder:
    if(root==NULL) return;
    print('%d->',root->data)
    preorder(root->left);
    preorder(root->right);
    
Levelorder:(alg)
    printLevelorder(tree)
    for d=1 to height(tree)
    printCurrentLevel(tree,d);

    printCurrentLevel(tree,level)
    if tree is NULL then return;
    if level is 1 then
       print(tree->data)
    elseif level >1 then
       printCurrentLevel(tree->left,level-1):
           printCurrentLevel(tree->right,level-1):
    Time Complexity:O(n^2) in worst case
    Space Complexity:O(n) in worst case


QUESTIONS:

Tree contruction
Tree traversal-level order,vertical order
Tree views-Left,Right,Top,Bottom views
Check given binary tree is bst
Check mirrorred binary tree
Height of binary tree
Print all nodes at level



def totalsum(self,root):
    if root is None:
        return 0
    else:
        leftsum=totalsum(root.left)
        rightsum=totalsum(root.right)
        return root.data+leftsum+rightsum
def treemax(self,root):
    if root is None:
        return 0
    else:
        leftmax=totalsum(root.left)
        rightmax=totalsum(root.right)
        #return root.data+leftsum+rightsum
    return max(root.data,leftmax,rightmax)
def treeheight(self,root):
    if root is None:
        return 0
    else:
        leftheight=treeheight(root.left)
        rightheight=treeheight(root.right)
        return 1+max(leftheight,rightheight)

#Binary Logics
Logics for binary tree

def totalsum(self,root):
    if root is None:
        return 0
    else:
        leftsum=totalsum(root.left)
        rightsum=totalsum(root.right)
        return root.data+leftsum+rightsum
def treemax(self,root):
    if root is None:
        return 0
    else:
        leftmax=totalsum(root.left)
        rightmax=totalsum(root.right)
    return max(root.data,leftmax,rightmax)
def treeheight(self,root):
    if root is None:
        return 0
    else:
        leftheight=treeheight(root.left)
        rightheight=treeheight(root.right)
        return 1+max(leftheight,rightheight)
def existintree(self,root,value):#(to find a ele present in binary tree)
    if root is None:
        return False
    else:
        inleft=existintree(root.left,value)
        inright=existintree(root.right,value)
        return root.data == value or inleft or inright
def reversetree(self,root):
    if root is None:
        return 0
    else:
        reversetree(root.left)
        reversetree(root.left)
        root.left,root.right=root.right,root.left


#consecutive numbers sum
Given an integer n. return the no. of ways that u can write n as the sum
of consecutive numbers.
Input: 5
Output: 2+3=5 and 5
i.e, 2
'''
n=input()
c=1
for i in range(len(n)):
    if (i + [i+1]) ==n :
        c+=1
    print(c)


















