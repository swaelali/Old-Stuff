def weak_point(matrix):
	rows_sums =[]
	cols_sums=[]
	cols =[[]*i for i in range(len(matrix))]
	for i in range(len(matrix)):
		rows_sums.append(sum(matrix[i]))
		for j in range(len(matrix)):
			cols[j].append(matrix[i][j])
	for i in range(len(matrix)):
		cols_sums.append(sum(cols[i]))
	row_index = rows_sums.index(min(rows_sums))
	col_index = cols_sums.index(min(cols_sums))
	return [row_index, col_index]
	
	
print weak_point([[7, 2, 7, 2, 8],
            [2, 9, 4, 1, 7],
            [3, 8, 6, 2, 4],
            [2, 5, 2, 9, 1],
            [6, 6, 5, 4, 5]])
