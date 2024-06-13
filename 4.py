'''
#Pgm to print sum of all odd numbers present in a largest number.

n=int(input())
totSum=0
while n !=0:
  rem=n%10
  if rem%2!=0:
    totSum+=rem
  n//= 10  
print(totSum)


# Prgnm to sort first half in ascending order ans second half
#in descending order in an array.
#Input: 4 2 5 8 7 3
#Output: 2 3 4 8 7 5

n=int(input("Enter length of array"))
m=list(map(int,input().split()))
mid=n//2
l1=m[:mid]
l2=m[mid:]
l1.sort()
l2.sort(reverse=True)
res=l1+l2
print(res)


The police department of your city has just started its journey. Initially, they don’t have any manpower. So, they started hiring new recruits in groups.

Meanwhile, crimes keeps occurring within the city. One member of the police force can investigate only one crime during his/her lifetime.

If there is no police officer free (isn't busy with crime) during the occurrence of a crime, it will go untreated.

Given the chronological order of crime occurrences and recruit hirings, find the number of crimes which will go untreated.

Input
The first line of input will contain an integer n (1 ≤ n ≤ 105), the number of events. The next line will contain n space-separated integers.

If the integer is -1 then it means a crime has occurred. Otherwise, the integer will be positive, the number of officers recruited together at that time. No more than 10 officers will be recruited at a time.

Output
Print a single integer, the number of crimes which will go untreated.

Soulution
def crimes(n, events):
    o = 0
    uc = 0
    
    for e in events:
        if e == -1:
            if o > 0:
                o -= 1
            else:
                uc += 1
        else:
            o += e
    
    return uc



n = int(input())
events = list(map(int, input().split()))
result = crimes(n, events)
print(result)


One hot summer day Pete and his friend Billy decided to buy a watermelon. They chose the biggest and the ripest one, in their opinion. After that the watermelon was weighed, and the scales showed w kilos. They rushed home, dying of thirst, and decided to divide the berry, however they faced a hard problem.

Pete and Billy are great fans of even numbers, that's why they want to divide the watermelon in such a way that each of the two parts weighs even number of kilos, at the same time it is not obligatory that the parts are equal. The boys are extremely tired and want to start their meal as soon as possible, that's why you should help them and find out, if they can divide the watermelon in the way they want. For sure, each of them should get a part of positive weight.

Input
The first (and the only) input line contains integer number w (1 ≤ w ≤ 100) — the weight of the watermelon bought by the boys.

Output
Print YES, if the boys can divide the watermelon into two parts, each of them weighing even number of kilos; and NO in the opposite case.


#solution
def watermelon(w):
    if w % 2 == 0 and w >= 4:
        return "YES"
    else:
        return "NO"

w = int(input())
print(watermelon(w))
'''

def reverse(s):
    a= [char for char in s if char.isalnum()]
    a.reverse()
    
    result = []
    alnum_index = 0
    
    for char in s:
        if char.isalnum():
            result.append(alnum_chars[alnum_index])
            alnum_index += 1
        else:
            result.append(char)
    
    return ''.join(result)

input_str = input("Enter a string: ")
output_str = reverse(input_str)
   print("Reversed string with special characters retained:", output_str)























                                    
