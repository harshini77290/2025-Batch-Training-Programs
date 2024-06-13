'''
Head recursion
If a recursion has code statements to be executed after function call
then it is a Head recursion.
Head recursions are generally hard to convert into loop statements.
Example:
    void fun(int n)
    {
    if(n==0)
        return 0;

    fun(n-1);
    printf("%d", n); // Post recursive operation
    }

Tail recursion
Tail recursions will not have any code statements after function calls
and are generally at the end of the function declaration.
Tail recursions are easy to convert into loop statements.

Example:
    void fun(int n) {
        if(n==0)
            return 0;

        printf("%d", n); 
        fun(n-1);
    }


Problem Statement No.08:

kth Largest factor of N

Question: A positive integer d is said to be a factor of another
positive integer N if when N is divided by d, the remainder obtained is
zero. For example, for number 12, there are 6factors 1, 2, 3, 4, 6, 12.
Every positive integer k has at least two factors, 1 and the number k
itself. Given two positive integers N and k, write a program to print
the kth largest factor of N.

Input Format: The input is a comma-separated list of positive integer
pairs (N, k).

Output Format: The kth highest factor of N. If N does not have k factors,
the output should be 1.

N,k=map(int,input().split())
for deno in range(N,0,-1):
    if N%deno==0:
        k-=1
    if k==0:
        print(deno)
        break
if k!=0:
    print("1")


def rec(n,k,i):
    if i==0:
        return 1
    if n % i==0:
        k-=1
        if k==0:
            return i
    return rec(n,k,i-1)
n,k=map(int,input().split())
r=rec(n,k,n)
print(r)


if in format-[int,float,int,float] return True else False

m=list(input().split())
c=[]
a=[]
for i in range(len(m)):
    if i%2==0:
        r=m[i].isdigit()
        c.append(r)
    else:
        t=m[i].isdigit()
        a.append(t)

if all(c) and not any(a):
    print("True")
else:
    print("False")


Mani is given an n-by-n matrix of O's and 1's where all 1's in each
row come before all O s, his task is to find the most efficient way
to return the row with the maximum number of O's.

Input:

First line of input contains a single integer T which denotes the
number of test cases. First line of each test case contains a single
integer N which represents a size of matrix and next matrix elements.

Output:
For each test case, print the row number

Example:
Input:
1
{{1,1,1,1), (1,1,0,0), (1,0,0,0), (1,1,0,0));
Output:
2

t=int(input("Enter test cases:"))
for _  in range(1,t+1):
    n= int(input("Enter size of matrix"))
    m = []
    for _ in range(rows):
        row = list(map(int, input().split()))
        m.append(row)

    for row in m:
        print(row)
    s =sum(m[0])
    a = []

    for row in m:
        r = sum(row)
        if r < s:
            a = row
    print(a)

for i in range(int(input())):
    nestList=list(map(int,input().split()))
    n=len(nestList)
    nestList=[nestList]
    for i in range(n-1):
        nestList.append(list(map(int,input().split())))
        mcount=0
        for i in range(n):
            if mcount<nestList[i].count(0):
                mcount=nestList[i].count(0)
                index=i
                print(index)


s=list(map(int,input().split()))
for i in range(len(s)):  
    s1=max(s)
    s.remove(s1)
    s2=max(s)
    s.remove(s2)
    print(s)
    if s1!=s2:
        x=s1-s2
        s.append(x)
    if len(s)==1:
        break

class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        while len(stones) > 1:
            m1 = max(stones)
            stones.remove(m1)
            m2 = max(stones)
            stones.remove(m2)
            if m1 != m2:
                stones.append(m1 - m2)
        return stones[0] if stones else 0
'''
l=list(map(int,input().split()))
c=0
c1=[]
for i in range(len(l)):
    for j in range(len(l)):
        if l[i]==l[j+1]:
            c+=1
print(c)        
    





