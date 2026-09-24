class Solution:
    def isPalindrome(self, s: str) -> bool:
        ns = ''.join(ch.lower() for ch in s if ch.isalnum())
        start, end = 0, len(ns)-1
        while start<end:
            if ns[start] != ns[end]:
                return False
            start += 1
            end -= 1
        return True