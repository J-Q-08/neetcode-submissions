class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorted_s = []
        sorted_t = []
        for letter in s:
            sorted_s.append(letter)
        for letter in t:
            sorted_t.append(letter)
        list.sort(sorted_s)
        list.sort(sorted_t)
        if sorted_s == sorted_t:
            return True
        return False