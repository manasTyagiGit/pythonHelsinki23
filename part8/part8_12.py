def row_sums(my_matrix: list) :
    for row in my_matrix :
        row.append (sum(row))

    
my_matrix = [[1, 2], [3, 4]]
row_sums(my_matrix)
print(my_matrix)