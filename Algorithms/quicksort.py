def quicksort(array):
  # in quicksort you must have a pivot in the code
  # the pivot will take a random No in the list/array, usually the mid number 
  if len(array) < 2:# if <2 return, 'cause think if the element is the first No ? you'll waste time finding in the mid. 
    return array
  else:
    pivot = array[0]#remember this '[0]' is the index of the array.
    less = [i for i in array[1:] if i <= pivot]
    greater = [i for i in array[1:] if i > pivot]
    return quicksort(less) + [pivot] + quicksort(greater)

print(quicksort([10, 5, 2, 3]))#->2,3,5,10
# if you use this code for a cp you can use in that way print(quicksort(list(int,input().split())))
