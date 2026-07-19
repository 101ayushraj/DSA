class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen,repeated=set(),set()
        m=len(s)
        for i in range(0,m-9):
            t=s[i:i+10]
            if t in seen:
                repeated.add(t)
            else:
                seen.add(t)
        return list(repeated)