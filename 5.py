
'''Ann has recently started commuting by subway.
We know that a one ride subway ticket costs a rubles.
Ann found out that she can buy a special ticket for m rides (she can buy it several times). It costs b rubles. Ann did the math; she will need to use subway n times. Help Ann, tell her what is the minimum sum of money she will have to spend to make n rides?

Input
The single line contains four space-separated integers n, m, a, b (1 ≤ n, m, a, b ≤ 1000) — the number of rides Ann has planned, the number of rides covered by the m ride ticket, the price of a one ride ticket and the price of an m ride ticket.

Output
Print a single integer — the minimum sum in rubles that Ann will need to spend.

def minimum_cost(n, m, a, b):
    sin= n * a
    
    full= n // m
    left= n % m
    cost_com= full * b + left * a
    
    cost_all= (full + 1) * b
    
    return min(sin, cost_com, cost_all)

n, m, a, b = map(int, input().split())

print(minimum_cost(n, m, a, b))


n,m,a,b=list(map(int,input().split()))
if m*a<=b:
    print(n*a)
else:
    print((n//m)*b + min((n%m)*a,b))


#Given 2 numbers as input. Add and put as linked list
n=int(input())
m=int(input())
s=n+m
print(s)

'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

def number_to_linked_list(number):
    linked_list = LinkedList()
    for digit in str(number):
        linked_list.append(int(digit))
    return linked_list

# Example usage
m=int(input())
n=int(input())
number = m+n
linked_list = number_to_linked_list(number)
linked_list.display()

