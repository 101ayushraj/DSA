from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        counter=set(nums)
        maxi=0
        for i in counter:
            a=i
            cnt=0
            if i-1 not in counter:
                while a in counter:
                    cnt+=1
                    a+=1
                maxi=max(maxi,cnt)
        return maxi
            


        