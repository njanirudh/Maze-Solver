import queue
from time import sleep

class Node :

    def __init__(self,in_x=0,in_y=0):
        self.x = in_x
        self.y = in_y
        self.data = None

        self.visited = False
        self.added = False

        self.parent = None

    def __str__(self):
        return str((self.x,self.y,self.data))

    def __data__(self):
        return str(self.data)


class Graph :

    def __init__(self , gr = None , start = None):
        self.graph_map = gr
        self.start_node = start
        self.goals = list

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
                      "FFTT": '\u2502',
                      "TTFF": '\u2500',
                      "TTTF": '\u2534',
                      "TTFT": '\u252c',
                      "TFTT": '\u251c',
                      "FTTT": '\u2524',
                      "TFFT": '\u250c',
                      "FTFT": '\u2510',
                      "TFTF": '\u2514',
                      "FTTF": '\u2518',
                      "FTFF": '\u2574',
                      "FFTF": '\u2575',
                      "TFFF": '\u2576',
                      "FFFT": '\u2577',
                      "TTTT": 'O'
                      }

        return symbol_map[input_str]

    def pretty_print_maze(self):

        for node_array in self.graph_map:
            for node in node_array:
                print(node.__data__(), end="")
            print()


if __name__ == "__main__":

    file_path = "maps/map1.txt"

    maze = Graph()
    maze.create_maze_array(file_path)
    maze.pretty_print_maze()
