class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:  
        count = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                count += 1 
        
        if count >= 2:
            z = 0
        else:
            z = 1

        for i in range(len(nums)):
            if nums[i] == 0:
                continue
            z *= nums[i]

        for i in range(len(nums)):
            if count > 0:
                if nums[i] == 0:
                    nums[i] = z 
                else:
                    nums[i] = 0
            else:
                nums[i] = z // nums[i]
            
        return nums