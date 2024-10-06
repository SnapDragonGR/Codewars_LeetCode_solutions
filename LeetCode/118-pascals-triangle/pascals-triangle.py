class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        output = []
        for line in range(numRows):
            row = []
            cell = 1
            for i in range(line + 1):
                row.append(cell)
                cell = int(cell * (line - i) / (i + 1))
            output.append(row)
        return output