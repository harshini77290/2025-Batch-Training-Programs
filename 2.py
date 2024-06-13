'''
#problem 1:checking if the number is prime or not
#n=int(input())
flag = 0
if n==1:
    print("not a prime")
elif n>1:
    for i in range(2,n):
        if n%i==0:
            flag+=1

    if flag == 2:
        print("prime")
    else:
        print("not prime")

#2
for i in range(2,n):
    if n%i==0:
        print("not prime")
        break
else:
    print("prime")
    
#3-->O(n/2)

n = int(input("Enter a number: "))

for i in range(2, (n // 2) + 1):
    if n % i == 0:
        print("not prime")
        break
else:
    print("prime")

#4
n = int(input("Enter a number: "))

for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
        print("not prime")
        break
else:
    print("prime")


#2 : Given a number. Return True if it is power of 6 else false

n=int(input())
if n <= 0:
    print(False)
else:
    while n % 6 == 0:
        n //= 6
    if n == 1:
        print(True)
    else:
        print(False)

# 3: Recursion(n to 1)        
def rec(n):
    if n<=0:
        return
    print(n)
    rec(n-1)  
n=int(input())
rec(n)


# 1 to n
def rec(c,n):
    if c>n:
        return
    print(c,end=" ")
    rec(c+1,n)  
n=int(input())
rec(1,n)


# Return a given string using recursion
def rev(s):
    if s==" ":
        return
    print(s[1:])

s=str(input())
rev(s)

#if data is number or not
import string
strNum=input()
for i in strNum:
  if i not in string.digits:
    print("False")
    break
else:
  print("True")


#123av45b78 -> 1234578->int
import string
st="123av45b78"
for i in st:
    if i in string.digits:
        print(int(i),end="")


# Program to remove all the consecutive duplicates from a given tring.
s=str(input())
for i in s:
    if s[i]==s[i+
printt(s)


# Rotate a given String in the specified direction by specified magnitude.
After each rotation make a note of the first character of the rotated String,
After all rotation are performed the accumulated first character as noted
previously will form another string, say FIRSTCHARSTRING.
Check If FIRSTCHARSTRING is an Anagram of any substring of the Originalstring.
If yes print "YES" otherwise"NO".
Input: The first line contains the original string s.
The second line contains a single integer q.
The ith of the next q lines contains character d[i] denoting direction
and integer rill denoting the magnitude.
Constraints: 1 <= Length of original string <= 30
1<= q <= 10
Output: YES or NO
Input: carrace 3 L 2 R 2 L 3
Output:NO
'''


data=input()
rot = int(input())
res=''
for i in range(rot):
    di,mag=input().split()
    if di.upper()=='L':
        res += (data[int(mag):]+data[:int(mag)])[0]
    elif di.upper()=='R':
        res += (data[:int(mag)]+data[int(mag):])[0]
subList = [data[i:i+rot] for i in range(len(data))]
#anagram
for subele in subList:
    if sorted(subele) == sorted(res):
        print("Yes")
        break
else:
    print("NO")














        
