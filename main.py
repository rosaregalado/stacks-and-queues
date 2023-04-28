from LinkedList import LinkedList
from LinkedListStack import LinkedListStack
from LinkedListQueue import LinkedListQueue

'''ll = LinkedList()
ll.append("A")
ll.append("B")
ll.append("C")
ll.prepend("X")
ll.prepend("Z")

ll.delete_from_head()
ll.delete_from_head()

ll.delete_from_tail()

ll.print_list()'''

#TODO: test out stack

s = LinkedListStack()
s.push('a')
s.push('b')
s.push('c')
s.pop()
print(s.peek())
s.pop()
print(s.peek())

#TODO: test out queue

q = LinkedListQueue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)

print(q.front()) # 1
print(q.dequeue()) # 1
print(q.dequeue()) # 2
print(q.front()) # 3
q.enqueue(5)
print(q.front()) # 3