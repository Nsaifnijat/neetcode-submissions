from collections import defaultdict
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        num_set = defaultdict()
        
        for i, num in enumerate(numbers):
            if target - num in num_set:
                return [num_set[target-num],i+1]
            else:
                num_set[num] = i+1
        return []