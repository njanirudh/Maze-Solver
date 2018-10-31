#!/usr/bin/sudo python

from collections import deque
from time import sleep
import keyboard
import queue

class Node :
    def __init__(self,in_x=0,in_y=0):
         self.x = in_x
         self.y = in_y
         self.data = None
         self.visited = False
         self.added = False

    def __str__(self):
        #return str((self.x,self.y,self.data))
        return str(self.data)


def create_maze_array(path):
    '''
    :param path: file path of text file representation of maze
    :return: array representation of the maze
    '''
    text = open(path,"r")
    maze_array = [i.strip() for i in text]

    node_maze = []
    for row_count, row in enumerate(maze_array):
        inner_val = []
        for column_count, value in enumerate(row):
            new_node = Node(column_count,row_count)
            new_node.data = maze_array[row_count][column_count]
            inner_val.append(new_node)
        node_maze.append(inner_val)

    return node_maze

def find_start(input):
    '''
    Get the starting point of the node
    :param input:
    :return:
    '''

    for i,row in enumerate(input):
        for j,value in enumerate(row):
            if(value.data == "s"):
                return input[i][j]

    return Node(-1,-1)


def pretty_print_maze(node_matrix):

    for node_array in node_matrix:
        for node in node_array:
            print(node,end = "")
        print()

def get_symbol(r,l,u,d):

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
                  "FFFT": '\u2577'}

    return symbol_map[input_str]


def run_dfs_on_maze(maze,start_pnt):

    current_node = start_pnt
    current_node.visited = True
    current_node.data = ""

    maze_array[current_node.y][current_node.x] = current_node

    right_node = None
    left_node  = None
    up_node  = None
    down_node  = None

    if (current_node.x != (len(maze[0]))):
        right_node = maze[current_node.y][current_node.x + 1]
        right_node_value = right_node.data

        if right_node_value != "=" and right_node_value != "|":
            if right_node.added is False and right_node.visited is False:
                right_node.added = True
                run_dfs_on_maze(maze, right_node)

    if (current_node.x != 0):
        left_node = maze[current_node.y][current_node.x - 1]
        left_node_value = left_node.data

        if left_node_value != "=" and left_node_value != "|":
            if left_node.added is False and left_node.visited is False:
                left_node.added = True
                run_dfs_on_maze(maze, left_node)

    if (current_node.y != 0):
        up_node = maze[current_node.y - 1][current_node.x]
        up_node_value = up_node.data

        if up_node_value != "=" and up_node_value != "|":
            if up_node.added is False and up_node.visited is False:
                up_node.added = True
                run_dfs_on_maze(maze, up_node)

    if (current_node.y != (len(maze) - 1)):
        down_node = maze[current_node.y + 1][current_node.x]
        down_node_value = down_node.data

        if down_node_value != "=" and down_node_value != "|":
            if down_node.added is False and down_node.visited is False:
                down_node.added = True
                run_dfs_on_maze(maze, down_node)

    current_node.data = str(get_symbol(right_node.visited,
                                       left_node.visited,
                                       up_node.visited,
                                       down_node.visited))
    maze_array[current_node.y][current_node.x] = current_node
    print(current_node.data)

    pretty_print_maze(maze_array)
    sleep(0.05)

if __name__ == "__main__":

    file_path = "maps/map1.txt"
    maze_array = create_maze_array(file_path)
    #pretty_print_maze(maze_array)

    start_pnt = find_start(maze_array)
    mz_bfs = run_dfs_on_maze(maze_array,start_pnt)
    pretty_print_maze(maze_array)


