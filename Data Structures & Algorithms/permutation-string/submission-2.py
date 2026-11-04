class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        target = {}
        window = {}
        size = len(s1)

        for char in s1:
            target[char] = target.get(char, 0) + 1

        for r, char in enumerate(s2):
            window[char] = window.get(char, 0) + 1

            # Remove the character that falls outside the window.
            if r >= size:
                left_char = s2[r - size]
                window[left_char] -= 1
                if window[left_char] == 0:
                    del window[left_char]

            if window == target:
                return True

        return False