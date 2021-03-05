#!/usr/bin/env python3
# https://en.wikipedia.org/wiki/Sudoku
subtract_set = {1,2,3,4,5,6,7,8,9}

def check_horizontal(i,j):
    return subtract_set - set(contrainer[i])
    
def check_vertical(i,j):
    ret_set = []
    for x in range(9) :
        ret_set.append(container[x][j])
    return subtract_set - set(ret_set)    
    
def check_square(i,j):
    first = [0,1,2]
    second = [3,4,5]
    third = [6,7,8]
    find_square = [first, second, third]
    for l in find_square :
        if i in l:
            row = 1
        if j in l:
            col = 1
    return_set = []
    for x in row:
        for y in col:
            return_set.append(container[x][y])
    return subtract_set - set(return_set)
    
    
def get_poss_vals(i, j):
    poss_vals = list(check_square(i, j) \
                    .intersection(check_horizontal(i, j)) \
                    .intersection(check_vertical(i, j)))
    return poss_vals
 
def explicit_solver(container):
    for i in range(9):
        for j in range(9):
            if container[i][j] == 0:
                poss_vals = get_poss_vals(i,j)
                if len(poss_vals) == 1:
                    container[i][j] = list(poss_vals)[0]
                    print_container(container)
    return container 
    
  
 def implicit_solver(i,j,container):
    if container[i][j] == 0:
        poss_vals = get_poss_vals(i,j)
        
        # check rows
        row_poss = []
        for y in range(9):
            if y ==j:
                continue
            if container[i][y] == 0:
                for val in get_poss_vals(i,y):
                    row_poss.append(val)
        if len(set(poss_vals)-set(row_poss)) == 1:
            container[i][j] = list(set(poss_vals)-set(row_poss))[0]
            print_container(container)
            
        # check column
        col_poss = []
        for x in range(9):
            if x == i:
                continue
            if container[x][j] == 0:
                for val in get_poss_vals(x, j):
                    col_poss.append(val)
        if len(set(poss_vals)-set(col_poss)) == 1:
            container[i][j] = list(set(poss_vals)-set(col_poss))[0]
            print_container(container)
        
        # check square
        first = [0, 1, 2]
        second = [3, 4, 5]
        third = [6, 7, 8]
        find_square = [first, second, third]
        for l in find_square:
            if i in l:
                row = l
            if j in l:
                col = l
        square_poss = []
        for x in row:
            for y in col:
                if container[x][y] == 0:
                    for val in get_poss_vals(x, y):
                        square_poss.append(val)
        if len(set(poss_vals)-set(square_poss)) == 1:
          container[i][j] = list(set(poss_vals)-set(square_poss))[0]
          print_container(container)

    return container
