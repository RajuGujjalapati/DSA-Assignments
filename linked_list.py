class Node:
    def __init__(self, data=None, next_=None):
        self.data=data
        self.next_=next_

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begining(self,data):
        node = Node(data,self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return 
        itr = self.head
        lstr=''      
        while itr:
            lstr+=str(itr.data) +' --> '
            itr = itr.next_
  
        print(lstr)


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_begining(5)
    #ll.print()
    ll.insert_at_begining(57)
    #ll.print()
    ll.insert_at_begining(93)
    ll.print()


