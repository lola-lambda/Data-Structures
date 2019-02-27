class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    self.storage.append(value)
    self._bubble_up(len(self.storage) - 1)
    # add to the end of the heap then bubble up to maintain the heap
   
  def delete(self):
    deleted = self.storage
    del(self.storage[0])
    # self._sift_down(0)
    return deleted
    # delete first item then sift down from the new top of the list to maintain the heap

  def get_max(self):
    return self.storage[0]
    # return the first item in the heap storage list

  def get_size(self):
    return len(self.storage)
    # return the length of the heap storage list

  def _bubble_up(self, index):
    parent_index = (index - 1) // 2
    while parent_index >= 0:
      if self.storage[index] > self.storage[parent_index]:
        child = self.storage[index]
        self.storage[index] = self.storage[parent_index]
        self.storage[parent_index] = child
        index -= 1
        self._bubble_up(index)
      else:
        break
    
    # compare child value to parent value
    # if child > parent
    # swap via their indices
    # else move to the next one
    # repeat until it reaches the right spot (no swap)

  # def _sift_down(self, index):
 
