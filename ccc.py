class Node:
    def __init__(self,data,next_node = None):
        self.data = data
        self.next = next_node
        
class Linkedlist:
    def __init__(self):
        self.head = None
        
    def node_insertion(self,data):
        node = Node(data,self.head)
        self.head = node

    def list_insertion(self,data_list):
        self.head = None
        for data in data_list:
            self.node_insertion(data)
        
        
    def printing(self):
        itr = self.head
        
        while itr :
            print(itr.data,end='')
            itr = itr.next
            if itr is not None:
                print('-->',end='')

def add_two_lists(l1 : Node,l2 : Node) -> Node:
    dummy = Node(data=-1)
    current_node = dummy
    t1 = l1
    t2 = l2
    carry = 0
    
    while t1  or t2 or carry:
        val1 = t1.data
        val2 = t2.data
        
        total_sum = val1 + val2
        element = total_sum % 10
        carry = total_sum // 10
        
        current_node.next = Node(element)
        current_node = current_node.next
        
        if t1:
            t1=l1.next
        
        if t2:
            t2 = l2.next
        
    return dummy.next
        
        
        
l1 = [2,4,3] 
l2 = [5,6,4]

for ele in l1 :
    list_head_1 = Node(data=ele)
    list_head_1 = list_head_1.next

for ele in l2 :
    list_head_2 = Node(data=ele)
    list_head_2 = list_head_2.next

objl = Linkedlist()
objl.list_insertion(l1)

obj2 = Linkedlist()
obj2.list_insertion(l2)

value = add_two_lists(list_head_1,list_head_2)


print(value)