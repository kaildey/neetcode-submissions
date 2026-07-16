class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        if len(nums) == 1:
            return 1
        
        lo, hi = min(nums), max(nums)
        nums2 = [0] * (hi - lo + 1)
        
        for num in nums:
            nums2[num - lo] += 1
        
        maxCon = 1
        counter = 0
        for num in nums2:
            if num == 0:
                maxCon = max(maxCon, counter)
                counter = 0
            else:
                counter += 1
        
        maxCon = max(maxCon, counter)
        return maxCon