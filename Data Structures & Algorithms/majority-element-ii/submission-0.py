class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        dictt = {}
        imp = []

        for ch in nums:
            if ch in dictt:
                dictt[ch] += 1 
            else:
                dictt[ch] = 1

        for i,j in dictt.items():
            if j > len(nums) // 3:
                imp.append(i)
        
        return imp