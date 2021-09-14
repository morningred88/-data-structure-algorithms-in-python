"""
Question 7: Finding the middle node in a linked list

Suppose we have a standard linked list. Construct an in-place (without extra momory) algorithm thats able to find the middle node!
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.nextNode = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.numOfNodes = 0

    # O(N/2), so O(N) linear running time complexity
    def getMiddleNode(self):
        fastPointer = self.head
        slowPointer = self.head

        while fastPointer.nextNode and fastPointer.nextNode.nextNode:
            fastPointer = fastPointer.nextNode.nextNode
            slowPointer = slowPointer.nextNode

        return slowPointer

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


if __name__ == '__main__':
    testLinkedList = LinkedList()
    testLinkedList.insert_start(1)
    testLinkedList.insert_start(2)
    testLinkedList.insert_start(3)
    testLinkedList.insert_start(4)
    testLinkedList.insert_start(5)
    print(testLinkedList.getMiddleNode().data)
