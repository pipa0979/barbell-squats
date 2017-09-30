# Purpose -  to add node to the end of the list. 

class Node(object):
    
    def __init__(self, val):
        self.data = val
        self.next = None

    
class LinkedList(object):
    
    # Head, Tail in a new LL will point to None
    def __init__(self):
        self.head = None
        self.tail = None
        
    def isEmpty(self):
        if self.head==None:
            return True
        else: 
            return False
    
    def status(self):
        if self.isEmpty():
            print "Empty!! No Status!"
            return
        else:
            print "Head --> {}".format(self.head.data)
            print "Tail --> {}".format(self.tail.data)
    
    # Print the LL
    def traverse(self):
        node = self.head
        if node == None:
            print "Empty Linked List"
        else:
            while node.next != None:
                print "{} -->".format(node.data),
                node = node.next
            print "{} --> |".format(node.data)
    
    # Adding the new node to the end of the list.
    # the head pointer will stay constant
    # the tail pointer will move to the new node. 
    def addEnd(self, val):
        new_node = Node(val)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
            self.head.next = None 
            return True
        else:
            self.tail.next = new_node # ask why
            self.tail = new_node
            new_node.next = None
            return True
    
LL = LinkedList()
LL.status()
LL.traverse()
for each in xrange(6):
    if LL.addEnd(each):
        print "{} added at the end!".format(each)
    else:
        print "{} not added :(".format(each)
LL.status()
LL.traverse()

        
        