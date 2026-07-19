class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n,m=len(haystack),len(needle)
        if m>n:
            return -1
        modu=10**9 
        base=26
        text_hash=window_hash=0
        highest_power=pow(base,m-1,modu)
        for i in range(m):
            text_hash=(text_hash * base + ord(haystack[i]))%modu
            window_hash=(window_hash * base + ord(needle[i]))%modu

        if text_hash==window_hash:
            return 0
        
        for i in range(1,n-m+1):
            outgoing=haystack[i-1]
            incoming=haystack[i+m-1]

            text_hash=((text_hash-ord(outgoing)*highest_power)*base + ord(incoming))%modu
            text_hash=(text_hash+modu)%modu
            if text_hash==window_hash:
                if haystack[i:i+m]==needle:
                    return i
        return -1


