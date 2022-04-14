import copy
import random


def read_graph_from_file(file_path):
    """
    This function is used to read a graph from a file.
    :param file_path:
    :return: Returns an object of the class Graph
    """
    file = open(file_path, "r")
    n, m = file.readline().split()
    n = int(n)
    m = int(m)
    g = Graphr(n)
    for index in range(m):
        x, y, cost = file.readline().split()
        x = int(x)
        y = int(y)
        cost = int(cost)
        g.add_edge(x, y, cost)
    file.close()
    return g


def accessible(g, s,d):
    queue = [s]
    visited = [s]
    distances={}
    pred={}
    for x in g.return_vertices():
        distances[x]=-1
        pred[x]=-1
    distances[s]=0
    while queue:
        vertex = queue.pop(0)
        for x in g.out_neighbours(vertex):
            if x not in visited:
                visited.append(x)
                distances[x] = distances[vertex] + 1
                pred[x] = vertex
                queue.append(x)
                if x==d:
                    return distances,pred
    return distances,pred



def write_graph_into_file(file_path, graph):
    file = open(file_path, "w")
    for vertix in graph.return_vertices():
        if len(graph.out_neighbours(vertix)) == 0 and len(graph.in_neighbours(vertix)) == 0:
            output = str(vertix) + " is an isolated vertex!\n"
            file.write(output)
    for vertix in graph.return_vertices():
        for edge in graph.out_neighbours(vertix):
            output = str(vertix) + " " + str(edge) + " " + str(graph.is_edge(vertix, edge)) + "\n"
            file.write(output)
    file.close()


def read_graph_from_my_file(file_path):
    graph = Graph()
    file = open(file_path, "r")
    line = file.readline().split()
    while line:
        if len(line) == 5:
            graph.add_vertix(int(line[0]))
        else:
            x = int(line[0])
            y = int(line[1])
            cost = int(line[2])
            if x not in graph.return_vertices():
                graph.add_vertix(x)
            if y not in graph.return_vertices():
                graph.add_vertix(y)
            graph.add_edge(x, y, cost)
        line = file.readline().split()
    file.close()
    return graph


def generate_random_graph(n, m):
    """
    This function generates a random graph that has n vertices and m edges
    :param n: INT
    :param m: INT
    :return: An object of class Graph
    """
    graph = Graph()
    index = 0
    counter = 0
    while index < m:

        x = random.randint(0, n - 1)
        y = random.randint(0, n - 1)
        cost = random.randint(0, 300)
        if x not in graph.return_vertices():
            graph.add_vertix(x)
            counter += 1
        if y not in graph.return_vertices():
            graph.add_vertix(y)
            counter += 1
        while (graph.is_edge(x, y) != False):
            x = random.randint(0, n - 1)
            y = random.randint(0, n - 1)
            if x not in graph.return_vertices():
                graph.add_vertix(x)
                counter += 1
            if y not in graph.return_vertices():
                graph.add_vertix(y)
                counter += 1
            cost = random.randint(0, 300)
        graph.add_edge(x, y, cost)
        index += 1
    while counter < n:
        x = random.randint(0, n - 1)
        if x not in graph.return_vertices():
            graph.add_vertix(x)
            counter += 1
    return graph


class Graphr:
    """
    This class represents the object of an oriented Graph.
    """

    def __init__(self, vertices):
        """
        This is the constructor. All the 3 dictionaries are initialised and initially there are 0 vertices in the Graph.
        """
        self.__din = {}
        self.__dout = {}
        self.__dcost = {}
        self.__number_of_vertices = vertices
        for vertex in range(vertices):
            self.__din[vertex] = []
            self.__dout[vertex] = []

    def add_edge(self, x, y, cost):
        """
        A new edge is added:
        First in the in dictionary, then the out dictionary, then the cost dictionary.
        :param x:
        :param y:
        :param cost:
        :return:
        """
        self.__din[y].append(x)
        self.__dout[x].append(y)
        self.__dcost[(x, y)] = cost

    def add_vertix(self, x):
        """
        A new vertex is added, having 0 edges.
        :param x:
        :return:
        """
        if x not in self.return_vertices():
            self.__din[x] = []
            self.__dout[x] = []
            self.__number_of_vertices += 1

    def return_number_of_vertices(self):
        """

        :return: An integer value being the number of vertices in the graph is returned.
        """
        return self.__number_of_vertices

    def is_edge(self, x, y):
        """
        This function checks if there is an edge between the vertices x and y, and if there is one the cost is returned.
        Otherwise False is returned.
        :param x:
        :param y:
        :return: False if there is not an edge between x and y and False otherwise.
        """
        if x in self.return_vertices() and y in self.return_vertices():
            if y in self.__dout[x]:
                return self.__dcost[(x, y)]
            return False
        else:
            return False

    def get_in_degree(self, x):
        """
        This function returns the number of vertices that goes into the vertex x.
        :param x:
        :return:
        """
        return len(self.__din[x])

    def get_out_degree(self, x):
        """
        This function returns the number of vertices that comes from the vertex x.
        :param x:
        :return:
        """
        return len(self.__dout[x])

    def out_neighbours(self, x):
        """
        This function returns a list of the outbound neighbours of the vertex x
        :param x:
        :return:
        """
        return copy.copy(self.__dout[x])

    def in_neighbours(self, x):
        """
        This function returns a list of the outbound neighbours of the vertex x
        :param x:
        :return:
        """
        return copy.copy(self.__din[x])

    def return_vertices(self):
        """

        :return: A copy of the list of vertices is returned.
        """
        return list(self.__din.keys())

    def delete_edge(self, x, y):
        """
        This function is used to delete the edge from x to y.
        First delete from in dictionary, then from out and then from cost.
        :param x:
        :param y:
        :return:
        """
        self.__din[y].remove(x)
        self.__dout[x].remove(y)
        self.__dcost.pop((x, y))

    def delete_vertex(self, x):
        """
        This function is used to delete a whole vertex and the edges that it contained.
        :param x:
        :return:
        """
        list_in = copy.copy(self.__din[x])
        for vertex in range(0, len(list_in)):
            self.delete_edge(list_in[vertex], x)
        list_out = copy.copy(self.__dout[x])
        for vertex in range(0, len(list_out)):
            self.delete_edge(x, list_out[vertex])
        self.__dout.pop(x)
        self.__din.pop(x)

    def print_graph(self):
        """
        This function is used to print the graph.
        :return:
        """
        for vertix in self.return_vertices():
            if len(self.out_neighbours(vertix)) == 0 and len(self.in_neighbours(vertix)) == 0:
                print(str(vertix) + " is an isolated vertex!")
            for edge in self.out_neighbours(vertix):
                output = str(vertix) + " " + str(edge) + " " + str(self.__dcost[(vertix, edge)])
                print(output)


