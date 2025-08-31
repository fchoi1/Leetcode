class Solution(object):
    def solveSudoku(self,board):
        R=[set()for _ in range(9)] #only 7 testcases here we can use list
        C=[set()for _ in range(9)] #making 9 empty spaces in all 3
        B=[set()for _ in range(9)]
        E=[] #stores empty
        for r in range(9):
            for c in range(9):
                if board[r][c]==".":
                    E.append((r,c))
                else: #if element is not empty
                    ch=board[r][c] #update in R,C,B lists
                    R[r].add(ch) #add to row no.
                    C[c].add(ch) #add to col no.
                    B[(r//3)*3+(c//3)].add(ch) #add to block no
        def f(k):
            if k==len(E):
                return 1 #for last index return True (1)
            r,c=E[k]
            b=(r//3)*3+(c//3) #block no.
            for ch in"123456789":
                if ch not in R[r]and ch not in C[c]and ch not in B[b]: #checking not in all
                    board[r][c]=ch #adding to the cell
                    R[r].add(ch)
                    C[c].add(ch) #update in all R,C,B lists of this index 
                    B[b].add(ch)
                    if f(k+1):  #checking if the next is last element
                        return 1
                    board[r][c]="."
                    R[r].remove(ch)
                    C[c].remove(ch) #claning the records
                    B[b].remove(ch)
            return 0
        f(0)
