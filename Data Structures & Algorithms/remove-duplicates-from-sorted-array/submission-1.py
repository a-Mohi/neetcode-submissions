class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        res = set()
        for i in nums:
            if i not in res:
                res.add(i)
        num = list(res)
        num.sort()
        nums[:] = num
        return len(res)