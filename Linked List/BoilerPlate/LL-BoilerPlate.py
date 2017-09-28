# Use this code as a template for all Linked List Questions. 

## ** Node Class:
# data : refers to the data that each node in th LL will hold. 
# next_node : behaves like a pointer to the child node. 
class Node(object):

    ## ** Initialize a node
    # We initialize each node with some "data"
    # next_node is set to None as the node is created as a floating node
    # a newly minted node does not point to anything. 
    def __init__(self, data):
        self.data = data
        self.next_node = None

## ** LinkedList Class:
# Acts as a container for the objects of the Node class. 
# head, tail refer to the first and last node of the LL data structure. 
# Eventually head, tail will be given some values which will be instances of the Node Class.        
class LinkedList(object):

    ## ** Initializing a LL:
    # We create an empty Linked List with no nodes. 
    # Hence the head, tail variables (pointers) will point to None.
    def __init__(self):
        self.head = None
        self.tail = None
        
    ## ** Add:
    # To add a value to a Linked List
    # val - variable refers to the data the new node should contain
    # contains the algorithm for inserting a node in the linked list at the beginning. 
    def add (self, val):
    	pass
    
    ## ** Traverse/Display:
    def traverse(self):
    	node = self.head
    	while (node.next_node!=None):
    		print node.data
    		node = node.next_node
    	print node.data

    def find(self, val):
    	pass
            
    def delete(self, val):
    	pass


L = LinkedList()
L.add(10)
L.add(20)
L.add(30)

# L.traverse()
# print L.find(30)
L.delete(20)
L.traverse()