class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l, r, = 0, 0
        dictionary = {}
        checked = {}
        if len(s1) > len(s2):
            return False
        for char in s1:
            checked[char] = checked.get(char, 0) + 1
        while r < len(s2):
            while r < len(s1):
                dictionary[s2[r]] = dictionary.get(s2[r], 0) + 1
                r += 1
            if dictionary == checked:
                return True
            elif r == len(s2):
                return False
            else:
                dictionary[s2[l]] -= 1
                if dictionary[s2[l]] == 0:
                    del dictionary[s2[l]]
                dictionary[s2[r]] = dictionary.get(s2[r], 0) + 1
                l += 1
                r += 1
                if dictionary == checked:
                    return True
        return False