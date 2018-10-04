class Node(object):
    def __init__(self, children):
        if isinstance(children) is not list:
            raise ValueError("Must pass a list to Node")
        self.visited = False
        self.children = children

    def get_children(self):
        """ Returns the children """
        return self.children

    def visit(self):
        """ Sets visited """
        self.visited = True
