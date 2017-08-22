class Node(object):

    def __init__(self, data, children=[]):
        self.data = data
        self.children = children or []


    def __repr__(self):
        return "<Node %s>" % self.data

    def find(self, data):


        to_visit = [self]

        while to_visit:
            current = to_visit.pop()

            if current.data == data:
                return current
            to_visit.extend(current.children)




class Tree(object):

    def __init__(self, root):
        self.root = root

    def __repr__(self):
        return "<Tree Root: %s>" % self.root

    def find_in_tree(self, data):

        return self.root.find(data)



dumby = Node("dumbledore")
snape = Node("snape")
flitwick = Node("flitwick")

dumby.children.append(snape)
dumby.children.append(flitwick)