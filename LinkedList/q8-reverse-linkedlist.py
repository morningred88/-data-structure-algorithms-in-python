# Q8: Construct an in-place algorithm to reverse a linked list!

class Node():
    def __init__(self, data):
        self.data = data
        self.nextNode = None


class LinkedList():
    def __init__(self):
        self.head = None
        self.numOfNodes = 0

    def insert_start(self, data):
        self.numOfNodes = self.numOfNodes + 1
        # Instantiate the new node
        new_node = Node(data)

        # If it is an empty linkedList, then the head node will be the new node
        if not self.head:
            self.head = new_node
        # If the linkedlist is not empty, then we need to update the references,
        # the current head node will be next node, the new node will become the head node
        else:
            new_node.nextNode = self.head
            self.head = new_node

        # Add print for debugging purpose
        # print(f'Insert head node with data: {self.head.data}')

    def traverse_list(self):
        actual_node = self.head
        while actual_node is not None:
            print(f'traverse {actual_node.data}')
            actual_node = actual_node.nextNode

    def reverse_linked_list(self):
        current_node = self.head
        previous_node = None
        next_node = None

        while current_node is not None:
            next_node = current_node.nextNode
            current_node.nextNode = previous_node
            previous_node = current_node
            current_node = next_node
        self.head = previous_node


if __name__ == '__main__':
    testLinkedList = LinkedList()
    testLinkedList.insert_start(1)
    testLinkedList.insert_start(2)
    testLinkedList.insert_start(3)
    testLinkedList.insert_start(4)
    testLinkedList.insert_start(5)
    testLinkedList.traverse_list()
    testLinkedList.reverse_linked_list()
    print('Reversed list')
    testLinkedList.traverse_list()
