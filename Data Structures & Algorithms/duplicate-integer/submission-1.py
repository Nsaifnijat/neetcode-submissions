class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == 0:
            return False
        
        prev = []
        for i in range(len(nums)):
            if nums[i] in prev:
                    return True
            prev.append(nums[i])

        return False