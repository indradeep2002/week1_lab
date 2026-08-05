# Create singly linked list.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)

temp = head
while temp:
    print(temp.data, end=" -> ")
    temp = temp.next
print("None")

# Insert and delete nodes in linked list.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)

# Insert at beginning
new_node = Node(5)
new_node.next = head
head = new_node

# Delete node with value 20
temp = head
while temp.next:
    if temp.next.data == 20:
        temp.next = temp.next.next
        break
    temp = temp.next

# Display
temp = head
while temp:
    print(temp.data, end=" -> ")
    temp = temp.next
print("None") 
# Reverse a linked list.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)

prev = None
current = head

while current:
    next_node = current.next
    current.next = prev
    prev = current
    current = next_node

head = prev

temp = head
while temp:
    print(temp.data, end=" -> ")
    temp = temp.next
print("None")

# Detect loop in linked list.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = head.next   

slow = head
fast = head

loop = False

while fast and fast.next:
    slow = slow.next
    fast = fast.next.next

    if slow == fast:
        loop = True
        break

if loop:
    print("Loop Detected")
else:
    print("No Loop") 
# Merge two sorted linked lists.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def print_list(head):
    while head:
        print(head.data, end=" ")
        head = head.next

a = Node(1)
a.next = Node(3)
a.next.next = Node(5)

b = Node(2)
b.next = Node(4)
b.next.next = Node(6)

dummy = Node(0)
tail = dummy

while a and b:
    if a.data < b.data:
        tail.next = a
        a = a.next
    else:
        tail.next = b
        b = b.next
    tail = tail.next

tail.next = a if a else b

print("Merged List:")
print_list(dummy.next)

# Implement doubly linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

head = Node(10)
second = Node(20)
third = Node(30)

head.next = second
second.prev = head

second.next = third
third.prev = second

temp = head

print("Doubly Linked List:")
while temp:
    print(temp.data, end=" <-> ")
    temp = temp.next

print("None")