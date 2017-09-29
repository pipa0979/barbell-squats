# This is the practice file - Insertion beginning of Linked List. 

class Node(object):
    
    def __init__(self, data):
        self.data = data
        self.next = None
    
class LinkedList(object):
    
    def __init__(self):
        self.head = None
        self.tail = None
        
    def addBeg(self, val):
        new_node = Node(val)
        if self.head == None: # LL is empty
            self.head = new_node
            self.tail = new_node
            self.head.next = None
            return True
        else:   # LL is not empty
            new_node.next = self.head 
            self.head = new_node
            return True
        return False
    
    # print the LL
    def traverse(self):
        node = self.head
        if node == None:
            print "List is empty"
        else:
            while node.next != None:
                print "{} --> ".format(node.data),
                node = node.next
            print "{} --| ".format(node.data), 
                
    # prints the nodes the head, tail is currently pointing to
    def status(self):
        print "Head --> {} ".format(self.tail.data)
        print "Tail --> {} ".format(self.head.data)
        

LL =  LinkedList()
LL.traverse()
for each in xrange(3):
    if LL.addBeg(each):
        print "{} successfully added".format(each)
    else:
        print "Failed to add {}".format(each)
LL.status()
LL.traverse()        

    
        