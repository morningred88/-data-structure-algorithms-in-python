# LIFO:last item we insert is the first item we take out

class Stack():
  
  # Use one dimensional array as underlying data structure
  def __init__(self):
    self.stack = []
  
  # Insert item into the stack //O(1)
  def push(self, data):
    self.stack.append(data)
  
  # remove and return the last item we have insert (LIFO) //O(1)
  def pop(self):
    if self.stack_size() <1:
      return -1

    data = self.stack[-1]
    del self.stack[-1]
    return data
  
  # Get the value of last added item without removing it //O(1)
  def peek(self):
    return self.stack[-1]
  
  # has 0(1) running time
  def is_empty(self):
    return self.stack == []
  
  def stack_size(self):
    return len(self.stack)


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(f'Stack size: {stack.stack_size()}')
print(f'Popped item: {stack.pop()}')
print(f'Stack size: {stack.stack_size()}')
print(f'Peeked item: {stack.peek()}')
print(f'Stack size: {stack.stack_size()}')
print(f'Popped item: {stack.pop()}')
print(f'Popped item: {stack.pop()}')
print(f'Popped item: {stack.pop()}')
print(f'Popped item: {stack.pop()}')


# Result:
# Stack size: 3
# Popped item: 3
# Stack size: 2
# Peeked item: 2
# Stack size: 2
# Popped item: 2
# Popped item: 1
# Popped item: -1
# Popped item: -1


  
    

  

