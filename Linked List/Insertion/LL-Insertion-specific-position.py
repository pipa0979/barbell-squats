# Program to insert a node at a specific position

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
            print "No status! List is empty"
        else:
            print "Head --> {}".format(self.head.data)
            print "tail --> {}".format(self.tail.data)
    
    def traverse(self):
        if self.isEmpty():
            print "LL is empty!"
        else:
            node = self.head
            while node.next != None:
                print "{} --> ".format(node.data),
                node = node.next
            print "{} --> |".format(node.data)
    
    # counts the number of nodes in the list
    def listLength(self):
        count = 0
        if self.isEmpty():
            return 0
        else:
            node = self.head
            while node!= None:
                count += 1
                node = node.next
        return count
                
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
    
    def addEnd(self, val):
        new_node = Node(val)
        if self.isEmpty():
            self.head = new_node
            self.tail = new_node
            self.tail.next = None
            return True
        else:
            self.tail.next = new_node
            self.tail = new_node
            new_node.next = None
            return True
        return False
    
    
    ## ** Add node at a specific position 
    # Eg: pos = 3, add it after 2 (pos-1)
    # Cases - 
    # 1. If LL empty, simply add at the end. 
    # 2. If pos = listLength ; add it at the end
    # 3. If pos = 1, add it at the beginning. 
    # 4. Traverse upto pos-1, insert at pos. 
    
    def addPos(self, val, pos):
        if self.isEmpty():
            self.addEnd(self, val)
            return True
        else:
            print "pos 1 :: ", pos-1
            if pos-1 > self.listLength(): # Ask why pos-1 
                self.addEnd( val)
                return True
            elif (pos-1) <= 0:
                self.addBeg(val)
                return True
            else:
                new_node = Node(val)
                temp = self.head
                count = 0
                while temp != None:
                    count += 1
                    if count == (pos-1): # insert node here
                        new_node.next = temp.next
                        temp.next = new_node
                        return True
                    temp = temp.next
            return False
        
        
LL = LinkedList()

LL.status()
LL.traverse()

for each in xrange(5):
    if LL.addEnd(each):
        print "{} successfully added".format(each)
    else:
        print "{} not added".format(each)

LL.status()
LL.traverse()
LL.listLength()

if LL.addPos(1000, 29):
    print "Adding 1000 at position 29 successful"
else:
    print "Adding 1000 at position 29 failed."
    
LL.status()
LL.traverse()
LL.listLength()

if LL.addPos(1000, 1):
    print "Adding 1000 at position 1 successful"
else:
    print "Adding 1000 at position 1 failed."

LL.status()
LL.traverse()
LL.listLength()
    
if LL.addPos(1000, -89):
    print "Adding 1000 at position -89 successful"
else:
    print "Adding 1000 at position -89 failed."

LL.status()
LL.traverse()
LL.listLength()

if LL.addPos(1000, 4):
    print "Adding 1000 at position 4 successful"
else:
    print "Adding 1000 at position 4 failed."

LL.status()
LL.traverse()
LL.listLength()