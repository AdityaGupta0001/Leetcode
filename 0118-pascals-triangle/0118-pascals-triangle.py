class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        matrix = [[1]]
        for i in range(1,numRows):
            row = []
            row.append(1)
            for j in range(1,i):
                row.append(0)
            row.append(1)

            matrix.append(row)

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    matrix[i][j] = matrix[i-1][j-1]+matrix[i-1][j]
        
        return matrix