class Solution:
    def search(self, nums: list[int], target: int) -> int:
        N = len(nums)
        low = 0
        high = N - 1

        while (low <= high):
            mid = low + (high-low)//2

            if nums[mid] == target:
                return mid
                
            if nums[low] <= nums[mid]: #left half sorted
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1

            else: #right half sorted
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return - 1 
    
nums = [4,5,6,7,0,1,2]
target = 0

x = Solution()
print(x.search(nums, 0))
