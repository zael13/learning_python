class Node:
   def __init__(self, dataval=None):
      self.val = dataval
      self.next = None


x = Node(1)
x.next = Node(2)
x.next.next = Node(3)
x.next.next.next = Node(4)


cur = x
prev = None

while cur:
   tmp = cur.next
   cur.next = prev
   prev = cur
   cur = tmp


print(prev.next.next.next.val)