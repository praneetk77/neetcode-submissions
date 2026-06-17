class Solution:
    def isPalindrome(self, s: str) -> bool:
        stack = []

        ms = ""
        for c in s: 
            if((c>='a' and c<='z') or (c>='A' and c<='Z') or(c>='0' and c<='9')):
                ms += c.lower()
        
        print(f"ms = {ms}")
        print(f"reversed ms = {reversed(ms)}")
        if(ms == ms[::-1]): return True
        else: return False
        