from graph import read_graph_from_file, Graph, generate_random_graph, write_graph_into_file, read_graph_from_my_file, \
    accessible


class UI:
    def __init__(self, graph):
        self.__type_of_graph = graph
        self.__graph = None
        self.__copy_of_graph = None

    def generate_random_graph(self):
        n = int(input("What is the number of vertices that you want?"))
        m = int(input("What is the number of edges that you want?"))
        if m > n * n:
            print("The amount of given edges is not right for the given vertices!")
        else:
            self.__graph = generate_random_graph(n, m)

    def read_graph_from_file_ui(self):
        file_path = input("Whats the name of the file you want to read from?")
        try:
            self.__graph = read_graph_from_file(file_path)
            print("The graph was read succesfully!")
        except:
            print("There was an error!")

    def write_graph_to_file_ui(self):
        file_path = input("Whats the name of the file that you want to write the graph in?")
        write_graph_into_file(file_path, self.__graph)

    def is_edge_ui(self):
        x = int(input("Whats the first vertex?"))
        y = int(input("Whats the second vertex?"))
        if self.__graph.is_edge(x, y) != False:
            print(self.__graph.is_edge(x, y))
        else:
            print("There is not an edge between the given vertices!")

    def print_in_degree(self):
        x = int(input("Whats the vertex that you want to get the in degree for?"))
        if x in self.__graph.return_vertices():
            print("The number of edges that goes in the vertex " + str(x) + " is " + str(self.__graph.get_in_degree(x)))
        else:
            print("The given vertex is not in the graph!")

    def print_out_degree(self):
        x = int(input("Whats the vertex that you want to get the out degree for?"))
        if x in self.__graph.return_vertices():
            print("The number of edges that comes from the vertex " + str(x) + " is " + str(
                self.__graph.get_out_degree(x)))
        else:
            print("The given vertex is not in the graph!")

    def print_graph_ui(self):
        self.__graph.print_graph()

    def get_number_of_vertices_ui(self):
        print("The total number of vertices from the graph is " + str(self.__graph.return_number_of_vertices()))

    def parse_the_list_of_vertices_ui(self):
        print("The list of vertices is:")
        list = self.__graph.return_vertices()
        list.sort()
        print(list)

    def parse_the_in_neighbours_ui(self):
        x = int(input("Give me the vertex of which you want to see the inbound neighbours!"))
        if x in self.__graph.return_vertices():
            print("The list of inbound neighbours of " + str(x) + "is:")
            print(self.__graph.in_neighbours(x))
        else:
            print("The given vertex is not in the graph!")

    def parse_the_out_neighbours_ui(self):
        x = int(input("Give me the vertex of which you want to see the outbound neighbours!"))
        if x in self.__graph.return_vertices():
            print("The list of inbound neighbours of " + str(x) + "is:")
            print(self.__graph.out_neighbours(x))
        else:
            print("The given vertex is not in the graph!")

    def add_vertex_UI(self):
        x = int(input("What is the vertex that you want to add?"))
        if x in self.__graph.return_vertices():
            print("The given vertex is already in the graph!")
        else:
            self.__graph.add_vertix(x)
            print("the given vertex was succesfully added!")

    def add_edge_UI(self):
        x = int(input("Whats the first vertex?"))
        y = int(input("Whats the second vertex?"))
        cost = int(input("What is the cost of the edge?"))
        if self.__graph.is_edge(x, y) == False:
            self.__graph.add_edge(x, y, cost)
        else:
            print("The given edge already exists!")

    def accesible_ui(self):
        x = int(input("Whats the first vertex?"))
        y = int(input("Whats the second vertex?"))
        distance, pred = accessible(self.__graph, x, y)
        if distance[y] == -1:
            print("No path between these 2")
        else:
            path = []
            crawl = y
            path.append(y)
            while pred[crawl] != -1:
                path.append(pred[crawl])
                crawl = pred[crawl]
            good_path = path[::-1]
            print("The shortest path is of length" + str(distance[y]) + "and is the following" + str(good_path))
    def delete_edge_UI(self):
        x = int(input("Whats the first vertex?"))
        y = int(input("Whats the second vertex?"))
        if self.__graph.is_edge(x, y) != False:
            self.__graph.delete_edge(x, y)
        else:
            print("The given edge doesnt exist!")

    def delete_vertex_UI(self):
        x = int(input("Whats the vertex that you want to delete?"))
        if x in self.__graph.return_vertices():
            self.__graph.delete_vertex(x)
        else:
            print("The given vertex is not in the graph!")

    def read_graph_from_my_format(self):
        file_path = input("Whats the name of the file you want to read from?")
        try:
            self.__graph = read_graph_from_my_file(file_path)
            print("The graph was read succesfully!")
        except:
            print("There was an error!")

    def start(self):
        commands = {"12": self.read_graph_from_file_ui,
                    "15": self.write_graph_to_file_ui,
                    "13": self.print_graph_ui,
                    "1": self.get_number_of_vertices_ui,
                    "3": self.is_edge_ui,
                    "4": self.print_in_degree,
                    "5": self.print_out_degree,
                    "2": self.parse_the_list_of_vertices_ui,
                    "6": self.parse_the_in_neighbours_ui,
                    "7": self.parse_the_out_neighbours_ui,
                    "8": self.add_vertex_UI,
                    "9": self.add_edge_UI,
                    "14": self.generate_random_graph,
                    "10": self.delete_edge_UI,
                    "11": self.delete_vertex_UI
            , "16": self.read_graph_from_my_format,
                    "17": self.accesible_ui
                    }
        while True:
            print("1 - get the number of vertices;")
            print("2 - parse (iterate) the set of vertices;")
            print("3 - check if it is an edge if there is the edge, the cost will be printed")
            print("4 - print the in degree")
            print("5 - print the out degree")
            print("6 - parse the inbound vertices of a given vertex")
            print("7 - parse the outbound vertices of a given vertex")
            print("8 - add a new vertex")
            print("9 - add a new edge")
            print("10 - delete an edge")
            print("11 - delete a vertex")
            print("12 - to read a graph from a file")
            print("13 - print the read graph")
            print("14 - generate a random graph with a given number of vertices and edges!")
            print("15 - write graph into file.")
            print("16 - read a graph from my format!")
            print("17 - accesible")
            cmd = input("\nWhat is your command\n")
            if cmd in commands:
                commands[cmd]()
            elif cmd == "0":
                break
            else:
                print("Invalid command")
