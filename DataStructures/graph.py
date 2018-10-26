class Graph(object):
    """Graphs are implemented using a map and an array.
        
    Attributes
    -----------
    map : dict
        A dictionary of node, edge combinations.
    nodes : list
        List of nodes that define edges between a key in the map.
    """
    def __init__(self):
        self.map = {}
        self.nodes = []

    def add_nodes(self, node):
        self.nodes.append(node)
