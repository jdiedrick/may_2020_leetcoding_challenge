class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        frequency_count = {}
        for s in magazine:
            if s in frequency_count:
                frequency_count[s] += 1
            else:
                frequency_count[s] = 1
        for s in ransomNote:
            if s not in frequency_count or frequency_count[s] == 0:
                return False
            else:
                frequency_count[s] -= 1
        return True
