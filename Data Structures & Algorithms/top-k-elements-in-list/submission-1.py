class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictt = {}
        freq = [[] for i in range(len(nums)+1)]
        for number in nums:
            dictt[number] = dictt.get(number, 0) + 1
        for x, y in dictt.items():
            freq[y].append(x)

        res = []
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res