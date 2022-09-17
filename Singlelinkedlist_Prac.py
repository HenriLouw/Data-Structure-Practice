class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

    
class sllist:
    def __init__(self) -> None:
        self.head = None

    def append_node(self, val):
        new_node = Node(val)
        if self.head == None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def print_list(self):
        if self.head == None:
            print('List is Empty')
            return
        
        curr = self.head

        while curr:
            print(curr.data)
            curr = curr.next

s = sllist()
s.append_node(3)
s.append_node(4)
s.append_node(5)
s.print_list()