class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s: 
            print(f"current stack : {stack}")
            if(c=='(' or c=='{' or c=='['):
                stack.append(c)

            else: 
                if(c==')'):
                    if (not stack) or stack[-1] != '(': return False
                    else: stack.pop()
                elif(c=='}'):
                    if (not stack) or stack[-1] != '{': return False
                    else: stack.pop()
                else:
                    if (not stack) or stack[-1] != '[': 
                        return False
                    else: stack.pop()
        if(not stack): return True
        else: return False

        