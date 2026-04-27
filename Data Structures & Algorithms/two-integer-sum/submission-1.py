class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        

        if len(nums) == 0:
            return []

        from collections import defaultdict
        prev = defaultdict()
        for i in range(len(nums)):
            visited = target - nums[i]
            if visited in prev:
                return [prev[visited], i]
            
            prev[nums[i]] = i
        return []