'''
a=list(map(int,input().split()))
x=min(a)
m = a.index(x)
if m+1==len(a):
    a.remove(x)
    l=a[:m]
    x1=min(l)
    y=max(l)
    n=l.index(y)+m  
else:
    l=a[m:]
    y=max(l)
    n=l.index(y)+m
if m<n :
    print(y-x1)
else:
    print(0)


#Sum of array using recursion
def SA(a):
    if len(a)==0:
        return 0
    if len(a)==1:
        return a[0]
    mid=len(a)//2
    ls=SA(a[:mid])
    rs=SA(a[mid:])
    return ls+rs
a=list(map(int,input().split()))
print(SA(a))

#Palindrome
def palindrome(n):
    if len(n)==0:
        return "Yes"
    elif len(n)==1:
        return "Yes"
    else:
        if n==n[::-1]:
            return "Yes"
        else:
            return "No"
n=input()
x=palindrome(n)
print(x)


#Using Recursion
def palindrome(n):
    if len(n) == 0:
        return "Yes"  
    elif len(n) == 1:
        return "Yes"      
    # Recursive case
    if n[0].lower() == n[-1].lower():
        return palindrome(n[1:-1])
    else:
        return "No"

n = input("Enter a string: ")
x = palindrome(n)
print(x)


n=list(map(int,input().split()))
c=0
for i in range(len(n)):
    for j in range(len(n)):
        if i < j:
            if n[i]==n[j]:
                c+=1
print(c)

n = int(input())

def isprime(n, deno=2):
    if n < 2:
        return False
    if deno > int(n**0.5):
        return True
    if n % deno == 0:
        return False
    return isprime(n, deno + 1)

print(isprime(n))

#Leetcode:1051(Height Checker)
h=list(map(int,input().split()))
x=sorted(h)
c=0
for i in range(len(h)):
    if h[i]==x[i]:
        continue
    else:
        c+=1
print(c)

N < 10*9
Example 1
Input.-
20
Output;-
3
Explanation
N=20
If we list the numbers that divide 20, they are
1, 2, 4, 5, 10, 20
1 is not a square free number, 4 is a perfect square, and 20 ls
divisible by 4, a perfect square, 2 and 5, being prime, are square free,
and 10 is divisible by 1,2,5 and 10,
none of which are perfect squares, Hence the result is 3

'''


n1=list(map(int,input().split()))
n2=list(map(int,input().split()))
x=sorted(n1+n2)
print(x)
n=len(x)
if len(x) % 2==0:
    middle1 = x[n // 2 - 1]
    middle2 = x[n // 2]
    median = (middle1 + middle2) / 2
    print(median)
else:
    median = x[n // 2]
    print(median)




