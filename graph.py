import queue
from time import sleep
import copy

class Node :
    """
    Node class to store each vortex of the graph
    """
    def __init__(self,in_x=0,in_y=0):
        self.x = in_x
        self.y = in_y
        self.data = None

        self.visited = False
        self.added = False

        self.parent = None
        self.parent_direction = None
        self.depth = 0


    def __str__(self):
        return str((self.x,self.y,self.data))

    def __data__(self):
        return str(self.data)


class Graph :
    """
    Graph Class: Used to create , store and print the graph object created from the map
    """

    def __init__(self , gr = None , start = None):
        self.graph_map = gr  #Stores the text map as array of Nodes
        self.start_node = start # Stores the start point node
        self.goals = [] # Stores the goal nodes

    def create_maze_array(self,path):
        '''
        Converts text map into a graph data structure.
        :param path: file path of text file representation of maze
        :return: None
        '''
        text = open(path, "r")
        maze_array = [i.strip() for i in text]

        node_maze = []
        for row_count, row in enumerate(maze_array):
            inner_val = []
            for column_count, value in enumerate(row):
                new_node = Node(column_count, row_count)
                new_node.data = maze_array[row_count][column_count]
                inner_val.append(new_node)
            node_maze.append(inner_val)

        self.graph_map = node_maze


    def get_maze_array(self):
        """
        Returns the graph object array
        :return: array of nodes
        """
        return self.graph_map


    def get_start(self):
        '''
        Get the starting point of the graph
        :param input:
        :return:
        '''
        for i, row in enumerate(self.graph_map):
            for j, value in enumerate(row):
                if (value.data == "s"):
                    return self.graph_map[i][j]

        return Node(-1, -1)

    def get_direction_symbol(self,r, l, u, d):
        """
        Get the relevant symbol depending on the direction of the parent and unvisited children
        :return: Unicode symbol
        """
        input_str = ""
        input_str += "T" if r == True else "F"
        input_str += "T" if l == True else "F"
        input_str += "T" if u == True else "F"
        input_str += "T" if d == True else "F"

        symbol_map = {"FFFF": '\u253c',
                      "TTFF": '\u2502',
                      "FFTT": '\u2500',
                      "FFFT": '\u2534',
                      "FFTF": '\u252c',
                      "FTFF": '\u251c',
                      "TFFF": '\u2524',
                      "FTTF": '\u250c',
                      "TFTF": '\u2510',
                      "FTFT": '\u2514',
                      "TFFT": '\u2518',
                      "TFTT": '\u2574',
                      "TTFT": '\u2575',
                      "FTTT": '\u2576',
                      "TTTF": '\u2577'
                      }

        return symbol_map[input_str]

    def get_goal_points(self):
        """
        Returns the goal nodes
        :return: array of goal nodes
        """
        return self.goals

    def pretty_print_maze(self):
        """
        Function to print the formatted maze
        :return: None
        """
        for node_array in self.graph_map:
            for node in node_array:
                print(node.__data__(), end="")
            print()
        print()



    def print_goal_paths(self):
        """
        Prints the individual goal paths
        :return: None
        """
        for count,goal_node in enumerate(self.goals):

            temp_maze = copy.deepcopy(self)
            curr = temp_maze.get_maze_array()[goal_node.y][goal_node.x]
            while curr.parent != None:
                curr.data = "*"
                curr = curr.parent

            print("Goal : ",count+1)
            temp_maze.pretty_print_maze()


if __name__ == "__main__":

    file_path = "maps/map1.txt"

    maze = Graph()
    maze.create_maze_array(file_path)
    maze.pretty_print_maze()
