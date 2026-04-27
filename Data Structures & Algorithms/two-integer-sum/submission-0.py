class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        prevVal = {}

        for i, n in enumerate(nums):
            diff = target - n 
            if diff in prevVal:
                return [prevVal[diff],i]
            prevVal[n] = i
        return False
            