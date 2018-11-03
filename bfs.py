import queue
from graph import Graph
from time import sleep


def run_bfs_on_maze(maze_obj,start_pnt):

    frontier_queue = queue.Queue()
    frontier_queue.put(start_pnt)

    result_maze_obj = maze_obj
    maze_array = maze_obj.get_maze_array()
    result_maze_array = result_maze_obj.get_maze_array()

    while not frontier_queue.empty():
        current_node = frontier_queue.get()
        current_node.visited = True
        current_node.added = True

        if(current_node.data == "*"):
            result_maze_obj.goals.append(current_node)

        result_maze_array[current_node.y][current_node.x]=current_node

        right_node = None
        left_node = None
        up_node = None
        down_node = None

        if(current_node.x != (len(maze_array[0]))):
            right_node = maze_array[ current_node.y][current_node.x + 1 ]
            right_node_value = right_node.data

            if right_node_value != "=" and right_node_value != "|":
                if right_node.added is False and right_node.visited is False:
                    right_node.added = True
                    right_node.parent = current_node
                    frontier_queue.put(right_node)

        if(current_node.x != 0):
            left_node = maze_array[ current_node.y][current_node.x - 1 ]
            left_node_value = left_node.data

            if left_node_value != "=" and left_node_value != "|":
                if left_node.added is False and left_node.visited is False:
                    left_node.added = True
                    left_node.parent = current_node
                    frontier_queue.put(left_node)

        if (current_node.y != 0):
            up_node = maze_array[ current_node.y - 1][current_node.x ]
            up_node_value = up_node.data

            if up_node_value != "=" and up_node_value != "|":
                if up_node.added is False and up_node.visited is False:
                    up_node.added = True
                    up_node.parent = current_node
                    frontier_queue.put(up_node)

        if(current_node.y != (len(maze_array)-1)):
            down_node = maze_array[ current_node.y + 1][current_node.x ]
            down_node_value  = down_node.data

            if down_node_value != "=" and down_node_value != "|":
                if down_node.added is False  and down_node.visited is False:
                    down_node.added = True
                    down_node.parent = current_node
                    frontier_queue.put(down_node)

        current_node.data = str(maze_obj.get_direction_symbol(right_node.visited,
                                           left_node.visited,
                                           up_node.visited,
                                           down_node.visited))

        result_maze_array[current_node.y][current_node.x]=current_node
        #Graph(result_maze_array).pretty_print_maze()

    return result_maze_obj


if __name__ == "__main__":

    file_path = "maps/map1.txt"
    maze = Graph()
    maze.create_maze_array(file_path)

    start_pnt = maze.get_start()
    result_maze = run_bfs_on_maze(maze,start_pnt)

    print(len(result_maze.goals))
    result_maze.pretty_print_maze()



