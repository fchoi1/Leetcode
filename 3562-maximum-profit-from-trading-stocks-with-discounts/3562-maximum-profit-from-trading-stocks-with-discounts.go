func maxProfit(n int, present []int, future []int, hierarchy [][]int, budget int) int {
	// Build tree
	tree := make([][]int, n)
	for _, e := range hierarchy {
		u, v := e[0]-1, e[1]-1
		tree[u] = append(tree[u], v)
	}

	// dp[u][parentBought][budget]
	dp := make([][][]int, n)
	for i := 0; i < n; i++ {
		dp[i] = make([][]int, 2)
		for j := 0; j < 2; j++ {
			dp[i][j] = make([]int, budget+1)
		}
	}

	max := func(a, b int) int {
		if a > b {
			return a
		}
		return b
	}

	var dfs func(int)
	dfs = func(u int) {
		// Process children first
		for _, v := range tree[u] {
			dfs(v)
		}

		// parentBought = 0 or 1
		for parentBought := 0; parentBought <= 1; parentBought++ {
			price := present[u]
			if parentBought == 1 {
				price /= 2
			}
			profit := future[u] - price

			curr := make([]int, budget+1)

			// -------- Option 1: do NOT buy u --------
			base := make([]int, budget+1)
			base[0] = 0

			for _, v := range tree[u] {
				next := make([]int, budget+1)
				for b1 := 0; b1 <= budget; b1++ {
					for b2 := 0; b1+b2 <= budget; b2++ {
						next[b1+b2] = max(next[b1+b2], base[b1]+dp[v][0][b2])
					}
				}
				base = next
			}

			for b := 0; b <= budget; b++ {
				curr[b] = max(curr[b], base[b])
			}

			// -------- Option 2: BUY u --------
			if price <= budget {
				baseBuy := make([]int, budget+1)
				baseBuy[0] = 0

				for _, v := range tree[u] {
					next := make([]int, budget+1)
					for b1 := 0; b1 <= budget; b1++ {
						for b2 := 0; b1+b2 <= budget; b2++ {
							next[b1+b2] = max(next[b1+b2], baseBuy[b1]+dp[v][1][b2])
						}
					}
					baseBuy = next
				}

				for b := price; b <= budget; b++ {
					curr[b] = max(curr[b], baseBuy[b-price]+profit)
				}
			}

			dp[u][parentBought] = curr
		}
	}

	dfs(0)

	// Root has no parent → parentBought = 0
	ans := 0
	for b := 0; b <= budget; b++ {
		ans = max(ans, dp[0][0][b])
	}
	return ans
}
