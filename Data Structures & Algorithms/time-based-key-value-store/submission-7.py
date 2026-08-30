class TimeMap:

    def __init__(self):
        self.map = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = {}

        self.map[key][timestamp] = value
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map: return ""
        
        times = self.map[key].keys()
        times = list(times)
        n = len(times)

        result = -1

        i,j = 0,n-1

        while(i<=j):
            mid = (i+j) // 2

            if(times[mid]==timestamp):
                result = times[mid]
                break
            elif(times[mid]<timestamp):
                result = times[mid]
                i = mid+1
            else:
                j = mid-1
        
        found_timestamp = result
        if(found_timestamp==-1): return ""
        else: return self.map[key][found_timestamp]

        
