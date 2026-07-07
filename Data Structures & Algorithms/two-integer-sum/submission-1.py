class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictt = {}
        for i in range(len(nums)):
            number = target - nums[i]
            if number in dictt:
                return [dictt[number], i]
            dictt[nums[i]] = i