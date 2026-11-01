class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r, maxlength = 0, 0, 0
        dictionary = {}
        while r < len(s):
            dictionary[s[r]] = dictionary.get(s[r], 0) + 1
            r += 1
            while sum(dictionary.values()) - max(dictionary.values()) > k:
                dictionary[s[l]] -= 1
                l += 1
            maxlength = max(maxlength, r - l)
        return maxlength
            