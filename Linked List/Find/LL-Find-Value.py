# Program to find a node with given "val" in the Linked List

class Node(object):
    
    def __init__(self, val):
        self.data = val
        self.next = None
    
class LinkedList(object):
    
    # Create a LL with head, tail pointers set to None
    def __init__(self):
        self.head = None
        self.tail= None 
        
    # To get the nodes at which the head/tail are currently at
    def status(self):
        if self.head = None:
            print "LL is empty"
        else:
            print "Head --> {}".format(self.head.data)
            print "Tail --> {}".format(self.tail.data)
    
    # Print the whole LinkedList
    def traverse(self):
        node = self.head
        if node ==None:
            print "LL is empty"
        else:
            while (node.next != None):
                print "{} --> ".format(node.data)
                node =  node.next
            print "{} --> |".format(node.data)
            
        
    
                