from graph import Graph
from time import sleep
import copy

def run_iddfs_on_maze(maze_obj,start_pnt):
    """
    Iterative deepening function
    """
    max_depth = 0
    start_pnt.depth = 0

    while True :

        if max_depth == 600:
            break

        maze_test = copy.deepcopy(maze)
        result = depth_limited_search(maze_test, start_pnt, max_depth)
        #result.pretty_print_maze()
        max_depth += 1



def depth_limited_search(maze_obj,start_pnt , max_depth):
    """
    Depth  Limited Search using stack as the main data structure
    :param maze_obj: Graph object created from the text maze
    :param start_pnt: The starting point from the maze
    :param max_depth: The maximum depth to run the DFS
    :return: Result Graph data structure with the direction
    """
    frontier_stack = []
    frontier_stack.append(start_pnt)

    maze_array = maze_obj.get_maze_array()
    result_maze_obj = copy.deepcopy(maze_obj)
    result_maze_array = result_maze_obj.get_maze_array()

    while frontier_stack :

        current_node = frontier_stack.pop()
        current_node.visited = True
        current_node.added = True

        if(current_node.data == "*"):
            result_maze_obj.goals.append(current_node)

        result_maze_array[current_node.y][current_node.x] = current_node

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
                    right_node.parent = current_node
                    right_node.parent_direction = "Left"

                    right_node.depth = right_node.parent.depth + 1

                    if(max_depth >= right_node.depth):
                        frontier_stack.append(right_node)

            else:
                right_node.visited = True
                right_node.added = True

        if (current_node.x != 0):
            left_node = maze_array[current_node.y][current_node.x - 1]
            left_node_value = left_node.data

            if left_node_value != "=" and left_node_value != "|":
                if left_node.added is False and left_node.visited is False:
                    left_node.added = True
                    left_node.parent = current_node
                    left_node.parent_direction = "Right"

                    left_node.depth = left_node.parent.depth + 1

                    if(max_depth >= left_node.depth):
                        frontier_stack.append(left_node)

            else:
                left_node.visited = True
                left_node.added = True

        if (current_node.y != 0):
            up_node = maze_array[current_node.y - 1][current_node.x]
            up_node_value = up_node.data

            if up_node_value != "=" and up_node_value != "|":
                if up_node.added is False and up_node.visited is False:
                    up_node.added = True
                    up_node.parent = current_node
                    up_node.depth = up_node.parent.depth + 1
                    up_node.parent_direction = "Down"

                    if(max_depth >= up_node.depth):
                        frontier_stack.append(up_node)

            else:
                up_node.visited = True
                up_node.added = True

        if (current_node.y != (len(maze_array) - 1)):
            down_node = maze_array[current_node.y + 1][current_node.x]
            down_node_value = down_node.data

            if down_node_value != "=" and down_node_value != "|":
                if down_node.added is False and down_node.visited is False:
                    down_node.added = True
                    down_node.parent = current_node
                    down_node.depth = down_node.parent.depth + 1
                    down_node.parent_direction = "Up"

                    if(max_depth >= down_node.depth):
                        frontier_stack.append(down_node)
            else:
                down_node.visited = True
                down_node.added = True


        # Logic to check the direction of the parent
        if (current_node.parent_direction == "Up"):
            up_node.visited = False

        elif (current_node.parent_direction == "Down"):
            down_node.visited = False

        elif (current_node.parent_direction == "Left"):
            left_node.visited = False

        elif (current_node.parent_direction == "Right"):
            right_node.visited = False

        current_node.data = str(maze_obj.get_direction_symbol(right_node.visited,
                                                              left_node.visited,
                                                              up_node.visited,
                                                              down_node.visited))

        result_maze_array[current_node.y][current_node.x] = current_node

    return result_maze_obj


if __name__ == "__main__":

    file_path = "maps/map1.txt"

    maze = Graph()
    maze.create_maze_array(file_path)
    print("Maze Array : ")
    maze.pretty_print_maze()

    start_pnt = maze.get_start()
    run_iddfs_on_maze(maze, start_pnt)
    maze.print_goal_paths()