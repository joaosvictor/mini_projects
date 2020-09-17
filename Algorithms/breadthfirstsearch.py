from collections import deque
#enque = add to right/deque = remove from left.

def country_neighbor_brazil(country):
	return country[-1]=='a'#a dumb way to find the neighbor with the last letter of the word with 'a'
	
graph = {} #here the hash function  
graph["Brazil"]=["Argentina","Peru","USA"]
graph["Argentina"]=["Chile"]
graph["Peru"]=["Venezuela"]
graph["USA"]=["Canada"]

def search(country):
	search_queue = deque()
	search_queue += graph[country] #same like search_queue = search_queue + 1.
	searched=[]
	#this loop below will check if the person is in the queue 2 times
	while search_queue:
		neighbor = search_queue.popleft()#take the first left Nº
		#only search this neighbor if you haven't already searched them
		if neighbor not in searched:
			if country_neighbor_brazil(neighbor):
				print(neighbor + " is a Brazil neighbor!")
				return True
			else:
				search_queue += graph[country]
				#mark this person as searched
				searched.append(country)
	return False 
search("Brazil")
	

		
