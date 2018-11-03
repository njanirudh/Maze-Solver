from graph import Graph
from time import sleep
import os


def run_iddfs_on_maze(maze_obj,start_pnt):

    max_depth = 0

    while True :
        result = depth_limited_search(maze_obj, start_pnt, max_depth)
        result.pretty_print_maze()
        max_depth += 1
        print(max_depth)

def depth_limited_search(maze_obj,start_pnt , max_depth):

    frontier_stack = []
    frontier_stack.append(start_pnt)

    close_stack = []

    maze_array = maze_obj.get_maze_array()
    result_maze_obj = maze_obj
    result_maze_array = result_maze_obj.get_maze_array()

    current_depth = 0
    while frontier_stack :

        current_node = frontier_stack.pop()
        current_node.visited = True
        current_node.added = True
        current_node.data = "X"

        close_stack.append(current_node)

        result_maze_array[current_node.y][current_node.x] = current_node

        if current_depth <= max_depth:

            right_node = None
            left_node = None
            up_node = None
            down_node = None

            if (current_node.x != (len(maze_array[0]))):
                right_node = maze_array[current_node.y][current_node.x + 1]
                right_node_value = right_node.data

                if right_node_value != "=" and right_node_value != "|":
                    if right_node.added is False and right_node.visited is False:
                        right_node.added = True
                        frontier_stack.append(right_node)

            if (current_node.x != 0):
                left_node = maze_array[current_node.y][current_node.x - 1]
                left_node_value = left_node.data

                if left_node_value != "=" and left_node_value != "|":
                    if left_node.added is False and left_node.visited is False:
                        left_node.added = True
                        frontier_stack.append(left_node)

            if (current_node.y != 0):
                up_node = maze_array[current_node.y - 1][current_node.x]
                up_node_value = up_node.data

                if up_node_value != "=" and up_node_value != "|":
                    if up_node.added is False and up_node.visited is False:
                        up_node.added = True
                        frontier_stack.append(up_node)

            if (current_node.y != (len(maze_array) - 1)):
                down_node = maze_array[current_node.y + 1][current_node.x]
                down_node_value = down_node.data

                if down_node_value != "=" and down_node_value != "|":
                    if down_node.added is False and down_node.visited is False:
                        down_node.added = True
                        frontier_stack.append(down_node)

        # current_node.data = str(maze_obj.get_direction_symbol(right_node.visited,
        #                                                       left_node.visited,
        #                                                       up_node.visited,
        #                                                       down_node.visited))

            result_maze_array[current_node.y][current_node.x] = current_node

    return result_maze_obj


if __name__ == "__main__":

    file_path = "maps/map3.txt"
    maze = Graph()
    maze.create_maze_array(file_path)

    start_pnt = maze.get_start()
    run_iddfs_on_maze(maze, start_pnt)