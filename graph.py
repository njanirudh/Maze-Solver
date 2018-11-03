import queue
from time import sleep
import copy


class Node :
    """

    """

    def __init__(self,in_x=0,in_y=0):
        self.x = in_x
        self.y = in_y
        self.data = None

        self.visited = False
        self.added = False

        self.parent = None
        self.depth = 0

    def __str__(self):
        return str((self.x,self.y,self.data))

    def __data__(self):
        return str(self.data)


class Graph :

    def __init__(self , gr = None , start = None):
        self.graph_map = gr
        self.start_node = start
        self.goals = []

    def create_maze_array(self,path):
        '''
        :param path: file path of text file representation of maze
        :return: array representation of the maze
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
        return self.graph_map

    def get_start(self):
        '''
        Get the starting point of the node
        :param input:
        :return:
        '''

        for i, row in enumerate(self.graph_map):
            for j, value in enumerate(row):
                if (value.data == "s"):
                    return self.graph_map[i][j]

        return Node(-1, -1)

    def get_direction_symbol(self,r, l, u, d):

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
                      "TTTF": '\u2577',
                      "TTTT" : ' '}

        return symbol_map[input_str]

    def pretty_print_maze(self):

        for node_array in self.graph_map:
            for node in node_array:
                print(node.__data__(), end="")
            print()
        print()

    def print_goal_paths(self):

        for count,goal_node in enumerate(self.goals):

            temp_maze = copy.deepcopy(self)
            curr = temp_maze.get_maze_array()[goal_node.y][goal_node.x]
            while curr.parent != None:
                curr.data = "X"
                curr = curr.parent

            print("Goal : ",count+1)
            temp_maze.pretty_print_maze()


if __name__ == "__main__":

    file_path = "maps/map1.txt"

    maze = Graph()
    maze.create_maze_array(file_path)
    maze.pretty_print_maze()
