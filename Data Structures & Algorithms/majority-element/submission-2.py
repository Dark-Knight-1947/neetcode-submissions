class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = 1
        me = nums[0]
        for i in range(len(nums)-1):
            if me == nums[i+1]:
                freq += 1 
            if me != nums[i+1]:
                freq -= 1
                if freq == 0:
                    me = nums[i+1]
                    freq = 1
        return me 