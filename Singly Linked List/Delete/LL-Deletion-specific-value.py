# This program is supposed to delete the node with value as provided by the user
class Node(object):
    
    # a new node is always a floating node
    def __init__(self, val):
        self.data = val
        self.next = None
        
class LinkedList(object):
    
    def __init__(self):
        self.head = None
        
    def isEmpty(self):
        if  self.head == None:
            return True
        else:
            return False
    
    def traverse(self):
        if self.isEmpty():
            print "list is empty"
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
            self.head.next = None
            return True
        else:
            new_node.next = self.head
            self.head = new_node
            return True
    
    ## Deleting a specific node
    '''
    - Find the node
    - maintain two pointers - prev, temp
    - when temp points to the chosen node, disconnect that node from prev and the node after it
    '''
    def delSpecificNode(self, val):
        temp = self.head
        prev = self.head
        while temp.next != None:
            if temp.data == val:
                print "Node found to be deleted"
                prev.next = temp.next
                return True                
            prev = temp
            temp = temp.next
        return False

LL = LinkedList()
LL.addBeg(5)
LL.addBeg(6)
LL.addBeg(15)
LL.addBeg(96)
LL.addBeg(2)
LL.addBeg(1000)
LL.traverse()

LL.delSpecificNode(96)
LL.traverse()
print "=------"

# Play with the code 
print LL.head
k = LL.head
print id(k)
print ((k.next).next).data
            
            
            
            
            