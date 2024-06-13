'''from collections import Counter
s=input()
c=Counter(s)
print(c)
for i in c.values():
    print(i)

a,b=map(int,input().split())
a=a-b
b=a+b
a=b-a
print(a,b,end=" ")

n = list(map(int, input().split()))
a = []
b=[]
c=[]
a.append(0)
b.append(0)

for i in range(len(n) - 1):
    a.append(n[i] + a[i])

x=n[::-1]
for i in range(len(n) - 1):
    b.append(x[i] + b[i])
b=b[::-1]
for i in range(len(n)):
    c.append(abs(a[i]-b[i]))
print(c)
'''

a = list(map(int, input().split()))
for i in range(len(a)):
    for j in range(len(a)):
        if i+1<j:
            if a[i]+a[i+1]==a[i+1]+a[i+2]==a[j]+a[j+1]:
                print("True")
                break
            else:
                print("False")
                break
