class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        left, right = 1, max(piles)
        cur_speed = right

        while left <= right:
            k = (left + right)//2

            totalTime = 0
            for pile in piles:
                totalTime += math.ceil(pile/k)
            
            if totalTime <=h:
                cur_speed = k
                right = k - 1
            else:
                left = k + 1
        return cur_speed