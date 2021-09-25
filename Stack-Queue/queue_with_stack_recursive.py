class QueueStackRecursive:

    def __init__(self) -> None:
        self.stack = []

    def enqueue(self, data):
        self.stack.append(data)

    def dequeue(self):
        if len(self.stack) == 1:
            return self.stack.pop()
        item = self.stack.pop()
        dequeued_item = self.dequeue()
        self.stack.append(item)
        return dequeued_item


queue = QueueStackRecursive()

queue.enqueue(10)
queue.enqueue(5)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)
queue.enqueue(50)

print(queue.dequeue())
# # queue.enqueue(100)
# print(queue.dequeue())
# print(queue.dequeue())
# # print(queue.dequeue())
