from collections import defaultdict
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        num_dict = defaultdict()
        
        for i, num in enumerate(numbers):
            if target - num in num_dict:
                return [num_dict[target-num],i+1]
            else:
                num_dict[num] = i+1
        return []