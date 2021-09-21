class MaxStack:

    def __init__(self):
        # Use one stack for operation
        self.main_stack = []
        # Use another stack for the  operation
        self.max_stack = []

    # Adding an item to the  - O(1) constant time
    def push(self, data):
        self.main_stack.append(data)
        if len(self.main_stack) == 1:
            self.max_stack.append(data)
        else:
            if data < self.max_stack[-1]:
                self.max_stack.append(self.max_stack[-1])
            else:
                self.max_stack.append(data)

    # Max item is the last item we have inserted into the maxStack O(1)
    def get_max_item(self):
        return self.max_stack.pop()


# if __name__='__main__'
max_stack = MaxStack()
max_stack.push(10)
max_stack.push(5)
max_stack.push(5000)
max_stack.push(12)
max_stack.push(100)

print(max_stack.get_max_item())
