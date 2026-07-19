class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        ans=[]
        tracker = defaultdict(lambda: defaultdict(int))
        m=len(s)
        if m<=10:
            return ans
        base=4
        highest_power=pow(4,9)
        text_hash=0
        for i in range(10):
            text_hash=(text_hash*base)+ord(s[i])
        pattern_hash=text_hash
        tracker[pattern_hash][s[0:10]] = 1
        for i in range(1,m-9):
            pattern_hash=(pattern_hash-ord(s[i-1])*highest_power)*base + ord(s[i+9])
            tracker[pattern_hash][s[i:i+10]] += 1
        for pattern_hash, string_counts in tracker.items():
            for unique_string, count in string_counts.items():
                if count > 1:
                    ans.append(unique_string)
        return ans