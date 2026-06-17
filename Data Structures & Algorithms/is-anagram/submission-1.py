class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map = {}
        for i, c in enumerate(s):
            if(c in map):
                map[c] = map[c]+1
            else:
                map[c] = 1
        
        for i, c in enumerate(t):
            if(c not in map or map[c]==0):
                return False
            else: 
                map[c] = map[c] - 1
        
        for key in map.keys():
            if (map[key] != 0): return False

        return True
        