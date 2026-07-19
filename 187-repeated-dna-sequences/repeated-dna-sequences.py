class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        ans=[]
        slider=defaultdict(int)
        m=len(s)
        old_word=s[:10]
        slider[old_word]=1
        for i in range(1,m-9):
            old_word=old_word[1:]+s[i+9]
            slider[old_word]+=1
        for key,value in slider.items():
            if value>1:
                ans.append(key)
        return ans