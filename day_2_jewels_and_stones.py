class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        result = 0
        stone_freq = {}
        for s in S:
            if s in stone_freq:
                stone_freq[s] += 1
            else:
                stone_freq[s] = 1
        
        for j in J:
            if j in stone_freq:
                result += stone_freq[j]
        return result
