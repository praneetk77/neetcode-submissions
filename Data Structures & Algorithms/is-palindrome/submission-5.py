class Solution:

    def impl2(self, s: str) -> bool:
        ms = ""
        for c in s: 
            if((c>='a' and c<='z') or (c>='A' and c<='Z') or(c>='0' and c<='9')):
                ms += c.lower()
        
        stack = []
        n = int((len(ms))/2)
        for i in range(n):
            stack.append(ms[i])

        print(f"ms is {ms} && len(ms) is {len(ms)} && n is {n}")

        print(f"stack after half : {stack}")

        add = len(ms)%2

        for i in range(n):
            print(f"i : {i}")
            c = stack.pop()
            print(f"i: {i} and popped : {c} and i+n+add : {ms[i+n+add]}")
            print(f"current stack : {stack}")
            if(ms[i+n+add] != c): return False
        
        return True
            

    def impl1(self, s: str) -> bool:
        ms = ""
        for c in s: 
            if((c>='a' and c<='z') or (c>='A' and c<='Z') or(c>='0' and c<='9')):
                ms += c.lower()
        
        print(f"ms = {ms}")
        print(f"reversed ms = {reversed(ms)}")
        if(ms == ms[::-1]): return True
        else: return False

    def isPalindrome(self, s: str) -> bool:
        return self.impl2(s)
        
        