class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = []
        right = [1] * len(nums)
        final = []
        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                right[i] = 1
            else: right[i] = right[i + 1] * nums[i + 1]
        for i in range(len(nums)):
            if i == 0:
                left.append(1)
            else:
                left.append(left[i - 1] * nums[i - 1])
            final.append(left[i] * right[i])
        return final