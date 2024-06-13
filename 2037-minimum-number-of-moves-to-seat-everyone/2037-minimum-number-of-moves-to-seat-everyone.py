class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        moves = 0
        for i,j in zip(seats, students):
            moves += abs(i-j)
        return moves
        