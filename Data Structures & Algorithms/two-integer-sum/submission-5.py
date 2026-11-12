class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted = []
        for i,num in enumerate(nums):
            sorted.append([num, i])
        sorted.sort()

        s = 0
        e = len(nums)-1
        while s<e:
            cur = sorted[s][0]+sorted[e][0]
            if cur == target:
                return[min(sorted[s][1],sorted[e][1]),max(sorted[s][1],sorted[e][1])]
            elif cur < target:
                s+=1
            else:
                e-=1
        return []
                
