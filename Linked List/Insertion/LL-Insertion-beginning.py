# Singly Linked List: Beginning Insertion


class Node(object):
    
    # A new node is always initialized with some data
    # A new node always points to None. It floats
    def __init__(self, data):
        self.data = data
        self.next = None
        

class LinkedList(object):
    
    # A new LL instance will always contain 2 pointers - head, tail.
    # Initially the both will point to None, as no node is added yet to the list.
    def __init__(self):
        self.head = None
        self.tail = None
    
    # Before adding to the LL, we need to check if LL is empty or not. 
    # Adding a new node with data=val at the beginning of the list.
    def addBeg(self, val):
        if self.head == None: # Empty LL
            new_node = Node(val)
            self.head = new_node
            self.tail = new_node
            self.head.next = None
            return True
        else: # LL not empty
            new_node = Node(val)
            self.status()
            new_node.next = self.head
            self.head = new_node
            return True
        return False
            
    # Print the LL from hsead to tail
    def traverse(self):
        node = self.head
        if node == None: 
            print "Empty Linked List"
            return
        while (node.next != None):
            print "{} --> ".format(node.data),
            node = node.next
        print "{} --> ".format(node.data)
        
      
    # Status of head, tail pointers
    def status(self):
        print "Head is currently at - {}".format(self.head.data);
        print "Tail is currently at - {}".format(self.tail.data);
    
LL = LinkedList()

LL.traverse()

for each in xrange(6):
    print "Adding value {} to LL".format(each)
    if (LL.addBeg(each)):
        print "Success! {} Added at the beginning of LL".format(each)
    else:
        print "Failed! {} could not be added to beginning".format(each)

LL.traverse()
print "finished"              