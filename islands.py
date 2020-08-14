#write the function that takes a 2d binary array and returns the nu,ber of 1
# islands. AN island consists of 1s that are conneted to thhe morth, south, east,
# or west. for example:

islands = [[0,1, 0, 1, 0],
          [1, 1, 0, 1, 1],
          [0, 0, 1, 0, 0],
          [1, 0, 1, 0, 0],
          [1, 1, 0, 0, 0]]

visited = [[False, False, False, False, False],
           [False, False, False, False, False],
           [False, False, False, False, False],
           [False, False, False, False, False]]


def island_counter(islands):
    #create a way to leep track of visited nodes
    visited = []
    for _ in range(len(islands)):
        new_row = [False] * len(islands[0])
        visited.append(new_row)

    print(visited)

    island_count = 0

    #walk through each cell in the grid

    for row in range(len(islands)):
        for col in range(len(islands[0])):
            #if its not visited
            if not visited[row][col]:
                #if its a 1:
                if islands[row][col] == 1:
                    # do a traversal 
                    dft(row, col, islands, visited)

                    #increment the counter
                    island_count += 1

    return island_count


def dft(row, col, islands, visited):
    s = Stack()

    s.push( (row, col) )

    while s.size() > 0:
        v = s.pop()
        row, col = v

        if not visited[row][col]:
            visited[row][col] = True

            for neighbor in get_neighbors(row, col, islands):
                s.push(neighbor)

def get_neighbors(row, col, islands):
    neighbors = []

    #check north
    if row > 0 and islands[row-1][col] == 1:
        neighbors.append((row-1, col))

    

island_counter(islands) # returns 4