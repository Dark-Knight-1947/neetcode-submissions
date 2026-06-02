class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        new = {}
        for i in range(len(nums)):
            number = target - nums[i]
            if number in new:
                return [new[number],i]
            new[nums[i]] = i