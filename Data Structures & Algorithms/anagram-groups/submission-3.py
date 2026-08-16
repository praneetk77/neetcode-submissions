class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        result = []
        map = {}
        for s in strs: 
            
            count = [0] * 26

            for c in s: 
                count[ord(c)-ord("a")] += 1
            
            tcount = tuple(count)
            if tcount in map.keys():
                map[tcount].append(s)
            else: 
                map[tcount] = [s]
        
        for val in map.values():
            result.append(val)
        
        return result
        