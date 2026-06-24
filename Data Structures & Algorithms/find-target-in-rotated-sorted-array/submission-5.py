class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n=len(nums);i=0;j=n-1;

        while(i<=j):
            mid = (i+j)//2

            if(nums[mid]==target):
                return mid


            if(nums[i]<=nums[j]): #case 1 : no discrepancy (normal asc sorted list)
                if(nums[mid]>target): j = mid-1
                else: i = mid+1
            else: #case 2 : discrepancy 
                if(nums[i]<=target): #target belongs in first slope
                    if(nums[i]<=nums[mid]): #mid belongs in first slope
                        if(nums[mid]>target): j = mid-1
                        else: i = mid+1
                    else: #mid belongs in second slope
                        j = mid-1
                else: #target belongs in second slope
                    if(nums[i]<=nums[mid]): #mid belongs in first slope
                        i = mid+1
                    else: #mid belongs in second slope
                        if(nums[mid]>target): j = mid-1
                        else: i = mid+1
            # if(nums[mid]>=nums[i] and nums[mid]>=nums[j]): #mid is in first rising slope
            #     if(nums[i]>=target): #target is in second rising slope
            #         i = mid+1
            #     else: #target is in first rising slope
            #         if(nums[mid]>target): i = mid+1 #target is after mid
            #         else: j = mid-1 #target is before mid
            # else: #mid is in second rising slope
            #     if(nums[i]<=target): 
            #         if(nums[i]>=nums[mid]): j = mid-1
            #         else: i = mid+1
            #     else: #target is in second rising slope
            #         if(nums[mid]>target): i = mid+1 #target is after mid
            #         else: j = mid-1 #target is before mid
            
        return -1



        