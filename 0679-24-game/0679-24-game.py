class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:

        # brute force
        # 4! = 4 * 3 * 2 * 1 = 24

        # brackets for plus and minus order


        # allocate symbols for  * + - /
        # solve after

        self.valid = False

        def allocate(strOp):
            if self.valid:
                return
            if len(strOp) == 3:
                check(strOp)
                return
            
            for sym in "*-/+":
                allocate(strOp + sym)

        
        operations = [[0,1,2], [0,2,1], [1,0,2], [1,2,0], [2,1,0], [2,0,1]]
       
        ops = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv  
        }
        # Try all bracket placements for one permutation and one operator combo
        def check(strOp):
            for nums in itertools.permutations(cards):
                a, b, c, d = nums
                op1, op2, op3 = strOp[0], strOp[1], strOp[2]

                try:
                    # ((a op1 b) op2 c) op3 d
                    res1 = ops[op3](ops[op2](ops[op1](a, b), c), d)
                    # (a op1 (b op2 c)) op3 d
                    res2 = ops[op3](ops[op1](a, ops[op2](b, c)), d)
                    # a op1 ((b op2 c) op3 d)
                    res3 = ops[op1](a, ops[op3](ops[op2](b, c), d))
                    # a op1 (b op2 (c op3 d))
                    res4 = ops[op1](a, ops[op2](b, ops[op3](c, d)))
                    # (a op1 b) op2 (c op3 d)
                    res5 = ops[op2](ops[op1](a, b), ops[op3](c, d))

                    for res in [res1, res2, res3, res4, res5]:
                        if abs(res - 24) < 1e-6:
                            self.valid = True
                            return
                except ZeroDivisionError:
                    continue

        # Start generating operator combinations
        allocate("")
        return self.valid
        