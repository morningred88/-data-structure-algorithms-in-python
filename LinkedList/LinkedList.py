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
        # If the linkedlist is not empty, then we need to update the references, the current head node will be next node, the new node will become the head node
        else:
            new_node.nextNode = self.head
            self.head = new_node

    # We need to go through all the LinkedList to add a new node - linear running time O(n)
    def insert_end(self, data):
        self.numOfNodes = self.numOfNodes + 1
        new_node = node(data)
        # actual node starts with the head node
        actual_node = self.head
        while actual_node.nextNode is not None:
            actual_node = actual_node.nextNode

        actual_node.nextNode == new_node
