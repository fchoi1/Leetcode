class Solution:
    def distMoney(self, money: int, children: int) -> int:
        
        money -= children
        if money < 0:
            return -1

        fill = 0
        while money >= 7 and children > 0:
            fill += 1
            money -= 7
            children -= 1
        
        if money == 3 and children <= 1:
            return max(0, fill - 1)

        if money != 0 and children == 0:
            return fill - 1
        
        return fill
        
