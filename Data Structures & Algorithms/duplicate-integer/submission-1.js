class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        const numMap = new Map();
        for (let i = 0; i < nums.length; i++) {
            const checked = nums[i];
            if (numMap.has(checked)) {
                return true;
            }
            numMap.set(nums[i], i);
        }
        return false;
    }
}
