class Solution:
    def dailyTemperatures(self, nums: List[int]) -> List[int]:
        st = []
        n = len(nums)
        result = [0] * n

        for i,num in enumerate(nums):
            if st:
                while(st and nums[st[-1]] < num):
                    idx = st.pop()
                    result[idx] = i-idx
            
            st.append(i)
        
        return result


        