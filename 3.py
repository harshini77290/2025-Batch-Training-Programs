'''
#Objects and classes
class stu:
    roll=2167
    name='Harshini'
    phn=7729021537
    add='Warangal'

    def display(self):
        print('Name:',self.name,'Roll no:',self.roll)
s1=stu()
s1.display()


#init constructor - Method / constructor used to initialise an attribute

class stu:
    def __init__(self,roll,name,phn,add):
        self.roll=roll
        self.name=name
        self.phn=phn
        self.add=add

    def display(self):
        print('Name:',self.name,'Roll no:',self.roll)
s1=stu(2167,'Harshu',7729015294,'WGL')
s1.display()


class stu:
    def __init__(self,roll,name,phn,add):
        self.roll=roll
        self.name=name
        self.phn=phn
        self.add=add

    def display(self):
        print('Name:',self.name,'Roll no:',self.roll,'Phone:',self.phn,'Address:',self.add)
s1=stu(2167,'Harshu',7729015294,'WGL')
s2=stu(2118,'Ash',9381298674,'SBI')
s3=stu(2167,'Siri',7532977290,'GPL')
s1.display()
s2.display()
s3.display()


class test:
    def __init__(self,a='Je taime'):
        self.a=a

    def dis(self):
        print(self.a)

x=test()
x.dis()


#py pgrm to get a list, sorted in increasing order by last element in each tuple from the given list of tuples.

def last(t):
    return t[-1]

n = int(input("Enter the no of tuples: "))

t= []
for _ in range(n):
    e = tuple(map(int, input("Enter the elements of the tuple : ").split()))
    t.append(e)

t_sort= sorted(t, key=last)

print("Sorted list of tuples:", t_sort)


#py pgrm to get a list, sorted in length of the string  

s=list(map(str,input().split()))
t= []
for i in range(0,len(s)):
    t.append(s[i])

t_sort= sorted(t, key=len)

print("Sorted list of tuples:", t_sort)


class Test:
    def _init_(self):
        self.x=0
class Derived_Test(Test):
    def _init_(self):
        Test._init_(self)
        self.y=0
def main():
    b=Derived_Test()
    print(b.x,b.y)
main()


class A:
    n=10
    def _init_(self,z,y=5):
        self.zee = z
        self.yee=y
    def disp(self):
        print(self.zee,self.n)
class B(A):
    def _init_(self,m,x,p):
        #A._init_(self,x,p)
        super()._init_(x,p)
        self.my =m
    def p(self):
        print(A.n,super().n)

obj= B(10,15,21)
obj.disp()
obj.p()

class A:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __str__(self):
        return 1
    def __eg__(self,other):
        return self.x *self.y==other.x*other.y

o1=A(5,2)
o2=A(2,5)
print(o1=o2)
'''
      

def isprime(num):
    if num==0 or num==1:
        return False
    for deno in range(2,int(num**0.5)+1):
        if num%deno==0:
            return False
    return True
num=int(input())
primeList=[i for i in range(2,num+1) if isprime(i)]
count,pSum=0,primeList[0]
for p in primeList[1:]:
    pSum+=p
    if pSum>num:
        break
    if isprime(pSum):
        count+=1
print(count)







