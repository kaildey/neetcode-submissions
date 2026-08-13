class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac, atl = set(), set()
        result = []

        def helper(i, j, visit, prev):
            if i < 0 or i >= len(heights) or j < 0 or j >= len(heights[0]) or (i,j) in visit or heights[i][j] < prev:
                return

            visit.add((i,j))
            helper(i, j+1, visit, heights[i][j])
            helper(i+1, j, visit, heights[i][j])
            helper(i, j-1, visit, heights[i][j])
            helper(i-1, j, visit, heights[i][j])
            
        
        for i in range(len(heights)):
            helper(i, 0, pac, heights[i][0])
            helper(i, len(heights[0])-1, atl, heights[i][-1])

        for j in range(len(heights[0])):
            helper(0, j, pac, heights[0][j])
            helper(len(heights)-1, j, atl, heights[-1][j])
    
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if (i,j) in pac and (i,j) in atl:
                    result.append([i,j])
        
        return result