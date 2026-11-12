class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        count = 0
        zero_index = -1

        for i in range(n):
            if nums[i] == 0:
                count += 1
                zero_index = i

        if count > 1:
            return [0] * n

        if count == 1:
            prod = 1
            for j in nums:
                if j != 0:
                    prod *= j
            result = [0] * n
            result[zero_index] = prod
            return result

        product = 1
        for a in nums:
            product *= a

        result = []
        for b in nums:
            result.append(product // b)
        return result