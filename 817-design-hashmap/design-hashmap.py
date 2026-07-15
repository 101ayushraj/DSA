class MyHashMap:

    def __init__(self):
        self.capacity=1000
        self.counter=[[] for _ in range(self.capacity)]

    def _hash(self,key):
        return key%self.capacity

    def put(self, key: int, value: int) -> None:
        counter_index=self._hash(key)
        
        for pair in self.counter[counter_index]:
            if pair[0]==key:
                pair[1]=value
                return
        
        self.counter[counter_index].append([key,value])


    def get(self, key: int) -> int:
        counter_index=self._hash(key)

        for pair in self.counter[counter_index]:
            if pair[0]==key:
                return pair[1]
            
        return -1

    def remove(self, key: int) -> None:
        counter_index=self._hash(key)
        for i, pair in enumerate(self.counter[counter_index]):
            if pair[0] == key:
                del self.counter[counter_index][i]
                return

   

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)