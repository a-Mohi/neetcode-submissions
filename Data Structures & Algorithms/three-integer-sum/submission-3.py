class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        if nums == [0,0,0]:
            return [nums]
        nums.sort()
        result = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i+1
            k = len(nums)-1
            while j < k:
                target = -nums[i]
                if nums[j] + nums[k] == target:
                    result.append([nums[j],nums[k],nums[i]])
                    j +=1
                    k -= 1
                    while nums[j] == nums[j-1] and j < k:
                        j += 1
                elif nums[j] + nums[k] < target:
                    j += 1
                else:
                    k -= 1
        return result

            
