class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic = {}
        for i in s:
            dic[i] = dic.get(i, 0) + 1
        for j in t:
                dic[j] = dic.get(j, 0) - 1
        for value in dic.values():
            if value != 0:
                return False
        return True
