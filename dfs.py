from graph import Graph
from time import sleep

def run_dfs_on_maze(maze_obj,start_pnt,result_maze_obj):
    """
    RECURSIVE Implementation of the DFS

    :param maze_obj: Pass the maze graph object created
    :param start_pnt: Pass the starting point of the Graph
    :param result_maze_obj: Result maze object of graph
    :return: None
    """

    # current_node refers to the node removed from queue and visited in the loop
    current_node = start_pnt
    current_node.visited = True
    current_node.added = True

    maze_array = maze_obj.get_maze_array()
    result_maze_array = result_maze_obj.get_maze_array()

    # Storing the goal to the result
    if (current_node.data == "*"):
        result_maze_obj.goals.append(current_node)

    result_maze_array[current_node.y][current_node.x] = current_node

    right_node = None
    left_node = None
    up_node = None
    down_node = None

    ## Using recursion to traverse all the children
    if (current_node.x != (len(maze_array[0]))):
        right_node = maze_array[current_node.y][current_node.x + 1]
        right_node_value = right_node.data

        if right_node_value != "=" and right_node_value != "|":
            if right_node.added is False and right_node.visited is False:
                right_node.visited = True
                right_node.parent = current_node
                right_node.parent_direction = "Left"
                run_dfs_on_maze(maze_obj, right_node,result_maze_obj)

        else:
            right_node.visited = True
            right_node.added = True



    if (current_node.x != 0):
        left_node = maze_array[current_node.y][current_node.x - 1]
        left_node_value = left_node.data

        if left_node_value != "=" and left_node_value != "|":
            if left_node.added is False and left_node.visited is False:
                left_node.visited = True
                left_node.parent = current_node
                left_node.parent_direction = "Right"
                run_dfs_on_maze(maze_obj, left_node,result_maze_obj)

        else:
            left_node.visited = True
            left_node.added = True

    if (current_node.y != 0):
        up_node = maze_array[current_node.y - 1][current_node.x]
        up_node_value = up_node.data

        if up_node_value != "=" and up_node_value != "|":
            if up_node.added is False and up_node.visited is False:
                up_node.visited = True
                up_node.parent = current_node
                up_node.parent_direction = "Down"
                run_dfs_on_maze(maze_obj, up_node ,result_maze_obj)
        else:
            up_node.visited = True
            up_node.added = True

    if (current_node.y != (len(maze_array) - 1)):
        down_node = maze_array[current_node.y + 1][current_node.x]
        down_node_value = down_node.data

        if down_node_value != "=" and down_node_value != "|":
            if down_node.added is False and down_node.visited is False:
                down_node.visited = True
                down_node.parent = current_node
                down_node.parent_direction = "Up"
                run_dfs_on_maze(maze_obj, down_node,result_maze_obj)

        else:
            down_node.visited = True
            down_node.added = True

    # Logic to check the direction of the parent
    if(current_node.parent_direction == "Up"):
        up_node.visited = False

    elif (current_node.parent_direction == "Down"):
        down_node.visited = False

    elif (current_node.parent_direction == "Left"):
        left_node.visited = False

    elif (current_node.parent_direction == "Right"):
        right_node.visited = False

    # Setting the unicode symbol depending on the path
    current_node.data = str(maze_obj.get_direction_symbol(right_node.visited,
                                                          left_node.visited,
                                                          up_node.visited,
                                                          down_node.visited))

    result_maze_array[current_node.y][current_node.x] = current_node

if __name__ == "__main__":

    file_path = "maps/map3.txt"
    maze = Graph()
    maze.create_maze_array(file_path)
    print("Maze Array : ")
    maze.pretty_print_maze()

    start_pnt = maze.get_start()

    result_maze_obj = maze
    run_dfs_on_maze(maze, start_pnt,result_maze_obj)

    print("Total Goals found :",len(result_maze_obj.goals))
    result_maze_obj.pretty_print_maze()
    result_maze_obj.print_goal_paths()