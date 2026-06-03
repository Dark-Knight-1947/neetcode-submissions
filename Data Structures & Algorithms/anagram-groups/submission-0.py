class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictt = {}
        for word in strs:
            x = "".join(sorted(word))
            if x in dictt:
                dictt[x].append(word)
            else:
                dictt[x] = [word]
        return list(dictt.values())