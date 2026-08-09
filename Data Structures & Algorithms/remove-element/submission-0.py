class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        next_non_val = 0 
        for i in range(len(nums)):
            if nums[i] != val: 
                nums[next_non_val] = nums[i]
                next_non_val += 1
        
        return next_non_val
        