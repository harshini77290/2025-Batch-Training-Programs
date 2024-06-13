'''
Zayn purenaved an array A having N imeger values.
Alter playing it tor a while, he was bored of it and decided to update
value of is ciement, in one second he can increase value of each array
element by 1. He want each array element's value to become greater than
or equal to K. Please help Zayn to find out the minium amount of time
it will take for him to do so.


n=int(input("Enter no of cases:"))
x=1
while(x<=n):
    m,k=map(int,input().split())
    a=[list(map(int,input().split())) for j in range(m-1)]
    for i in a:
        if i<k:
            maximum=max(0,k-i)
    print(maximum)
    x+=1

t=int(input())
x=1
while(x<=t):
    n,k=map(int,input().split())
    a = [list(map(int, input().split())) for i in range(n-1)]
    mini=0
    for i in a:
        if i<k:
            mini=max(mini,k-i)
    print(mini)
    x+=1

Sandhir was into aviation industry and she was trying to check with some
take off rules, There are three planes A, B and C. Plane A will
takeoff on every pth day i.e. p, 2p, 3p and so on.Plane B will takeoff
on every qth day and plane C will takeoff on every rth day.
There Is only one runway and the takeoff timing is same for each of the
three planes on each day. Now her task is to find out the maximum number
of flights that will successfully takeoff in the period of N days.
Note: If there is collision between the flights no flight will take off
on that day.
Input Format:
The first line of the input contains a single Integer T, the number of
test cases. Then T lines follow each containing four space-separated
integers N, p, q and res denoted in the statement.
Output Format:
For each test case print a single integer representing the maximum
number of flights that will successfully takeoff in the period of N days


t=int(input("Enter no. of test cases:"))
for i in range(t):
    n,p,q,r=map(int,input().split())
    c=0
    for i in range(1,n+1):
        takeoff_count = (i % p == 0) + (i % q == 0) + (i %r == 0)
        print(takeoff_count)
        if takeoff_count == 1:
            c+=1
    print(c)
    


a=10
b=20
print(a==b)

i = 8
j = 4
p = 4
print((i % p == 0) +(j % p == 0))

if 0:
    print('Hai')
if -1:
    print('Hello')
if 1:
    print('ok')
'''

print(False + False )







