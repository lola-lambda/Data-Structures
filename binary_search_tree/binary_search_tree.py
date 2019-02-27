class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    if value < self.value:
      if self.left:
        self.left.insert(value)
      else:
        self.left = BinarySearchTree(value)
    if value > self.value:
      if self.right:
        self.right.insert(value)
      else:
        self.right = BinarySearchTree(value)
   
  def contains(self, target):
    if target is self.value:
      return True
    elif target < self.value:
      if self.left:
        return self.left.contains(target)
      else:
        return False
    elif target > self.value:
      if self.right:
        return self.right.contains(target)
      else:
        return False
    
  def get_max(self):
    if self.right:
      return self.right.get_max()
    else:
      return self.value