class Graph:
    """
    This class represents the object of an oriented Graph.
    """

    def __init__(self):
        """
        This is the constructor. All the 3 dictionaries are initialised and initially there are 0 vertices in the Graph.
        """
        self.__din = {}
        self.__dout = {}
        self.__dcost = {}
        self.__number_of_vertices = 0

    def add_edge(self, x, y, cost):
        """
        A new edge is added:
        First in the in dictionary, then the out dictionary, then the cost dictionary.
        :param x:
        :param y:
        :param cost:
        :return:
        """
        self.__din[y].append(x)
        self.__dout[x].append(y)
        self.__dcost[(x, y)] = cost

    def add_vertix(self, x):
        """
        A new vertex is added, having 0 edges.
        :param x:
        :return:
        """
        if x not in self.return_vertices():
            self.__din[x] = []
            self.__dout[x] = []
            self.__number_of_vertices += 1

    def return_number_of_vertices(self):
        """

        :return: An integer value being the number of vertices in the graph is returned.
        """
        return self.__number_of_vertices

    def is_edge(self, x, y):
        """
        This function checks if there is an edge between the vertices x and y, and if there is one the cost is returned.
        Otherwise False is returned.
        :param x:
        :param y:
        :return: False if there is not an edge between x and y and False otherwise.
        """
        if x in self.return_vertices() and y in self.return_vertices():
            if y in self.__dout[x]:
                return self.__dcost[(x, y)]
            return False
        else:
            return False

    def get_in_degree(self, x):
        """
        This function returns the number of vertices that goes into the vertex x.
        :param x:
        :return:
        """
        return len(self.__din[x])

    def get_out_degree(self, x):
        """
        This function returns the number of vertices that comes from the vertex x.
        :param x:
        :return:
        """
        return len(self.__dout[x])

    def out_neighbours(self, x):
        """
        This function returns a list of the outbound neighbours of the vertex x
        :param x:
        :return:
        """
        return copy.copy(self.__dout[x])

    def in_neighbours(self, x):
        """
        This function returns a list of the outbound neighbours of the vertex x
        :param x:
        :return:
        """
        return copy.copy(self.__din[x])

    def return_vertices(self):
        """

        :return: A copy of the list of vertices is returned.
        """
        return list(self.__din.keys())

    def delete_edge(self, x, y):
        """
        This function is used to delete the edge from x to y.
        First delete from in dictionary, then from out and then from cost.
        :param x:
        :param y:
        :return:
        """
        self.__din[y].remove(x)
        self.__dout[x].remove(y)
        self.__dcost.pop((x, y))

    def delete_vertex(self, x):
        """
        This function is used to delete a whole vertex and the edges that it contained.
        :param x:
        :return:
        """
        list_in = copy.copy(self.__din[x])
        for vertex in range(0, len(list_in)):
            self.delete_edge(list_in[vertex], x)
        list_out = copy.copy(self.__dout[x])
        for vertex in range(0, len(list_out)):
            self.delete_edge(x, list_out[vertex])
        self.__dout.pop(x)
        self.__din.pop(x)

    def print_graph(self):
        """
        This function is used to print the graph.
        :return:
        """
        for vertix in self.return_vertices():
            if len(self.out_neighbours(vertix)) == 0 and len(self.in_neighbours(vertix)) == 0:
                print(str(vertix) + " is an isolated vertex!")
            for edge in self.out_neighbours(vertix):
                output = str(vertix) + " " + str(edge) + " " + str(self.__dcost[(vertix, edge)])
                print(output)
