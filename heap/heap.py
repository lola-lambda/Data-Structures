class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    self.storage.append(value)
    self._bubble_up(len(self.storage) - 1)
    # add to the end of the heap then bubble up to maintain the heap
   
  def delete(self):
    removed = self.storage[0]
    self.storage[0] = self.storage[len(self.storage) - 1]
    del self.storage[len(self.storage) - 1]
    self._sift_down(0)
    return removed
    # delete first item then sift down from the new top of the list to maintain the heap

  def get_max(self):
    return self.storage[0]
    # return the first item in the heap storage list

  def get_size(self):
    return len(self.storage)
    # return the length of the heap storage list

  def _bubble_up(self, index):
    while (index - 1) // 2 >= 0:
      parent_index = (index - 1) // 2
      if self.storage[index] > self.storage[parent_index]:
        self.storage[index], self.storage[parent_index] = self.storage[parent_index], self.storage[index]
      index = parent_index
    # if child > parent, swap
    # set new index to parent index
    # repeat until it reaches the right spot (no swap)

  def _sift_down(self, index):
    while index * 2 + 1 <= len(self.storage) - 1:
      left_child = index * 2 + 1
      right_child = index * 2 + 2
      if right_child > len(self.storage) - 1 or self.storage[left_child] > self.storage[right_child]:
        big_child = left_child
      else:
        big_child = right_child
      if self.storage[index] < self.storage[big_child]:
        self.storage[index], self.storage[big_child] = self.storage[big_child], self.storage[index]
        index = big_child
      else:
        break
    # until there are either no more left children or the sifting is complete, loop through
    # set the left & right child indices
    # let the big child = the left child if the left child value exceeds the right child's or there is no right child
    # otherwise the big child is the right one
    # then if the parent is smaller than the biggest child, swap them, and let the current index be that of the big child (post swap)
    # if the parent is not bigger than the child then it has found its place and sifting is complete