# Program to delete the node at the beginnning of the LL

class Node(object):
    
    def __init__(self, val):
        self.data = val
        self.next = None
    
class LinkedList(object):
    
    def __init__(self):
        self.head = None
        self.tail = None
    
    def isEmpty(self):
        if self.head == None:
            return True
        else:
            return False
    
    def status(self):
        if self.isEmpty():
            print "no status!"
        else:
            print "Head --> {}".format(self.head.data)
            print "Tail --> {}".format(self.tail.data)
    
    def traverse(self):
        if self.isEmpty():
            print "LL empty"
        else:
            node = self.head
            while node.next != None:
                print "{} --> ".format(node.data),
                node = node.next
            print "{} --> | ".format(node.data)
    
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
        
    def delBeg(self):
        if self.isEmpty():
            print "Cannot delete, list empty"
        else:
            self.head = self.head.next
            return True
        return False

LL = LinkedList()

LL.status()
LL.traverse()

for each in xrange(10):
    LL.addBeg(each)

LL.traverse()

if LL.delBeg():
    print "first element deleted"

LL.status()    
LL.traverse()