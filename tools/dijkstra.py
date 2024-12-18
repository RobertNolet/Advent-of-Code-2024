class Dijkstra:
    """Generic Dijkstra's algorithm solver.
    """ 
    def __init__(self, nodes, nbrs, dist):
        """Initialize a Dijkstra solver with a set of nodes, a description of
        neighbours of nodes and distances between nodes.

        Args:
            nodes (set): 
                The nodes of a graph, elements must be hashable (for 
                example, tuples of coordinates.)
            nbrs (dict or function): 
                A dict with as key a node, or a function with as argument 
                a node. The (return)value is a set of neighbours of this node.
            dist (int, dict or function): 
                A dict with as key a tuple of two neighbouring nodes, or a
                function with as arguments two neighbouring nodes. The
                (return)value is the distance between these two nodes. If
                integer, the distance between any two neighbouring nodes.
        """
        self.nodes = nodes
        if type(nbrs) == dict:
            self.nbrs = lambda node: nbrs[node]
        else:
            self.nbrs = nbrs
        if type(dist) == dict:
            self.dist = lambda node1, node2: dist[(node1, node2)]
        elif type(dist) == int:
            self.dist = lambda node1, node2: dist
        else:
            self.dist = dist
        self.start = None
        self.end = None

    def reset(self):
        """Reset internal data such as previously calculated distances.
        """
        self.unvisited = self.nodes.copy()
        self.visited = {}
        self.current = None
        self.curdist = 0
        self.tocheck = {}

    def step(self):
        """Check one unvisited node.

        Returns:
            bool: Whether algorithm can continue. If false there are no
                more nodes to check.
        """
        for node in (self.nbrs(self.current) & self.unvisited):
            d = self.curdist + self.dist(self.current, node)
            if self.tocheck.get(node, d+1) > d:
                self.tocheck[node] = d
        if not self.tocheck:
            return False
        self.curdist, self.current = min((d,n) for n,d in self.tocheck.items())
        self.tocheck.pop(self.current)
        self.unvisited.remove(self.current)
        self.visited[self.current] = self.curdist
        return True

    def mindist(self, start, end):
        """Calculate minimal distance between start note and end note.

        Args:
            start (node): Starting node
            end (node): Destination node

        Returns:
            int: distance
        """
        if type(end) is not set:
            end = {end}
        if start != self.start:
            self.reset()
            self.start = start
            self.current = start
        while not (end & self.visited.keys()):
            if not self.step():
                # No route found
                return None
        return self.curdist

    def alldist(self, start):
        """Calculate shortest distance to start node for all reachable nodes

        Args:
            start (node): Starting node

        Returns:
            dict: Dictionary with as keys the reachable nodes and as values
                the distance from start to this node.
        """
        if start != self.start:
            self.reset()
            self.start = start
            self.current = start
        while self.unvisited:
            self.step()
        return self.visited

    def shortestpath(self, start, end):
        """Calculate a shortest path from start node to end node.

        Args:
            start (node): Starting node
            end (node): Destination node

        Returns:
            list: List of neighnouring nodes [start, ..., end]
        """
        d = self.mindist(start, end)
        node = next(n for n in end if self.visited[n] == d)
        path = [end]
        while node != start:
            node = next(n for n in self.nbrs(node) if self.visited.get(n, d+1) == d - self.dist(n, node))
            path.append(node)
            d = self.visited[node]
        return path.reverse()

