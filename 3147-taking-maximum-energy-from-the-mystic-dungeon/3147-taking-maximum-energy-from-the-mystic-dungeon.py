class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        
        currEnergy = [val for val in energy[:k]]
        for i in range(k,len(energy), k):
            for j in range(k):
                if j + i < len(energy):
                    if currEnergy[j] < 0:
                        currEnergy[j] = energy[j+i]
                    else:
                        currEnergy[j] += energy[j+i] 
        
        return max(currEnergy)
        