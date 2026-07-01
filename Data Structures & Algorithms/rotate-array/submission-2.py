class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        x = nums[len(nums)-k:]
        y = nums[0:len(nums)-k]
        nums[:] = x + y
        