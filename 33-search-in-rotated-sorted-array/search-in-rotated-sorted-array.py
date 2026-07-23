class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        i = 0
        j = n - 1
        while i <= j:
            mid = (i + j) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] >= nums[i]:
                if nums[i] <= target <= nums[mid]:
                    j = mid - 1
                else:
                    i = mid + 1
            elif nums[mid] < nums[i]:
                if nums[mid] <= target <= nums[j]:
                    i = mid + 1
                else:
                    j = mid - 1
        return -1