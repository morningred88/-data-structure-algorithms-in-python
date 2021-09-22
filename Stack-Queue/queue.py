# FIFO first item we insert is the first one we take out


class Queue:

    def __init__(self):
        self.queue = []

    # O(1) constant running time
    def is_empty(self):
        return self.queue == []

    # O(1) constant running time
    def enqueue(self, data):
        self.queue.append(data)

    # O(N) linear running time
    # Get the item value has O(1), but deletion of first item make the implementation to O(N)
    # How to solve this problem? Doubly linked list
    def dequeue(self):
        if self.size_queue() < 1:
            return -1
        data = self.queue[0]
        del self.queue[0]
        return data

    # O(1) constant running time
    def peek(self):
        return self.queue[0]

    # O(1) constant running time
    def size_queue(self):
        return len(self.queue)


queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(f'Dequeue: {queue.dequeue()}')
print(f'Queue size is {queue.size_queue()}')
print(f'Dequeue: {queue.dequeue()}')
print(f'Queue size is {queue.size_queue()}')
print(f'Dequeue: {queue.dequeue()}')
print(f'Queue size is {queue.size_queue()}')
print(f'Dequeue: {queue.dequeue()}')
print(f'Queue size is {queue.size_queue()}')
print(f'Dequeue: {queue.dequeue()}')

