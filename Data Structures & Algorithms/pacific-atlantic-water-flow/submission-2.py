class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        hashSet = set()
        result = []
        
        def helper(i,j, prev, visited):
            nonlocal pac
            nonlocal atl
            
            if i < 0 or i >= len(heights):
                return
            if j < 0 or j >= len(heights[0]):
                return

            if heights[i][j] > prev:
                return

            if i == 0 or j == 0:
                pac = True
            if i == len(heights)-1 or j == len(heights[0])-1:
                atl = True
            if pac and atl:
                pac = atl = True
                return
            if (i,j) in visited:
                return
            
            prev = heights[i][j]
            visited.add((i,j))
            helper(i, j+1, prev, visited)
            helper(i+1, j, prev, visited)
            helper(i, j-1, prev, visited)
            helper(i-1, j, prev, visited)

        for i in range(len(heights)):
            for j in range(len(heights[i])):
                pac, atl = False, False
                visited = set()

                helper(i, j, heights[i][j], visited)

                if pac and atl:
                    result.append([i,j])
            
        return result