class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # matrix = [[1,2,5], [10,11,16], [23,30,39]]
        rows = len(matrix)
        columns = len(matrix[0])
        low = 0
        high = (rows*columns) - 1

        while (low<=high):
            mid = low + (high-low)//2
            rIndex = mid//columns #Row Index
            cIndex = mid%columns #Column Index

            if matrix[rIndex][cIndex] == target:
                return True
            elif matrix[rIndex][cIndex] < target:  #left half eliminated
                low = mid + 1 #move to right
            else: #right half eliminated
                high = mid - 1 #move to left

        return False 
