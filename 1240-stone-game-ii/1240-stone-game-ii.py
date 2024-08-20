from functools import cache

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        
		# Constants
        ALICE = 1 # To represent current turn.
        BOB = -1 # To represent current turn.
        N = len(piles)
        
		# Helpers
        @cache
        def max_piles_from(idx, m, turn): # Returns alice's gain from the given state.
            if idx == N:
                return 0
		
            # Note: We need to maximize alice's gain in alice's turn, minimize alice's gain in bob's turn.
            localMax = 0
            localMin = float('inf')
            turnSum = 0
            
			# Try all choices.
            for x in range(1, min(2*m, N-idx) + 1): # harvesting index's upper is N-1.
                harvesting_idx = idx + x - 1
                turnSum += piles[harvesting_idx]
                next_m = max(m, x)
                
                current_turn_gain = turnSum if turn == ALICE else 0
                future_gain = max_piles_from(harvesting_idx+1, next_m, -turn) # Switching turn by multipling -1.
                
                localMax = max(localMax, current_turn_gain + future_gain)
                localMin = min(localMin, current_turn_gain + future_gain)
                
            return localMax if turn == ALICE else localMin
        
        # Main
        return max_piles_from(0, 1, ALICE)