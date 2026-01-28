import (
	"container/heap"
	"math"
	"sort"
)

type Cell struct {
	val int
	i   int
	j   int
}

type State struct {
	cost int
	i    int
	j    int
	t    int
}

type PQ []State

func (pq PQ) Len() int { return len(pq) }
func (pq PQ) Less(i, j int) bool { return pq[i].cost < pq[j].cost }
func (pq PQ) Swap(i, j int) { pq[i], pq[j] = pq[j], pq[i] }
func (pq *PQ) Push(x interface{}) { *pq = append(*pq, x.(State)) }
func (pq *PQ) Pop() interface{} {
	old := *pq
	n := len(old)
	x := old[n-1]
	*pq = old[:n-1]
	return x
}

func minCost(grid [][]int, k int) int {
	n := len(grid)
	m := len(grid[0])

	// All cells sorted by value descending
	vals := make([]Cell, 0, n*m)
	for i := 0; i < n; i++ {
		for j := 0; j < m; j++ {
			vals = append(vals, Cell{grid[i][j], i, j})
		}
	}
	sort.Slice(vals, func(i, j int) bool { return vals[i].val > vals[j].val })

	// Available teleport cells for each teleport count
	available := make([][]Cell, k)
	for i := 0; i < k; i++ {
		available[i] = append([]Cell(nil), vals...)
	}

	const INF = math.MaxInt32 / 2
	shortest := make([][][]int, n)
	for i := 0; i < n; i++ {
		shortest[i] = make([][]int, m)
		for j := 0; j < m; j++ {
			shortest[i][j] = make([]int, k+1)
			for t := 0; t <= k; t++ {
				shortest[i][j][t] = INF
			}
		}
	}

	pq := &PQ{}
	heap.Init(pq)
	shortest[0][0][0] = 0
	heap.Push(pq, State{0, 0, 0, 0})

	for pq.Len() > 0 {
		cur := heap.Pop(pq).(State)
		cost, i, j, t := cur.cost, cur.i, cur.j, cur.t

		if cost > shortest[i][j][t] || (t > 0 && cost >= shortest[i][j][t-1]) {
			continue
		}

		if i == n-1 && j == m-1 {
			return cost
		}

		// Move down
		if i+1 < n {
			nc := cost + grid[i+1][j]
			if nc < shortest[i+1][j][t] {
				shortest[i+1][j][t] = nc
				heap.Push(pq, State{nc, i + 1, j, t})
			}
		}

		// Move right
		if j+1 < m {
			nc := cost + grid[i][j+1]
			if nc < shortest[i][j+1][t] {
				shortest[i][j+1][t] = nc
				heap.Push(pq, State{nc, i, j + 1, t})
			}
		}

		// Teleport
		if t < k {
			for len(available[t]) > 0 && available[t][len(available[t])-1].val <= grid[i][j] {
				c := available[t][len(available[t])-1]
				if cost < shortest[c.i][c.j][t+1] {
					shortest[c.i][c.j][t+1] = cost
					heap.Push(pq, State{cost, c.i, c.j, t + 1})
				}
				available[t] = available[t][:len(available[t])-1]
			}
			for p := t + 1; p < k; p++ {
				for len(available[p]) > 0 && available[p][len(available[p])-1].val <= grid[i][j] {
					available[p] = available[p][:len(available[p])-1]
				}
			}
		}
	}

	return -1
}