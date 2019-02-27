"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
  def __init__(self, value, prev=None, next=None):
    self.value = value
    self.prev = prev
    self.next = next

  """Wrap the given value in a ListNode and insert it
  after this node. Note that this node could already
  have a next node it is point to."""
  def insert_after(self, value):
    current_next = self.next
    self.next = ListNode(value, self, current_next)
    if current_next:
      current_next.prev = self.next

  """Wrap the given value in a ListNode and insert it
  before this node. Note that this node could already
  have a previous node it is point to."""
  def insert_before(self, value):
    current_prev = self.prev
    self.prev = ListNode(value, current_prev, self)
    if current_prev:
      current_prev.next = self.prev

  """Rearranges this ListNode's previous and next pointers
  accordingly, effectively deleting this ListNode."""
  def delete(self):
    if self.prev:
      self.prev.next = self.next
    if self.next:
      self.next.prev = self.prev

"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
  def __init__(self, node=None):
    self.head = node
    self.tail = node

  def add_to_head(self, value):
    if self.head:
      prevHead = self.head
      self.head = ListNode(value, prev=None, next=prevHead)
    else:
      self.head = ListNode(value, prev=None, next=None)

  def remove_from_head(self):
    if self.head:
      removed = self.head.value
      self.head.delete()
      return removed
    else:
      return None
      
  def add_to_tail(self, value):
    if self.tail:
      prevTail = self.tail
      self.tail = ListNode(value, prev=prevTail, next=None)
    else:
      self.tail = ListNode(value, prev=None, next=None)

  def remove_from_tail(self):
    if self.tail:
      removed = self.tail.value
      self.tail.delete()
      return removed
    else:
      return None

  def move_to_front(self, node):
    node.delete()
    self.add_to_head(node.value)

  def move_to_end(self, node):
    node.delete()
    self.add_to_tail(node.value)

  # def delete(self, node):
  #   prev_node = node.prev
  #   next_node = node.next
  #   prev_node.next = next_node
  #   next_node.prev = prev_node
    
  def get_max(self):
    cur_node = self.head
    max_val = 0
    while True:
      if not cur_node:
        return None
      if cur_node.value > max_val:
        max_val = cur_node.value
      if cur_node.next is None:
        return max_val
      else:
        cur_node = cur_node.next      
