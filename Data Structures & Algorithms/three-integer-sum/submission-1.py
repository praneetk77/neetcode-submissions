class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums = sorted(nums)
        result = set()
        for ind,num in enumerate(nums): 
            i = 0; j = n-1;
            while(i<j):
                if(i==ind): 
                    i+=1
                    continue
                elif(j==ind):
                    j-=1
                    continue
                curr = nums[i] + nums[j] + num
                if(curr == 0):
                    triplet = sorted([num, nums[i], nums[j]])
                    result.add((triplet[0], triplet[1], triplet[2]))
                    curr_i = nums[i]; curr_j = nums[j];
                    while(i<n and nums[i]==curr_i): i+=1
                    while(j>0 and nums[j]==curr_j): j-=1
                elif(curr < 0):
                    i += 1
                else:
                    j -= 1
        
        list_result = []
        for a,b,c in result:
            list_result.append([a,b,c])
        return list_result


        