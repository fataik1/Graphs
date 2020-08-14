import string

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

# Raed words in from the file, add to set of the words

    word_set = set()

    with open("x.txt") as f:
        for word in f: # for each line of the ifle
            word_set.add(word.strip().lower())
def get_neighbors(word):
    word_letters = list(word) 

    for i in range(len(word_letters)):
        for letter in list(string.ascii_lowercase):

            # Make a copy of the word
            temp_word = list(word_letters)

            # Substitute the letter into the word copy
            temp_word[i] = letter

            # Make it string
            temp_word_str = "".join(temp_word)

            # If it's a real world, add it to the return set
            if temp_word_str != word and temp_word_str in word_set:
                neighbors.append(temp_word_str)

    return neighbors





def find_word_ladder(begin_word, end_word): #BFS
    visited = set()

    q = Queue()

    q.enqueue([begin_word])

    while q.size() > 0:
        path = q.dequeue()

        v = path[-1]

        if v not in visited:
            visited.add(v)

            if v == end_word:
                return path
            
            for neighbor in get_neighbors(v):
                path_copy = list(path)
                path_copy.append(neighbor)
                q.enqueue(path_copy)

    #If we got here, didn't find a path
    return None


print(find_word_ladder("sail", "boat"))