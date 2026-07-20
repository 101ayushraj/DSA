# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left,right=0,n
        mid=last_recorded=-1
        while right>=left:
            mid=left+(right-left)//2
            if isBadVersion(mid)==True:
                last_recorded=mid
                right=mid-1
            else:
                left=mid+1
        return last_recorded