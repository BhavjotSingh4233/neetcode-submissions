class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1 
        right = max(piles)
        best_so_far = max(piles)

        while left <= right: 
            mid = (left + right) // 2

            total = 0
            for i in piles: 
                total += math.ceil(i/mid)


            if total <= h: 
                best_so_far = mid
                right = mid - 1
            else: 
                left = mid + 1
        
        return best_so_far

