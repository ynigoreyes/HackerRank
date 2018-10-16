class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ans = 0
        width = len(grid)
        height = len(grid[0])

        for i, row in enumerate(grid):
            for j, element in enumerate(row):
                maxValRow = max(row)
                maxValCol = 0
                for arr in grid:
                    if arr[j] > maxValCol:
                        maxValCol = arr[j]

                minVal = min(maxValRow, maxValCol)

                ans += (minVal - grid[i][j])

        return ans
