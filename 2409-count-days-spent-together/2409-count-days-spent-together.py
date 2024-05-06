class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        prefix = [0]
        for d in days:
            prefix.append(prefix[-1] + d)
        
        alice = (prefix[int(arriveAlice[:2])-1] - int(arriveAlice[2:]), prefix[int(leaveAlice[:2])-1] - int(leaveAlice[2:]))
        bob = (prefix[int(arriveBob[:2])-1] - int(arriveBob[2:]), prefix[int(leaveBob[:2])-1] - int(leaveBob[2:]))
        print(bob, alice, int(arriveAlice[:2])-1,int(arriveAlice[2:]), int(leaveAlice[:2])-1, int(leaveAlice[2:]))

        if alice[0] > bob[1] or bob[0] > alice[1]:
            return 0
        return min(alice[1], bob[1]) - max(alice[0], bob[0]) + 1



