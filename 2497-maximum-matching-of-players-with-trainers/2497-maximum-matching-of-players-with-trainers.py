class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        valid = t = p = 0

        while t < len(trainers):

            if p >= len(players):
                break
            
            if players[p] <= trainers[t]:
                p += 1
                valid += 1
            
            t += 1


        return valid 