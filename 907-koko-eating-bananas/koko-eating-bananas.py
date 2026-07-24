class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left,right=1,max(piles)

        def solve(mid):
            hr=0
            for i in piles:
                if i % mid==0:
                    hr+=i//mid
                else:
                    hr+=(i//mid)+1
            return hr<=h

        while right>=left:
            mid=left+(right-left)//2
            if solve(mid):
                ans=mid
                right=mid-1
            else:
                left=mid+1
        return ans