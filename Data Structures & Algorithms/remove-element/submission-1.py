class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        next_valid_nonval = 0 
        for i in range(len(nums)): 
            if nums[i] != val: 
                nums[next_valid_nonval] = nums[i]
                next_valid_nonval += 1 
            
        return next_valid_nonval 
        