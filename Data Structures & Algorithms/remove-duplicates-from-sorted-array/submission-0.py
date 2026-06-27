class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0 
        j = 1
        count = 0 
        while i < len(nums)-1:
            if nums[i] < nums[j]:
                i = i+1
                j = j+1
            elif nums[i] == nums[j]:
                count += 1
                nums.pop(i)
                j = i+1
        return len(nums)



