# Use this code as a template for all Linked List Questions. 

## ** Node Class:
#----------------
# data : refers to the data that each node in th LL will hold. 
# next_node : behaves like a pointer to the child node. 
class Node(object):

    ## ** Initialize a node
    #----------------------
    # We initialize each node with some "data"
    # next_node is set to None as the node is created as a floating node
    # a newly minted node does not point to anything. 
    def __init__(self, data):
        self.data = data
        self.next_node = None

## ** LinkedList Class:
#----------------------
# Acts as a container for the objects of the Node class. 
# head, tail refer to the first and last node of the LL data structure. 
# Eventually head, tail will be given some values which will be instances of the Node Class.        
class LinkedList(object):

    ## ** Initializing a LL:
    #-----------------------
    # We create an empty Linked List with no nodes. 
    # Hence the head, tail variables (pointers) will point to None.
    def __init__(self):
        self.head = None
        self.tail = None
        
    ## ** Add:
    #--------
    # To add a value to a Linked List
    # val - variable refers to the data the new node should contain
    # contains the algorithm for inserting a node in the linked list at the beginning. 
    # Return - True/False if successful/failed
    def add (self, val):
    	pass
    
    ## ** Delete:
    #------------
    # val - variable refers to the node(data) that should be deleted
    # it is checked if a node containing that value is present. 
    # contains algo for deleting the node. 
    # Return - True/False if successful/failed
    def delete(self, val):
    	pass
    
    ## ** Traverse/Display/Print:
    #----------------------------
    # Return - To print all the nodes in the linked list
    def traverse(self):
    	node = self.head
    	while (node.next_node!=None):
    		print node.data
    		node = node.next_node
    	print node.data

    ## ** Find/Search:
    #-----------------
    # To find a node with val if it exists in the LL
    # return True/False 
    def find(self, val):
    	pass
        

# Create instance of LL
L = LinkedList()

# Add bunch of values to LL
if L.add(10):
    print "10 added to LL"
if L.add(20):
    print "20 added to LL"
if L.add(30):
    print "30 added to LL"

# Print LL
L.traverse()

# Check if val present in LL 
find_val = 30
if L.find(find_val): 
    print "{} present in LL".format(find_val)
else:
    print "{} not found in LL".format(find_val
    
# Delete del_val                                      
del_val = 20
if L.delete(del_val):
    print "{} successfully deleted from LL".format(del_val)
else:
    print "{} could not be deleted".formt(del_val)
                                    
# Print LL 
L.traverse()
                                      
                                      
                                      