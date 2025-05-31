def column_correct(list : list, column_num : int) -> bool :
    new_list = []
    for i in range(len(list)): 
        if list[i][column_num] > 0 and  list[i][column_num] in new_list:
            return False
        else:
            new_list.append(list[i][column_num])

    return True

def row_correct (sudoku : list, rowNum) -> bool :
    row = sudoku[rowNum]

    for i in range (1, 10) :
        if row.count(i) > 1 :
            return False
        
    return True

def block_correct (sudoku : list, r, c) -> bool :

    new_list = []

    for i in range (r, r + 3) :
        for j in range (c, c + 3) :            
            if sudoku[i][j] > 0 and sudoku[i][j] in new_list :
                return False
            else :
                new_list.append (sudoku[i][j])


    return True 

def sudoku_grid_correct (sudoku : list) -> bool :
    correct = True

    for i in range (0, 9) :
        correct = row_correct (sudoku, i)
        if correct == False :
            return False
        
    for i in range (0, 9) :
        correct = column_correct (sudoku, i)
        if correct == False :
            return False
        
    for i in range (0, 7, 3) :
        for j in range (0, 7, 3) :
            correct = block_correct (sudoku, i, j)
            if correct == False : return False      
    

    return True

if __name__ == "__main__" :

    sudoku1 = [
    [9, 0, 0, 0, 8, 0, 3, 0, 0],
    [2, 0, 0, 2, 5, 0, 7, 0, 0],
    [0, 2, 0, 3, 0, 0, 0, 0, 4],
    [2, 9, 4, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 7, 3, 0, 5, 6, 0],
    [7, 0, 5, 0, 6, 0, 4, 0, 0],
    [0, 0, 7, 8, 0, 3, 9, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 3],
    [3, 0, 0, 0, 0, 0, 0, 0, 2]
    ]

    print(sudoku_grid_correct(sudoku1))

    sudoku2 = [
    [2, 6, 7, 8, 3, 9, 5, 0, 4],
    [9, 0, 3, 5, 1, 0, 6, 0, 0],
    [0, 5, 1, 6, 0, 0, 8, 3, 9],
    [5, 1, 9, 0, 4, 6, 3, 2, 8],
    [8, 0, 2, 1, 0, 5, 7, 0, 6],
    [6, 7, 4, 3, 2, 0, 0, 0, 5],
    [0, 0, 0, 4, 5, 7, 2, 6, 3],
    [3, 2, 0, 0, 8, 0, 0, 5, 7],
    [7, 4, 5, 0, 0, 3, 9, 0, 1]
    ]

    print(sudoku_grid_correct(sudoku2))