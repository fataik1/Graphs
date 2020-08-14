from room import Room
from player import Player
from world import World
from util import Stack, Queue

import random
from ast import literal_eval

# Load world
world = World()

file_path = 'C://Users//kingf//Desktop//33//Graphs//projects//adventure//maps//'

# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = file_path + "main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

visited = {}

paths = {
    'n': 's',
    's': 'n',
    'e': 'w',
    'w': 'e'
}

# stack is here to hold the paths we have traveled to
s = Stack()

# want to mark down the current room while we visit it
visited[player.current_room.id] = player.current_room.get_exits()

while len(visited) < len(room_graph):

    # if current room has not been visited
    if player.current_room.id not in visited:
        #add room as a key to visited, with  get_exits as its values
        visited[player.current_room.id] = player.current_room.get_exits()

        #want to grab the last direction & put on the stack. opposite direction so we can get to the current room.
        old_room = s.stack[-1]

        # going to want to remove that direction from the current room's exit
        #don't want to go back to previous room until needed to
        visited[player.current_room.id].remove(old_room)

    #if current room has no remaining exits to be tried
    if len(visited[player.current_room.id]) == 0:
        # want to pop the top of the stack and assign it to the direction to travel
        old_room = s.pop()
        # traverse back
        player.travel(old_room)
        # add previous room to the traversal directions
        traversal_path.append(old_room)
    else:
        #choose a direction to go
        direction = visited[player.current_room.id].pop()
        # travel in that direction
        player.travel(direction)
        # add it to the traversal direction
        traversal_path.append(direction)
        #push to the paths directon
        s.push(paths[direction])

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
# #######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
