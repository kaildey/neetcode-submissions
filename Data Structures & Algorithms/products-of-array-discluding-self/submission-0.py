class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        prefix, postfix = 1, 1

        for num in nums:
            result.append(prefix)
            prefix *= num
        
        for i in range(len(nums)-1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]
        
        return result
