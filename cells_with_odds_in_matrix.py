class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        matrix=[]
        count_of_odds=0
        for _ in m:
            matrix.append([0]*n)
        for row, col in indices:
            #incrementing the row 
            for i in range(n):
                matrix[row][i] +=1
            #incrementing the col    
            for i in range(m):
                matrix[col][i] +=1
        for i in range(m):
            for j in range(n):
                if matrix[i][j]%2!=0:
                    count_of_odds +=1
        return count_of_odds