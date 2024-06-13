'''
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=a+b
print(c)
print(sorted(c))

d='369527184'
dlist=list(d)
print(sorted(dlist))

#Lexicographical order

n=int(input())
l=[str(i) for i in range(1,n+1)]
l.sort()
print(list(map(int,l)))


#Read list and swap frst and last element
n=input().split()
n[0],n[-1]=n[-1],n[0]
print(n)
'''

#House Problem
h=list(map(int,input().split()))
emax=sum(h[0::2])  #even house sum
omax=sum(h[1::2])  #Odd house sum
tmax=0
while(max(h)!=0):
    tmax+=max(h)
    i = h.index(max(h))
    if i==0:
        h[0],h[1]=0,0
    elif i==len(h)-1:
        h[-2],h[-1]=0,0
    else:
        h[i],h[i+1],h[i-1]=0,0,0
print(max([emax,omax,tmax]))

l=[]
for i in range(1,11):
    c=i*i*i
    if c%2==0:
        l.append(c)
print(l)
'''
#comprehension method
c=[i*i*i for i in range(1,6) if i*i*i %2==0]
print(c)



d="hello everyone"
x=d[1::2]
print(x)

x=[d[i] for i in range(len(d)) if i%2 !=0]
print(x)

res=[]
for i in range(len(d)):
    if i%2 != 0:
        res.append(d[i])

        
o=[]
for ch in d[1::2]:
    o.append(ch)
print(res)
print(o)
    
n=int(input())
nestedlist = [list(map(int,input().split())) for i in range(n)]
print(nestedlist)
maxIn,tsum = 0,0
for index,data in enumerate(nestedlist):
    if tsum< sum(data):
        tsum = sum(data)
        maxIn = index
print(maxIn)'''












