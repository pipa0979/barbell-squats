# Program to delete a node of specific value before/after a node of specific value

class Node(object):
    
    def __init__(self, val):
        self.next = None
        self.data = val
    
class LinkedList(object):
    
    def __init__(self):
        self.head = None
        #self.tail = None
    
    def isEmpty(self):
        if self.head == None:
            return True
        else:
            return False
        
    def traverse(self):
        if self.isEmpty():
            print "LL empty"
        else:
            node = self.head
            while node != None:
                print "{} --> ".format(node.data),
                node = node.next
            print ""
            
    def addBeg(self, val):
        new_node = Node(val)
        if self.isEmpty():
            self.head = new_node
            self.head.next = None
            return True
        else:
            new_node.next = self.head 
            self.head = new_node
            return True
        return False
    
    ## Delete a node before a node(val) else do nothing
    ## 4 --> 5 --> 1 --> 6 --> 8
    # Case 1 :: if val is 1, then we want to delete 5
    # Case 2 :: if val is 4, then no previous node exists and so do nothing.
    # Maintain 3 pointers, prev, toDel, temp.  ''' Ask why ?'''
    # when temp points to Node(val), isolate the node pointed by prev 
    def delNodeBeforeVal(self, val):
        if self.isEmpty():
            print "LL empty! Cant delete"
            return False
        else:
            prev = self.head
            toDel = self.head
            temp = self.head
            while temp.next != None:
                if temp.data == val:
                    print "Node is found, lets delete before!"
                    if temp == toDel:
                        print "No previous node exists"
                        return False
                    elif prev == toDel:
                        print "{} will be deleted".format(toDel.data)
                        self.head = temp
                        return True
                    else:
                        print "{} will be deleted".format(toDel.data)
                        print "prev --> {}".format(prev.data)
                        print "toDel --> {}".format(toDel.data)
                        print "temp --> {}".format(temp.data)
                        prev.next = temp
                        toDel.next = None
                        return True
                prev = toDel
                toDel = temp
                temp = temp.next 
        return False
    
LL = LinkedList()

LL.addBeg(8)
LL.addBeg(6)
LL.addBeg(1)
LL.addBeg(5)
LL.addBeg(4)

# 4 -->  5 -->  1 -->  6 -->  8 -->          
LL.traverse()

'''
Try each of the following delete cases one by one
'''
# prev --> 4
# toDel --> 4
# temp --> 4
LL.delNodeBeforeVal(4)

# prev --> 4
# toDel --> 4
# temp --> 5
LL.delNodeBeforeVal(5)

# prev --> 4
# toDel --> 5
# temp --> 1
LL.delNodeBeforeVal(1)

LL.traverse()