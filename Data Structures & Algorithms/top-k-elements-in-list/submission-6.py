class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        count_items = [[] for i in range(len(nums)+1)]
        for num, cnt in count.items():
            count_items[cnt].append(num)

        res = []
        for i in range(len(count_items) - 1, -1, -1):
            for num in count_items[i]:
                res.append(num)
                if len(res) == k:
                    return res
        return []
        