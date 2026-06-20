class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        x = set(nums)
        i = 1
        while i < len(nums) + 1:
            if i in x:
                i += 1
            else:
                return i
        return i