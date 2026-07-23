class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows,columns=len(matrix),len(matrix[0])
        left,right=0,rows*columns - 1
        while right>=left:
            mid=left+(right-left)//2
            row_no = mid // columns
            column_no = mid % columns
            num=matrix[row_no][column_no]
            if num==target:
                return True
            elif num>target:
                right=mid-1
            else:
                left=mid+1
        return False