# Program to play around. 

import random

class Node(object):
    
    def __init__(self, val):
        self.data = val
        self.next = None
    
class LinkedList(object):
    
    def __init__(self):
        self.head = None
        
    def isEmpty(self):
        if self.head == None:
            return True
        else:
            return False
    
    '''# how to write the __str__ for this ???
    def __str__(self):
        if self.isEmpty():
            print "LL is empty"
        else:
            node = self.head
            while node != None:
                print "{} --> ".format(node.data),
                node = node.next
            print "|"'''
    
    def traverse(self):
        if self.isEmpty():
            print "LL is empty"
        else:
            node = self.head
            while node != None:
                print "{} --> ".format(node.data),
                node = node.next
            print "|"
            
    
    def addBeg(self, val):
        new_node = Node(val)
        if self.isEmpty():
            self.head = new_node
            new_node.next = None
            return True
        else:
            new_node.next  = self.head
            self.head = new_node
            return True
        
    # Concatenate two linked lists into self.
    def concat2LL(self, LL):
        if self.isEmpty() or LL.isEmpty():
            print "Either empty, cannot do nothing"
        else:
            node = self.head
            while node != None:
                if node.next == None:
                    print "the last node is {}".format(node.data)
                    node.next = LL.head
                    break
                else:
                    node = node.next
            print "new concatenated L1 list is  -"
            self.traverse()
     
    # concatenate 2 LinkedLists into new list
    '''
    # {{ IMP }} ::  L3.head = self.head -> this causes L1 also to be updated. 
    Because you are basically saying L3.head points to the beginning
    of L1. 
    If you replace it with L3.head = self.head, the whole thing goes into recursion. Ask why ?
    '''
    def concat(self, LL):
        L3 = LinkedList()
        # explicity declare a new node with the same value as self.head
        L3.head = Node(self.head.data)  # L3.head = self.head
        node = L3.head
        while node != None:
            if node.next == None: # means you have found the last node in the LL
                node.next = LL.head  
                break
            else:
                node=node.next
        return L3
                
# first Linked List    
L1  = LinkedList()
for each in xrange(3):
    L1.addBeg(random.randint(1,100))
L1.traverse()
print L1.head.data

print "-------------"
# second Linked List
L2 = LinkedList()
for each in xrange(5):
    L2.addBeg(random.randint(100,200))
L2.traverse()
print L2.head.data

'''print "-------Lets merge L1 and L2, by L1's head------"
L1.head.next = L2.head # L1 is lost clearly
print "L1 --", L1.traverse()
print "L2 --", L2.traverse()'''

print "-------Lets concatenate L1 and L2 into L3 (new list) ------"
L3 = L1.concat(L2)
print type(L3)
print "L3 - ", L3.traverse()
print "L1 - ", L1.traverse()
print "L2 - ", L2.traverse()


print "-------Lets concatenate L1 and L2 into L1------"
L1.concat2LL(L2)

print "L3 - ", L3.traverse()
print "L1 - ", L1.traverse()
print "L2 - ", L2.traverse()

            
            
        
        