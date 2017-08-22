class Node(object):

    def __init__(self, data, children=None):
        self.data = data
        self.children = children or []
        # if children is None:
        #     self.children = []
        # else:
        #     self.children = children


    def find_DFS(self, data):
        """depth first search STACK"""

        to_visit = [self]

        while to_visit:
            current = to_visit.pop()

            if current.data == data:
                return current

            to_visit.extend(current.children)


    def find_BFS(self, data):
        """breath first search  QUEUE"""

        to_visit = [self]

        while to_visit:
            current = to_visit.pop(0)

            if current.data == data:
                return current

            to_visit.exten(current.children)


class Tree(object):
    def find_in_tree(self, data):

        return self.root.find(data)



