# Implement stack using list. 
stack = []

# Push
stack.append(10)
stack.append(20)
stack.append(30)

print("Stack after Push:", stack)

# Pop
item = stack.pop()
print("Popped Element:", item)

print("Stack after Pop:", stack)

# Infix to postfix conversion.
# Implement queue using list. 

queue = []

# Enqueue
queue.append(10)
queue.append(20)
queue.append(30)

print("Queue:", queue)

# Dequeue
item = queue.pop(0)

print("Dequeued Element:", item)
print("Queue after Dequeue:", queue)

# Balanced parentheses checker using stack.
# Circular queue implementation.

size = 5
queue = [None] * size
front = rear = -1

# Enqueue
for item in [10, 20, 30]:
    if (rear + 1) % size == front:
        print("Queue is Full")
    else:
        if front == -1:
            front = 0
        rear = (rear + 1) % size
        queue[rear] = item

print("Circular Queue:", queue)

# Dequeue
if front == -1:
    print("Queue is Empty")
else:
    print("Deleted Element:", queue[front])
    queue[front] = None

    if front == rear:
        front = rear = -1
    else:
        front = (front + 1) % size

print("Queue after Deletion:", queue)

# Real-world application of stack
# Undo Operation using Stack

stack = []

# User actions
stack.append("Type A")
stack.append("Type B")
stack.append("Type C")

print("Actions:", stack)

# Undo last action
undo = stack.pop()

print("Undo:", undo)
print("Remaining Actions:", stack)