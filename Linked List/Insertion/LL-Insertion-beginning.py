# Singly Linked List: Beginning Insertion


class Node(object):
    
    # A new node is always initalized with some data
    # A new node always points to None. It floats
    def __init__(self, data):
        self.data = data
        self.next = None
        

class LinkedList(object):
    
    def add