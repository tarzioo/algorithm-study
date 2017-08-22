class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __repr__(self):
        return "<Node: %s>" % self.data



class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None


    def print_list(self):
        current = self.head

        while current is not None:
            print current,

            current = current.next


    def append_to(self, item):
        

        new_node = Node(item)
        current = self.head

        if current is None:
            current = new_node

        while current.next is not None:
            current = current.next

        current.next = new_node


    def find(self, item):

        current = self.head

        while current is not None:
            if current.data == item:
                return True
            current = current.next

        return False


    def remove(self, item):

        if self.head is not None and self.head.data == item:
            self.head = self.head.next
            if self.head is None:
                self.tail = None

        current = self.head

        while current.next is not None:
            if current.next.data == item:
                current.next = current.next.next
                if current.next is None:
                    self.tail = current

                return

            else:
                current = current.next


    def reverse(self):

        current = self.head
        previous = None

        while current:
            next = current.next
            current.next = previous
            previous = current
            current = next


        self.head = previous


def remove_duplicates(head):
    if head == None:
        pass
    elif head.next == None:
        pass
    elif head.data != head.next.data:
        remove_duplicates(head.next)
    elif head.data == head.next.data:
        head.next = head.next.next
        remove_duplicates(head.next)
    return head

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

node1.next = node2
node2.next = node3

my_list = LinkedList()
my_list.head = node1