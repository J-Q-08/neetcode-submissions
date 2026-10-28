class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            currentsum = numbers[l] + numbers[r]
            if currentsum == target:
                return [l + 1, r + 1]
            elif currentsum < target:
                l += 1
            elif currentsum > target:
                r -= 1