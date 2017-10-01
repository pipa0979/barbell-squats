# Program to find a node with given "val" in the Linked List
from random import *

class Node(object):
    
    def __init__(self, val):
        self.data = val
        self.next = None
    
class LinkedList(object):
    
    # Create a LL with head, tail pointers set to None
    def __init__(self):
        self.head = None
        self.tail= None 
     
    def isEmpty(self):
        if self.head == None:
            return True
        else:
            return False
        
        
    # To get the nodes at which the head/tail are currently at
    def status(self):
        if self.isEmpty():
            print "LL is empty"
        else:
            print "Head --> {}".format(self.head.data)
            print "Tail --> {}".format(self.tail.data)
    
    # Print the whole LinkedList
    def traverse(self):
        if self.isEmpty():
            print "LL is empty"
        else:
            node = self.head
            while (node.next != None):
                print "{} --> ".format(node.data),
                node =  node.next
            print "{} --> |".format(node.data)

    
    def addBeg(self, val):
        new_node = Node(val)
        if self.isEmpty():
            self.head = new_node
            self.tail = new_node
            self.head.next = None
            return True
        else:
            new_node.next = self.head
            self.head = new_node
            return True
        return False
    
    # To check if "value" exists and then return it
    def find(self, value):
        if self.isEmpty():
            return False
        else:
            node = self.head
            while node.next != None:
                if node.data == value:
                    return True
                node = node.next
            return False
        
        
LL = LinkedList()
LL.traverse()

for each in xrange(1,10):
    if LL.addBeg(each):
        print "{} added".format(each)
    else:
        print "{} not added".format(each)
LL.status()
LL.traverse()

f = randint(1,30)
print "to find {}".format(f)
if LL.find(f):
    print "{} found in LL".format(f)
else:
    print "{} not found in LL".format(f)
