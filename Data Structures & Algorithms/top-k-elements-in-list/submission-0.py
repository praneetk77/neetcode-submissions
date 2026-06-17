class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        for i,num in enumerate(nums):
            if(num in map):
                map[num] = map[num]+1
            else: map[num] = 1

        sorted_map = sorted(map.items(), key=lambda x:x[1], reverse=True)
        result = []
        for num,count in sorted_map[:k]:
            result.append(num)

        return result
        
        sorted_map = sorted(map.items(), key=lambda x: x[1], reverse=True)

        result = []
        for num, count in sorted_map[:k]:
            result.append(num)

        return result

        