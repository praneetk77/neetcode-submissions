class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)

        for i,t in enumerate(temperatures): 
            if(stack):
                while(stack and temperatures[stack[-1]]<t):
                    result[stack[-1]] = i-stack[-1]
                    stack.pop()
                stack.append(i)
            else: 
                stack.append(i)

        return result
        