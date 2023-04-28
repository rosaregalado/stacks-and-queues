from LinkedList import LinkedList

#TODO: coomplete the methods and put their time complexities in the comments

class LinkedListStack:

  def __init__(self):
    self.ll_stack = LinkedList()

  def push(self, new_data):
    # inserts element at head of list
    self.ll_stack.prepend(new_data)

  def pop(self):
    # removes head of list
    return self.ll_stack.delete_from_head()

  def peek(self):
    if self.ll_stack.head is None:
      return None
    else:
      # returns head element without removing it
      return self.ll_stack.head.data
