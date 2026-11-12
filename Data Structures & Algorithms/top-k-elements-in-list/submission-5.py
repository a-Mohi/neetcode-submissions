class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        for i in nums:
            map[i] = map.get(i,0)+1
        sortedM = sorted(map.items(), key = lambda x:x[1], reverse = True)
        res =[]
        i = 0
        while i < k:
            res.append(sortedM[i][0])
            i +=1
        return res
        