class Solution:

    def impl1(self, nums:List[int]) -> List[int]:
        product = 1
        containsZero = False
        for num in nums: 
            if(num==0): containsZero = True
            else: product *= num
            

        result = []
        for num in nums: 
            if(containsZero):
                if(num==0): return []
            ans = product/num
            result.append(int(ans))
        
        return result

    def impl2(self, nums:List[int]) -> List[int]:
        a1 = []
        n = len(nums)
        a2 = [0] * n

        p1 = 1
        for num in nums: 
            p1 *= num
            a1.append(p1)
        
        p2 = 1
        for i in range(n-1, -1, -1):
            p2 *= nums[i]
            a2[i] = p2
        
        result = []

        for i in range(n):
            if(i==0):
                result.append(a2[i+1])
            elif(i==n-1):
                result.append(a1[i-1])
            else:
                result.append(a1[i-1]*a2[i+1])

        return result

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        return self.impl2(nums)
        