class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        if not nums:
            return []
        res = []
        nums.sort()
        n = len(nums)

        for i, a in enumerate(nums):

            if a > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            left = i + 1
            right = n - 1

            while left < right:
                thresum = a + nums[left] + nums[right]

                if thresum > 0:
                    right -= 1
                elif thresum < 0:
                    left +=1
                else:
                    res.append([a, nums[left], nums[right]])
                    left +=1
                    right -=1
                    while nums[left] == nums[left -1] and left < right:
                        left +=1
        return res

        