class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        n = len(nums)
        result = []
        resultCount = 0

        for num in nums:
            if num in map : 
                map[num] += 1
            else : 
                map[num] = 1
        
        count = [[] for _ in range(n + 1)]

        for key, val in map.items():
            # print(f"key is {key} and val is {val}")
            count[val].append(key)
            # print(f"after append, count[val] is {count[val]}")

        # print(f"count array : {count}")
        
        for i in range(n, 0 , -1):
            x = count[i]

            for num in x : 
                if(resultCount < k) : result.append(num)
                else : break
                resultCount += 1
            
            if(resultCount == k): break
        
        return result



        