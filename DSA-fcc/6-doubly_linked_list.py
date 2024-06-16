class node:
    prevnode = None
    nextnode = None

    def __init__(self, data) -> None:
        self.data = data
    
    def __repr__(self) -> str:
        return "data: %s, nextnode: %s" % (self.data,self.nextnode)
    
class linkedList:

    def __init__(self) -> None:
        self.head = None

    def is_empty(self) -> bool:
        return self.head == None
    
    def length(self) -> int:
        current = self.head
        count = 0

        while current:
            count += 1
            current = current.nextnode
        return count
    
    def __repr__(self) -> str:
        current = self.head

        while current:
            print(current.data)
            current = current.nextnode

        return "done"
    


n1 = node(10)
n2 = node(20)
n3 = node(30)

n1.nextnode = n2
n2.prevnode = n1

n2.nextnode = n3
n3.prevnode = n2

l = linkedList()
l.head = n1
l.add(34)
l.insert(52, 3)

print(l)
print(l.is_empty())
print(l.length())