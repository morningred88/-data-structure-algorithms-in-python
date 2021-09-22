# Question: Max in a stack problem overview
# The aim is to design an algorithm that can return maximum item of a stack in O(1) running time complexity.
# We can use O(N) extra memory

class MaxStack:

    def __init__(self):
        # Use one stack for adding new item
        self.main_stack = []
        # Use another stack to get the max item
        self.max_stack = []

    # Adding an item to the  - O(1) constant time
    def push(self, data):
        # push the new item onto the stack
        self.main_stack.append(data)

        # First item is teh same in both stacks
        if len(self.main_stack) == 1:
            self.max_stack.append(data)
        else:
            # If the new item smaller than the largest one so far,
            # then we duplicate the largest one on the max-stack
            if data < self.max_stack[-1]:
                self.max_stack.append(self.max_stack[-1])
            # If the item is the largest one so far, we insert it onto the stack
            else:
                self.max_stack.append(data)

    # Max item is the last item we have inserted into the maxStack O(1)
    def get_max_item(self):
        return self.max_stack.pop()


max_stack = MaxStack()
max_stack.push(10)
max_stack.push(5)
max_stack.push(5000)
max_stack.push(12)
max_stack.push(100)

print(max_stack.get_max_item())
