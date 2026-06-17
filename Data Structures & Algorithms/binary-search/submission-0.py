class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)

        i = 0
        j = n-1

        while (i<=j):
            mid = int((i+j)/2)
            print(f"i is {i}, j is {j}, mid is {mid}")
            print(f"Element at : i is {nums[i]}, j is {nums[j]}, mid is {nums[mid]}")

            if(nums[mid] < target):
                i = mid+1
            elif(nums[mid] > target):
                j = mid-1
            else:
                return mid
        
        return -1