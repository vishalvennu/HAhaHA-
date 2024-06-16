class node:
    nextnode = None

    def __init__(self, data) -> None:
        self.data = data
    
    def __repr__(self) -> str:
        return "data: %s, nextnode: %s" %(self.data, self.nextnode)
    

    
class linkedList:

    def __init__(self) -> None:
        self.head = None
    
    def length(self) -> int:
        current = self.head
        count = 0

        while current:
            count += 1
            current = current.nextnode
        return count
    
    def add(self, data) -> None:
        new_node = node(data)
        new_node.nextnode = self.head
        self.head = new_node

    def insert(self, data, index) -> None:
        if index == 0:
            self.add(data)

        new_node = node(data)
        current = self.head

        while index > 1:
            current = current.nextnode
            index -= 1
        
        temp = current.nextnode
        current.nextnode = new_node
        new_node.nextnode = temp

    def __repr__(self) -> str:
        current = self.head

        while current:
            print(current.data)
            current = current.nextnode

        return "done"

l = linkedList()
n1 = node(10)
n2 = node(20)

n1.nextnode = n2
l.head = n1


l.add(34)
l.insert(52, 3)

# print(n1.print())

    
