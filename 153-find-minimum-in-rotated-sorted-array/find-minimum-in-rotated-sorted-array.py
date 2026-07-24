class Solution:
    def findMin(self, nums: List[int]) -> int:
        left,right=0,len(nums)-1

        if nums[left]<nums[right] or len(nums)==1:
            return nums[0]

        border=left+(right-left)//2
        while nums[border]<nums[border+1]:
            border=left+(right-left)//2

            if nums[border]<nums[left]:
                right=border-1
            else:
                left=border+1
        return nums[border+1]