class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dic = {}
        for i in s:
            dic[i] = dic.get(i,0)+1
        for j in t:
            dic[j] = dic.get(j,0)-1
        for i in dic.values():
            if i !=0:
                return False
        return True