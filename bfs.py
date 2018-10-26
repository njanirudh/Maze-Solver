from collections import deque

class Node :
    def __init__(self,in_x=0,in_y=0):
         self.x = in_x
         self.y = in_y
         self.data = None
         self.visited = False

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



# def pretty_print_maze(text):
#     for arr in text:
#         print(arr)

def pretty_print_maze(node_matrix):

    for node_array in node_matrix:
        for node in node_array:
            print(node,end = "")
        print()



def run_bfs_on_maze(maze,start_pnt):

    frontier_queue = deque()
    frontier_queue.append(start_pnt)

    while len(frontier_queue) != 0 :
        current_node = frontier_queue.popleft()
        current_node.visited = True

        if(current_node.x != (len(maze[0]))):
            right_node = maze[ current_node.y][current_node.x + 1 ]
            right_node_value = right_node.data

            if right_node_value != "=" or right_node_value != "|":
                if right_node.visited is False:
                    frontier_queue.append(right_node)

        if(current_node.x != 0):
            left_node = maze[ current_node.y][current_node.x - 1 ]
            left_node_value = left_node.data

            if left_node_value != "=" or left_node_value != "|":
                if left_node.visited is False:
                    frontier_queue.append(left_node)

        if (current_node.y != 0):
            up_node = maze[ current_node.y - 1][current_node.x ]
            up_node_value = up_node.data

            if up_node_value != "=" or up_node_value != "|":
                if up_node.visited is False:
                    frontier_queue.append(up_node)

        if(current_node.y != (len(maze)-1)):
            down_node = maze[ current_node.y + 1][current_node.x ]
            down_node_value  = down_node.data

            if down_node_value != "=" or down_node_value != "|":
                if down_node.visited is False:
                    frontier_queue.append(down_node)


if __name__ == "__main__":

    file_path = "maps/map1.txt"
    maze_array = create_maze_array(file_path)
    pretty_print_maze(maze_array)

    start_pnt = find_start(maze_array)
    #print(start_pnt)
    #run_bfs_on_maze(maze_array,start_pnt)

    #print(maze_array[1][0])

