class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        result = []
        n = len(nums)

        for i in range(n-2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            l, r = i + 1, n - 1
            target = -nums[i]

            while l < r:
                s = nums[l] + nums[r]

                if target == s:
                    result.append([nums[i], nums[l], nums[r]])
                    
                    l += 1
                    r -= 1

                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                
                elif s < target:
                    l += 1
                else:
                    r -= 1

        return result