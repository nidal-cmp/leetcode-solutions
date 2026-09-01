class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        count = {}

        for row in grid:
            row = tuple(row)
            count[row] = count.get(row,0)+1
        
        answer = 0

        n = len(grid)
        
         
        
        for col in range(n):
            column = []

            for row in range(n):
                column.append(grid[row][col])
            
            column = tuple(column)

            answer += count.get(column,0)

        return answer


         

        