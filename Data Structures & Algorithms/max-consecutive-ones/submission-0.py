class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        curr_c = 0 
        max_c = 0 
        for i in range(len(nums)): 
            if nums[i] == 1: 
                curr_c += 1 
            else: 
                max_c = max(curr_c, max_c)
                curr_c = 0 
        
        return max(max_c, curr_c)
        