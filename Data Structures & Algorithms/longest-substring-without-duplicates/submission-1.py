class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r, maxlength = 0, 0, 0
        hashmap = set()
        while r < len(s):
            if s[r] in hashmap:
                hashmap.discard(s[l])
                l += 1
            else:
                hashmap.add(s[r])
                maxlength = max(maxlength, r - l + 1)
                r += 1
        return maxlength
