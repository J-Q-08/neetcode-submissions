class Solution:
    def trap(self, height: List[int]) -> int:
        l,r = 0, len(height) - 1
        maxleft = height[0]
        maxright = height[len(height) - 1]
        trappedwater = 0

        while l < r:
            if height[l] <= height[r]:
                l += 1
                if maxleft > height[l]:
                    trappedwater += maxleft - height[l]
                maxleft = max(maxleft, height[l])

            elif height[l] > height[r]:
                r -= 1
                if maxright > height[r]:
                    trappedwater += maxright - height[r]
                maxright = max(maxright, height[r])
        return trappedwater