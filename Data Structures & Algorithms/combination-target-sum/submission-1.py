class Solution:
    def __init__(self):
        self.ans = []
    
    def helper(self, nums, target, l, start, current_sum):
        if target == current_sum:
            self.ans.append(l.copy())
            return
        
        if target < current_sum:
            return
        
        for i in range(start, len(nums)):
            l.append(nums[i])

            self.helper(nums, target, l, i, current_sum + nums[i])
            l.pop()

    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        l = []

        self.helper(nums, target, l, 0, 0)
        return self.ans