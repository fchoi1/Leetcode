from typing import List
import itertools
import operator

class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        # Map symbols to actual operation functions
        ops = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': lambda a, b: a / b if abs(b) > 1e-6 else float('inf')  # handle div by zero
        }

        # Try all the 5 valid parenthesis combinations
        def try_all_expressions(a, b, c, d, op1, op2, op3):
            try:
                # ((a op1 b) op2 c) op3 d
                if abs(ops[op3](ops[op2](ops[op1](a, b), c), d) - 24) < 1e-6:
                    return True
                # (a op1 (b op2 c)) op3 d
                if abs(ops[op3](ops[op1](a, ops[op2](b, c)), d) - 24) < 1e-6:
                    return True
                # a op1 ((b op2 c) op3 d)
                if abs(ops[op1](a, ops[op3](ops[op2](b, c), d)) - 24) < 1e-6:
                    return True
                # a op1 (b op2 (c op3 d))
                if abs(ops[op1](a, ops[op2](b, ops[op3](c, d))) - 24) < 1e-6:
                    return True
                # (a op1 b) op2 (c op3 d)
                if abs(ops[op2](ops[op1](a, b), ops[op3](c, d)) - 24) < 1e-6:
                    return True
            except ZeroDivisionError:
                return False
            return False

        # Try every permutation of numbers and every combination of 3 operators
        for nums in itertools.permutations(cards):
            for ops_combo in itertools.product(['+', '-', '*', '/'], repeat=3):
                if try_all_expressions(*nums, *ops_combo):
                    return True

        return False
