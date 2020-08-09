# bin /dash
from collections import deque 

def the_hunter(hunter):
    return hunter[-1] == 'l' # a dumb way to find the hunter 

graph = {}
graph["Carlos"] = ['Lucas', 'Jhony', 'Paul']
graph["Lucas"] = ['Michael', 'Jeff']
graph['Jhony'] = ['George','Jeff']
graph['Paul'] = []
graph['Michael'] = ['Cory']
graph['Cory'] = ['Mike']
graph['Mike'] = []
graph['Jeff'] = []

# O(3)

def search(hunter):
    search_queue = deque()
    search_queue += graph[hunter]
    searched = []
    
    # this loop will check if the hunter is in the queue 2 times;
    while search_queue:
        neighbor = search_queue.popleft() # take the first left name 
        # only search this neighbor if you haven't already searched them
        if neighbor not in searched: 
            if the_hunter(neighbor):
                print(neighbor + " Is the hunter. Yeaaah")
                return True
            else:
                search_queue += graph[hunter]
                # mark this person as searched
                searched.append(hunter)
               
                '''
                # this will take the len of graph and see if it's correct.
                n = len(graph)
                if n >=  8:
                    print('done --> 99')
                '''    

    return False
search('Carlos')

# create a sample that find the number of both ways to the result and say if it's done

