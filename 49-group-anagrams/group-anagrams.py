from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counter=defaultdict(list)
        for word in strs:
            freq=[0]*26
            for l in word:
                freq[ord(l)-ord('a')]+=1
            frozen=tuple(freq)
            counter[frozen].append(word)
        
        return [i for i in counter.values()]