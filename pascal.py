#leetcode solution day 2
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        if numRows == 0:
            return []
        else:
            triangle = [[1]]
            for i in range(1, numRows):
                last_row = triangle[-1]
                row = [1]
                for j in range(1, len(last_row)):
                    row.append(last_row[j - 1] + last_row[j])
                row.append(1)
                triangle.append(row)
        return triangle
