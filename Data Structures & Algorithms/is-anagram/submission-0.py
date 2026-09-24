class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict = {}
        for i in s:
            dict[i] = dict.get(i, 0) + 1
        for j in t:
                dict[j] = dict.get(j, 0) - 1
        for value in dict.values():
            if value != 0:
                return False
        return True
