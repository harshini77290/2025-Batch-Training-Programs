'''
#Input:[7 8 9 3]
#Output:3
queue=list(map(int,input().split()))
n=int(input())
while len(queue)>0:
    x=queue.pop(0)
    x=x-n
    if x>0:
        queue.append(x)
    elif len(queue)== 1:
        print(queue[0])
    #print(queue)

#Input: 3 [3 4 2] [5 3 4]
#Output: 3
n=int(input())
e=list(map(int,input().split()))
b=list(map(int,input().split()))
x=[]
for i in range(n):
    m=e[i]-b[i]
    x.append(m)
print(abs(sum(x)))

n=int(input())
e=list(map(int,input().split()))
b=list(map(int,input().split()))
x=sum(e)-sum(b)
if x <0:
    print(abs(x))
else:
    print("0")


import math
n=int(input())-1
m=int(input())-1
x=int(input())-1
y=int(input())-1
def validPath():
  total_path=math.factorial(n+m)//(math.factorial(n)*math.factorial(m))
  path_to_xy=math.factorial(x+y)//(math.factorial(x)*math.factorial(y))
  xy_to_mn=math.factorial(n-x+m-y)//(math.factorial(n-x)*math.factorial(m-y))
  return total_path-(path_to_xy*xy_to_mn)
print(validPath())
'''

class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        oddsCount = 0
        evensCount = 0
        for n in position:
            if n % 2 == 0:
                evensCount +=1
            else:
                oddsCount += 1
        return min(oddsCount, evensCount)


















