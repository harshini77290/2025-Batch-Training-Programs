'''
def push_e():
    if len(s)==n:
        print("Stack is full!")
    else:
        e=input("Enter the element to insert")
        s.append(e)
        print(s)

def pop_e():
    if(s==0):
        print("Stack is empty..Add data items")
    else:        
        e=s.pop()
        print(e,"removed")
s=[]
n=int(input("Enter the size of the stack:"))
while True:
    print("Enter the operation\n1.push\n2.pop\n3.Quit")
    c=int(input())
    if c==1:
        push_e()
    elif c==2:
        pop_e()
    elif c==3:
        break
    else:
        print("Enter the correct operation:")

n = input()
s = []
for c in n:
    s.append(c)
rev= ""
while s:
    rev += s.pop()
if n == rev:
    print(f"'{n}' is a palindrome.")
else:
    print(f"'{n}' is not a palindrome.")

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
'''
def isValid(s: str) -> bool:
    bracket_map = {')': '(', '}': '{', ']': '['}
    stack = []
    for char in s:
        if char in bracket_map:
            top_element = stack.pop() if stack else '#'
            if bracket_map[char] != top_element:
                return False
        else:
            stack.append(char)
    return not stack
s = input("Enter a string containing only parentheses '()', '[]', and '{}':")
if isValid(s):
    print("True")
else:
    print("False")







    
