class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)

        while left <= right:
            mid = (left + right)//2

            current_load = 0
            days_needed = 1

            for weight in weights:
                if current_load + weight > mid:
                    days_needed += 1
                    current_load = 0
                current_load += weight

            if days_needed <= days:
                right = mid - 1
            else:
                left = mid + 1
            
        return left