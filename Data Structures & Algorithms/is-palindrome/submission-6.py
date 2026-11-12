class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr =[]
        for c in s:
            if c.isalnum():
                newStr += c.lower()
        newStr = ''.join(newStr)
        i = 0
        j = len(newStr)-1
        while i < j:
            if newStr[i] == newStr[j]:
                i+=1
                j-=1
            else:
                return False
        return True
            