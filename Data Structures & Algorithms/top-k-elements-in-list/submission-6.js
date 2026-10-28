class Solution {
    topKFrequent(nums, k) {
        const counter = {};

        for (let i = 0; i < nums.length; i++) {
            if (Object.hasOwn(counter, nums[i])) {
                counter[nums[i]]++;
            } else {
                counter[nums[i]] = 1;
            }
        }

        const array = [];

        for (const [key, value] of Object.entries(counter)) {
            array.push([value, Number(key)]);
        }

        array.sort((a, b) => a[0] - b[0]);

        const res = [];
        while (res.length < k) {
            res.push(array.pop()[1]);
        }

        return res;
    }
}