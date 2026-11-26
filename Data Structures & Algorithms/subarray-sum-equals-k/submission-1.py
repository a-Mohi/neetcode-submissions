class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        Sum = 0
        hmap = {0:1}
        for n in nums:
            Sum += n
            diff = Sum - k
            res += hmap.get(diff, 0)
            hmap[Sum] = hmap.get(Sum, 0)+1
        return res