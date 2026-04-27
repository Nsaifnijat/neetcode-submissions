class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        

        count = {}

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        freq = [ [] for i in range(len(nums)+1)]

        for key, cnt in count.items():
            print('key',key, cnt)
            freq[cnt].append(key)
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for fr in freq[i]:
                res.append(fr)
                if len(res) == k:
                    return res

