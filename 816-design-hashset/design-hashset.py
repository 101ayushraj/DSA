class MyHashSet:

    def __init__(self):
        self.capacity=1000000
        self.counter=[0]*self.capacity

    def add(self, key: int) -> None:
        if self.counter[key]==0:
            self.counter[key]=1

    def remove(self, key: int) -> None:
        if self.counter[key]==1:
            self.counter[key]=0

    def contains(self, key: int) -> bool:
        if self.counter[key]==1:
            return True
        else:
            return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)