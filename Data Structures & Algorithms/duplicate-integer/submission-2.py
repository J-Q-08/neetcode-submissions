class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        empty_dictionary = {}
        for num in nums:
            if num in empty_dictionary:
                return True
            else: 
                empty_dictionary[num] = num
        return False
