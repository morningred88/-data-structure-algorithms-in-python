class Node:
    def __init__(self, data):
        self.data = data
        self.nextNode = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.numOfNodes = 0

    # We can access the head node exclusively in LinkedList.
    # This is exactly why we like linked lists - O(1)
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

    # We need to go through all the LinkedList to add a new node - linear running time O(n)
    def insert_end(self, data):
        self.numOfNodes = self.numOfNodes + 1
        new_node = Node(data)
        # actual node starts with the head node
        actual_node = self.head
        while actual_node.nextNode is not None:
            actual_node = actual_node.nextNode

        actual_node.nextNode == new_node

    # O(N)
    def traverse_list(self):
        actual_node = self.head
        while actual_node is not None:
            print(f'traverse {actual_node.data}')
            actual_node = actual_node.nextNode

    def remove(self, data):
        if self.head is None:
            return
        actual_node = self.head
        previous_node = None

        while actual_node is not None and actual_node.data != data:
            previous_node = actual_node
            actual_node = actual_node.nextNode
        # Search miss - the item is not present in the linked list
        if actual_node is None:
            return
        if previous_node is None:
            self.head = actual_node.nextNode
        else:
            previous_node.nextNode = actual_node.nextNode


linked_list = LinkedList()
linked_list.insert_start(4)
linked_list.insert_start(3.0)
linked_list.insert_start("Adam")
linked_list.insert_start(10)
linked_list.insert_start(100)
linked_list.insert_start(1000)

linked_list.traverse_list()
print('-----------------')
linked_list.remove(10)
linked_list.traverse_list()
