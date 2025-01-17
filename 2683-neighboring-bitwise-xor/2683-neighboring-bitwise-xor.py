class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        
        # two ways
        o_1 = [1]
        o_0 = [0]
        for d in derived:
           # inverse of xor is xor

           n_1 = o_1[-1] ^ d
           n_0 = o_0[-1] ^ d
           o_1.append(n_1)
           o_0.append(n_0)
        # print("target", derived[-1])
        # print(o_1,o_1[-2] ^ o_1[0])
        # print(o_0,o_0[-2] ^ o_0[0])
        return o_1[-2] ^ o_1[0] == derived[-1] or  o_0[-2] ^ o_0[0] == derived[-1] 
