class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next =None

    def __repr__(self):
        return "<Node: %s>" % self.data



class LinkedLists(object):

    def __init__(self):
        self.head = None


    def print_list(self):
        current = self.head

        while current is not None:
            print current,

            current = current.next

    def middle(self):

        current = self.head
        if current == None or current.next == None:
            return head

        fast = head
        slow = head

        while fast.next != None and fast.next.next != None:
            fast = fast.next.next
            slow = slow.next

        return slow.data

ll = LinkedLists()
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(1)
node5 = Node(2)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
ll.head = node1
