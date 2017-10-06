# Program to insert a node after a node of specific value

class Node(object):
    
    def __init__(self, val):
        self.data = val
        self.next = None
    
class LinkedList(object):
    
    def __init__(self):
        self.head = None
        self.tail = None
        
    def isEmpty(self):
        if self.head ==None:
            return True
        else:
            return False
    
    def status(self):
        if self.isEmpty():
            print "No status! List empty"
        else:
            print "Head --> {}".format(self.head.data)
            print "Tail --> {}".format(self.tail.data)
    
    def listLength(self):
        count = 0
        if self.isEmpty():
            return count
        else:
            node = self.head
            while node != None:
                count += 1
                node = node.next
            return count
    
    def traverse(self):
        if self.isEmpty():
            print "Cannot traverse! List is Empty"
        else:
            node = self.head
            while node.next != None:
                print "{} -->".format(node.data),
                node = node.next
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
    
    ## Find:
    # Find the node of specific value and return it.
    # if node not found, return None
    def find(self, val):
        if self.isEmpty():
            return None
        else:
            temp = self.head
            while temp != None:
                if temp.data == val:
                    return temp
                temp = temp.next
            return None    
            

    ## Adds a new node(val2) after a node of specific value(val1)
    # If node not found, add it at the beginning. 
    def addNodeAfterVal(self, val1, val2):
        if self.isEmpty():
            self.addBeg(val2)
            return True
        else:
            new_node = Node(val2)
            temp = self.find(val1)
            if temp == None:
                return False
            else:
                new_node.next = temp.next
                temp.next = new_node
                return True
            
    ## Add a node(val2) before a node of specific value(val1)
    # If node not found, insert at the beginning.
    # We maintain two pointers, temp & prev
    # prev - is one step behind temp so once we find the value(temp), 
    # we can insert the new node right after prev
    def addNodeBeforeVal(self, val1, val2):
        if self.isEmpty():
            self.addBeg(val2)
            return True
        else:
            new_node = Node(val2)
            temp = self.head
            prev = self.head
            while temp.next != None:
                if temp.data == val1:
                    print "Node is found"
                    new_node.next = prev.next
                    prev.next = new_node
                    return True
                prev = temp
                temp = temp.next
            return False
        
                    
LL = LinkedList()

LL.status()
LL.traverse()

for each in xrange(9):
    if LL.addBeg(each):
        print "{} added at the beginning successfully".format(each)
    else:
        print "{} not added".format(each)

LL.status()
LL.traverse()

if LL.addNodeAfterVal(3, 1000):
    print " 1000 added after 3"
else:
    print " 1000 not added after 3"

LL.status()
LL.traverse()

if LL.addNodeBeforeVal(3, 333):
    print " 333 added before 3"
else:
    print " 333 not added before 3"
LL.traverse()