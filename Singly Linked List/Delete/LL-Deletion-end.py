# program to delete node in LL at the end.
# special case : Dont use the tail pointer


class Node(object):
    
    def __init__(self, val):
        self.data = val
        self.next = None

class LinkedList(object):
    
    def __init__(self):
        self.head = None
        # no tail pointer
    
    def isEmpty(self):
        if self.head ==None:
            return True
        else:
            return False
    
    def status(self):
        if self.isEmpty():
            print "no status1"
        else:
            print "Head --> {}".format(self.head.data)
    
    def traverse(self):
        if self.isEmpty():
            print "list empty"
        else:
            node = self.head
            while node != None:
                print "{} --> ".format(node.data),
                node = node.next
            print "|"
            
    # to add nodes to the beginning of the list
    def addBeg(self, val):
        new_node = Node(val)
        if self.isEmpty():
            self.head = new_node # no tail pointer
            self.head.next = None
            return True
        else:
            new_node.next = self.head
            self.head = new_node
            return True
        return False
    
    ## * Delete last node in LL
    '''
    - what does it mean to delete a node? You basically cut off all the pointers surrounding it
    and make it a "floater" 
    - So if we want to delete the last node, we need to make the previous node connected to it point to null
    - We need to maintain two pointers and traverse till we reach the end of the list'''
    def delEnd(self):
        if self.isEmpty():
            print "Cannot delete nothing as Linked List is empty"
        else:
            prev = self.head
            to_del = self.head
            while to_del.next != None:
                prev = to_del   # keeping track of the previous node.
                to_del = to_del.next # ask why this order of statements
             
            prev.next = None
            print "{} deleted!".format(to_del.data)
            self.traverse()
            
LL = LinkedList()
LL.addBeg(5)
LL.addBeg(6)
LL.addBeg(15)
LL.addBeg(96)
LL.addBeg(2)
LL.addBeg(1000)
LL.traverse()

LL.delEnd()

          