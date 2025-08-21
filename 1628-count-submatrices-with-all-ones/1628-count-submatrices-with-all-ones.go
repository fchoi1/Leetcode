func numSubmat(mat [][]int) int {
	m, n := len(mat), len(mat[0])
	res := 0
	row := make([][]int, m)
	for i := range row {
		row[i] = make([]int, n)
	}

	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if j == 0 {
				row[i][j] = mat[i][j]
			} else {
				if mat[i][j] == 0 {
					row[i][j] = 0
				} else {
					row[i][j] = row[i][j-1] + 1
				}
			}
			cur := row[i][j]
			for k := i; k >= 0; k-- {
				if row[k][j] < cur {
					cur = row[k][j]
				}
				if cur == 0 {
					break
				}
				res += cur
			}
		}
	}
	return res
}