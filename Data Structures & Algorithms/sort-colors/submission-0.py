class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        dictt = {}
        for number in nums:
            dictt[number] = dictt.get(number, 0) + 1

        i = 0
        for x in range(dictt.get(0,0)):
            nums[i] = 0 
            i += 1 

        for x in range(dictt.get(1,0)):
            nums[i] = 1 
            i += 1 

        for x in range(dictt.get(2,0)):
            nums[i] = 2 
            i += 1 