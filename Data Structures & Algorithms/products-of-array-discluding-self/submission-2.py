class Solution:

    def impl1(self, nums:List[int]) -> List[int]:
        product = 1
        containsZero = False
        containsMoreThanOneZero = False
        for num in nums: 
            if(num==0): 
                if(not containsZero):
                    containsZero = True
                else: 
                    containsMoreThanOneZero = True
            else: product *= num
            

        result = []
        for num in nums: 
            if(num == 0):
                if(not containsMoreThanOneZero): result.append(product)
                else: result.append(0)
            else:
                if(containsZero): result.append(0)
                else: result.append(int(product/num))
        
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
    
    def impl3(self, nums:List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n

        p1 = 1
        for i,num in enumerate(nums): 
            p1 *= num
            if(i+1<n): result[i+1] = p1

        print(f"after first pass {result}")
        
        p1 = 1
        for i in range(n-1, -1, -1):
            p1 *= nums[i]
            if(i-1>=0): result[i-1] *= p1

        print(f"after second pass {result}")
        

        # for i in range(n):
        #     if(i==0):
        #         result.append(a2[i+1])
        #     elif(i==n-1):
        #         result.append(a1[i-1])
        #     else:
        #         result.append(a1[i-1]*a2[i+1])

        return result

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        return self.impl3(nums)
        