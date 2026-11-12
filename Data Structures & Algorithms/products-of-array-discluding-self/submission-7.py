class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        count = 0
        n = len(nums)
        zero =-1
        for i in range(n):
            if nums[i] == 0:
                count += 1
                zero = i

        if count > 1:
            return [0]* n
     
        if count == 1:
            prod = 1
            for j in nums:
                if j != 0:
                    prod *= j
            new_list = [0]*n
            new_list[zero] = prod
            return new_list
       
        product = 1
        for a in nums:
            product *= a
        
        result = []
        for b in nums:
            result.append(product // b)
        return result