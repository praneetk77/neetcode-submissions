class Solution:
    def search(self, nums: List[int], target: int) -> int:

        n = len(nums)
        i,j = 0,n-1

        while(i<=j):
            mid = (i+j) // 2
            print(f"i = {i} and j = {j} and mid = {mid}")
            if(nums[mid]==target): return mid

            # edge case - normal sorted
            if(nums[i] <= nums[mid] and nums[mid] <= nums[j]):
                if nums[mid] > target: j = mid-1
                else: i = mid+1
                continue

            # mid is in the second slope
            if(nums[mid] <= nums[j]):

                # mid is lower than target
                if(nums[mid] < target):

                    # target is in the first slope - check left
                    if(target >= nums[i]):
                        j = mid-1

                    # target is in the second slope - check right    
                    else:
                        i = mid+1

                # mid is greater than target - check left
                else:
                    j = mid-1

            # mid is in the first slope
            else:

                # mid is greater than target
                if(nums[mid] > target):

                    # target is in first slope - check left
                    if(target > nums[j]):
                        j = mid-1
                    
                    # target is in second slope - check right
                    else: 
                        i = mid+1
                
                # mid is lesser than target - check right
                else: 
                    i = mid+1
            
        return -1
        