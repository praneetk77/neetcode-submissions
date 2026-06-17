class Solution:

    def getCharMap(self, s:str) -> Dict:
        map = {}
        for c in s:
            if c in map: map[c] = map[c] + 1
            else: map[c] = 1
        return frozenset(map.items())

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}
        print("hell0")
        for str in strs:
            strMap = self.getCharMap(str)
            found = False
            for key in map.keys():
                if strMap == key:
                    print(f"found true for {str}")
                    map[key].append(str)
                    found = True
            if found: continue
            map[strMap] = []
            map[strMap].append(str)
        
        result = []
        for value in map.values(): result.append(value)
        return result
            
        