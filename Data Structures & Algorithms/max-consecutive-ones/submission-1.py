class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        curr_c = 0 
        max_c = 0 
        for num in nums: 
            if num == 1: 
                curr_c += 1 
                max_c = max(curr_c, max_c)
            else: 
                curr_c = 0 
        
        return max_c
        