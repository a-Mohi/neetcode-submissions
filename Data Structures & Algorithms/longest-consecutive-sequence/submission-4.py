class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        nums.sort()
        Lcount = 0
        count = 1
        for i in range(len(nums)-1):
            if nums[i+1] == nums[i]:
                continue
            elif nums[i+1] == nums[i]+1:
                count +=1
            else:
                Lcount = max(Lcount, count)
                count = 1

        return max(Lcount, count)
