class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        mod = 10**9 + 7

        curr_sum = 0
        curr_s = ""

        slice_list = [(0, 0)]

        pref = [0]
        pow10 = [1]
        ans = []

        for ch in s:
            if ch != '0':
                curr_sum += int(ch)
                curr_s += ch

                pref.append((pref[-1] * 10 + int(ch)) % mod)
                pow10.append((pow10[-1] * 10) % mod)

            slice_list.append((curr_sum, len(curr_s)))

        for l,r in queries:
            l_sum, l_idx = slice_list[l]
            r_sum, r_idx = slice_list[r + 1]

            digit_sum = r_sum - l_sum

            if digit_sum == 0:
                ans.append(0)
                continue

            num = (pref[r_idx] - pref[l_idx] * pow10[r_idx - l_idx]) % mod

            ans.append(digit_sum * num % mod)

        return ans