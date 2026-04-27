class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        

        vals = set(nums)

        longest = 0

        for i in range(len(nums)):
            
            if nums[i] - 1 in vals:
                continue
            length = 1
            while nums[i] + length in vals:
                length +=1
            

            longest = max(longest, length)

        return longest