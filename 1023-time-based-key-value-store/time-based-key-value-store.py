from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.cointainer=defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.cointainer[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        values=self.cointainer[key]
        left=0
        right=len(values) -1
        ans=""
        while right>=left:
            mid=left+(right-left)//2
            if values[mid][1]<=timestamp:
                ans=values[mid][0]
                left=mid+1
            else:
                right=mid-1

        return ans



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)