from LinkedList import LinkedList
#TODO: coomplete the methods and put their time complexities in the comments
class LinkedListQueue:

  def __init__(self):
    self.ll_queue = LinkedList()

  def enqueue(self, new_data):
    self.ll_queue.append(new_data)

  def dequeue(self):
    # check if queue is empty
    if self.ll_queue.head is None:
      return None
    else:
      # delete node at front of the queue
      front = self.ll_queue.head.data
      self.ll_queue.delete_from_head()
      return front

  def front(self):
    # check if queue is empty
    if self.ll_queue.head is None:
      return None
    else: 
      # return data of head node in the queue
      return self.ll_queue.head.data