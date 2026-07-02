class Solution:
    def maxArea(self, heights: List[int]) -> int:
        current, max = 0, 0 
        i = 0 
        j = len(heights) - 1
        while i < j:
            current = (j-i) * min(heights[i], heights[j])
            if current > max:
                max = current
            if heights[i] > heights[j]:
                j -= 1
            else:
                i += 1
            
        return max
