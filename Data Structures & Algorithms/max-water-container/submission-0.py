class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxContainer = 0
        l = 0
        r = len(heights) - 1

        while l < r:
            height = min(heights[l], heights[r])
            container = height * (r - l)
            maxContainer = max(maxContainer, container)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return maxContainer