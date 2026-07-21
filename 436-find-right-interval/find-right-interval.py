class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        arr=[]
        for i in range(len(intervals)):
            arr.append([intervals[i][0],intervals[i][1],i])
        arr_sorted=sorted(arr,key=lambda x : x[0])
        ans=[0]*len(intervals)

        for item in arr_sorted:
            index=bisect.bisect_left(arr_sorted,item[1],key=lambda x:x[0])
            if index >= len(intervals):
                ans[item[2]]=-1
            else:
                ans[item[2]]=arr_sorted[index][2]
        return ans