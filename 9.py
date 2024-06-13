Little Petya very much likes gifts. Recently he has received a new laptop as a New Year gift from his mother. He immediately decided to give it to somebody else as what can be more pleasant than giving somebody gifts. And on this occasion he organized a New Year party at his place and invited n his friends there.

If there's one thing Petya likes more that receiving gifts, that's watching others giving gifts to somebody else. Thus, he safely hid the laptop until the next New Year and made up his mind to watch his friends exchanging gifts while he does not participate in the process. He numbered all his friends with integers from 1 to n. Petya remembered that a friend number i gave a gift to a friend number pi. He also remembered that each of his friends received exactly one gift.

Now Petya wants to know for each friend i the number of a friend who has given him a gift.

Input
The first line contains one integer n (1 ≤ n ≤ 100) — the quantity of friends Petya invited to the party. The second line contains n space-separated integers: the i-th number is pi — the number of a friend who gave a gift to friend number i. It is guaranteed that each friend received exactly one gift. It is possible that some friends do not share Petya's ideas of giving gifts to somebody else. Those friends gave the gifts to themselves.

Output
Print n space-separated integers: the i-th number should equal the number of the friend who gave a gift to friend number i.

n = int(input())
p = list(map(int, input().split()))
j = [0]*n
for i in range(n):
    k = p[i]
    j[k - 1] = i+ 1
print(" ".join(map(str,j)))

n=int(input())
x = list(map(int, input().split()))
for i in range(1,n+1):
    #r=x.index(i)
    #print(r)
    #y=sorted(x,key=index)
    y =sorted(x, key=lambda item: i.index(item))

n = int(input())
x = list(map(int, input().split()))

g = [ ] * n

for i in range(n):
    r = x[i] - 1  # Convert 1-based index to 0-based index
    g[r] = i + 1  # Store the giver's number (1-based)

print(' '.join(map(str, g)))

n, t = map(int, input().split())
for _ in range(n):
    x = input()
    l = list(x)
    for _ in range(t):
        i = 0
        while i < len(l) - 1:
            if l[i] == 'B' and l[i + 1] == 'G':
                l[i], l[i + 1] = l[i + 1], l[i]
                i += 1  
            i += 1
    print(''.join(l))


Input
The first line contains two integers m, R (1 ≤ m ≤ 105, 1 ≤ R ≤ 10).
Output
In a single line print a single real number — the answer to the problem.
The answer will be considered correct if its absolute or relative error
doesn't exceed 10 - 6.
Example
input
1 1
output
2.0000000000

m,r=map(int,input().split())
answer = (m*(m+1)*(m+2)/3-m)*2
answer+=(2.0*0.5-2)((m*m-m)+(m*m-m-(m-1)*2))
answer/=(m**2)
answer*=r
print("{:.10f}".format(round(answer,10)))


The end of the school year is near and Ms. Manana, the teacher, will soon have to say goodbye to a yet another class. She decided to prepare a goodbye present for her n students and give each of them a jigsaw puzzle (which, as wikipedia states, is a tiling puzzle that requires the assembly of numerous small, often oddly shaped, interlocking and tessellating pieces).

The shop assistant told the teacher that there are m puzzles in the shop, but they might differ in difficulty and size. Specifically, the first jigsaw puzzle consists of f1 pieces, the second one consists of f2 pieces and so on.

Ms. Manana doesn't want to upset the children, so she decided that the difference between the numbers of pieces in her presents must be as small as possible. Let A be the number of pieces in the largest puzzle that the teacher buys and B be the number of pieces in the smallest such puzzle. She wants to choose such n puzzles that A - B is minimum possible. Help the teacher and find the least possible value of A - B.

Input
The first line contains space-separated integers n and m (2 ≤ n ≤ m ≤ 50). The second line contains m space-separated integers f1, f2, ..., fm (4 ≤ fi ≤ 1000) — the quantities of pieces in the puzzles sold in the shop.

Output
Print a single integer — the least possible difference the teacher can obtain.

Examples
inputCopy
4 6
10 12 10 7 5 22
outputCopy
5


n,m=map(int,input().split())
f=list(map(int,input().split()))
print(abs(min(f[:n])-max(f[:n])))


n,m=map(int,input().split())
pieces=sorted(map(int,input().split()))
min_diff=float('inf')
for i in range(n-1,m):
    diff=pieces[i]-pieces[i-n+1]
    if diff<min_diff:
        min_diff=diff
print(min_diff)



Haiku is a genre of Japanese traditional poetry.

A haiku poem consists of 17 syllables split into three phrases, containing 5, 7 and 5 syllables correspondingly (the first phrase should contain exactly 5 syllables, the second phrase should contain exactly 7 syllables, and the third phrase should contain exactly 5 syllables). A haiku masterpiece contains a description of a moment in those three phrases. Every word is important in a small poem, which is why haiku are rich with symbols. Each word has a special meaning, a special role. The main principle of haiku is to say much using a few words.

To simplify the matter, in the given problem we will consider that the number of syllable in the phrase is equal to the number of vowel letters there. Only the following letters are regarded as vowel letters: "a", "e", "i", "o" and "u".

Three phases from a certain poem are given. Determine whether it is haiku or not.

Input
The input data consists of three lines. The length of each line is between 1 and 100, inclusive. The i-th line contains the i-th phrase of the poem. Each phrase consists of one or more words, which are separated by one or more spaces. A word is a non-empty sequence of lowercase Latin letters. Leading and/or trailing spaces in phrases are allowed. Every phrase has at least one non-space character. See the example for clarification.

Output
Print "YES" (without the quotes) if the poem is a haiku. Otherwise, print "NO" (also without the quotes).

Examples
inputCopy
on  codeforces 
beta round is running
   a rustling of keys 
outputCopy
YES
inputCopy
how many gallons
of edo s rain did you drink
                                cuckoo
outputCopy
NO



phrase1=input()
phrase2=input()
phrase3=input()
vowels=['a','e','i','o','u']
haiku=[5,7,5]
res=[]
for i in(p1,p2,p3):
    count=0
    for c in i:
        if c in vowels:
            count+=1
    res.append(count)
if res==haiku:
    print('Yes')
else:
    print('No')



h='aeiou'
n=input("Enter phrase 1:")
n2=input("Enter phrase 2:")
n3=input("Enter phrase 3:")
c=0
for i in range(len(n)):
    if n[i] in h:
        c+=1
c2=0
for i in range(len(n2)):
    if n2[i] in h:
        c2+=1
c3=0
for i in range(len(n3)):
    if n3[i] in h:
        c3+=1
if c==5 and c2== 7 and c3== 5:
    print("YES")
else:
    print("NO")



def is_haiku(phrase1,phrase2,phrase3):
    vowels="aeiou"
    counts=[0,0,0]
    for i,phrase in enumerate([phrase1,phrase2,phrase3]):
        for char in phrase:
            if char in vowels:
                counts[i]+=1
    if counts==[5,7,5]:
        return "YES"
    else:
        return "NO"
phrase1=input().strip()
phrase2=input().strip()
phrase3=input().strip()
print(is_haiku(phrase1,phrase2,phrase3))
