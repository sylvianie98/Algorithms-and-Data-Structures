# TODO: Your name, Cornell NetID
# Hongyi Nie, hn327
# Please see instructions.pdf for the description of this problem.
from fixed_size_array import FixedSizeArray
from cs5112_hash import cs5112_hash

# Implementation of a node in a singlely linked list.
# DO NOT EDIT THIS CLASS
class SLLNode:
  def __init__(self, value, next_node=None):
    self.value = value
    self.next_node = next_node

  def set_next(self, node):
    self.next_node = node

  def get_next(self):
    return self.next_node

  def set_value(self, value):
    self.value = value

  def get_value(self):
    return self.value

# An implementation of a hash table that uses chaining to handle collisions.
class HashTable:
  def __init__(self, initial_size=10, load_factor=.75):
    # DO NOT EDIT THIS CONSTRUCTOR
    if (initial_size < 0) or (load_factor <= 0) or (load_factor > 1):
      raise Exception("size must be greater than zero, and load factor must be between 0 and 1")
    self.array_size = initial_size
    self.load_factor = load_factor
    self.item_count = 0
    self.array = FixedSizeArray(initial_size)

  # Inserts the `(key, value)` pair into the hash table, overwriting any value
  # previously associated with `key`.
  # Note: Neither `key` nor `value` may be None (an exception will be raised)
  def insert(self, key, value):
      # TODO: YOUR CODE HERE
      if key is None:
          raise Exception("key can not be None")
      index = cs5112_hash(key) % self.array_size
      node = self.array.get(index)
      if node is None:
          node = SLLNode((key,value),None)
          self.array.set(index,node)
          self.item_count = self.item_count + 1
      else:
          prev = node
          while node is not None:
              if node.get_value()[0] == key:
                  node.set_value((key,value))
                  if self.item_count / self.array_size > self.load_factor:
                      self._resize_array()
                  return
              if node.get_next() is not None:
                  node = node.get_next()
              else:
                  break
          self.item_count = self.item_count + 1
          self.array.set(index,SLLNode((key,value),None))
          self.array.get(index).set_next(prev)

      if self.item_count / self.array_size > self.load_factor:
          self._resize_array()

  # Returns the value associated with `key` in the hash table, or None if no
  # such value is found.
  # Note: `key` may not be None (an exception will be raised)
  def get(self, key):
    # TODO: YOUR CODE HERE
    if key is None:
      raise Exception("key can not be None")
    index = cs5112_hash(key) % self.array_size
    node = self.array.get(index)
    while node is not None:
        if node.get_value()[0] != key:
            node = node.get_next()
        else:
            return node.get_value()[1]
    return None

  # Removes the `(key, value)` pair matching the given `key` from the map, if it
  # exists. If such a pair exists in the map, the return value will be the value
  # that was removed. If no such value exists, the method will return None.
  # Note: `key` may not be None (an exception will be raised)
  def remove(self, key):
    if key is None:
      raise Exception("key can not be None")
    index = cs5112_hash(key) % self.array_size
    node = self.array.get(index)
    if node is None:
      return None
    if node.get_value()[0] == key:
      self.array.set(index, node.get_next())
      self.item_count = self.item_count - 1
      return node.get_value()[1]
    while node.get_next() is not None:
      next_node = node.get_next()
      if next_node.get_value()[0] == key:
        node.set_next(next_node.get_next())
        self.item_count = self.item_count - 1
        return node.get_value()[1]
      node = next_node
    return None

  # Returns the number of elements in the hash table.
  def size(self):
    return self.item_count

  # Internal helper function for resizing the hash table's array once the ratio
  # of stored mappings to array size exceeds the specified load factor.
  def _resize_array(self):
    new_hash_table = HashTable(self.array_size*2, self.load_factor)
    for i in range(0, self.array_size):
      node = self.array.get(i)
      if (node is not None):
        (key, value) = node.get_value()
        new_hash_table.insert(key, value)
        while (node.get_next() is not None):
          node = node.get_next()
          (key, value) = node.get_value()
          new_hash_table.insert(key, value)
    self.array_size = self.array_size*2
    self.array = new_hash_table._get_array()

  # Internal helper function for accessing the array underlying the hash table.
  def _get_array(self):
    # DO NOT EDIT THIS FUNCTION
    return self.array
