class Solution:
    def findMin(self, nums: List[int]) -> int:
        curr_min = nums[0]
        for i in range(1, len(nums)):
            if nums[i] < curr_min:
                curr_min = nums[i]
        return curr_min