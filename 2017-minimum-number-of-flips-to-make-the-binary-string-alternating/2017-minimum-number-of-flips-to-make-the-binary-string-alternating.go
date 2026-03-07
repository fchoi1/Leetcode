func minFlips(s string) int {
    n := len(s)
    t := s + s

    mis0 := 0
    ans := n

    for i := 0; i < 2*n; i++ {

        expected := byte('0')
        if i%2 == 1 {
            expected = '1'
        }

        if t[i] != expected {
            mis0++
        }

        if i >= n {
            left := i - n
            expLeft := byte('0')
            if left%2 == 1 {
                expLeft = '1'
            }
            if t[left] != expLeft {
                mis0--
            }
        }

        if i >= n-1 {
            mis1 := n - mis0
            ans = min(ans, min(mis0, mis1))
        }
    }

    return ans
}

func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}