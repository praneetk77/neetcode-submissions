class TimeMap:

    def __init__(self):
        self.name = []
        self.val = []
        self.time = []
        self.n = 0

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.name.append(key)
        self.val.append(value)
        self.time.append(timestamp)
        self.n += 1

    def get(self, key: str, timestamp: int) -> str:
        
        curr_time = []
        curr_val = []
        for i in range(self.n):
            if(self.name[i]==key):
                curr_time.append(self.time[i])
                curr_val.append(self.val[i])
        


        max_time_ind = -1

        i = 0; j = len(curr_time)-1;

        while(i<=j):
            mid = (i+j)//2
            
            if(curr_time[mid]==timestamp): 
                return curr_val[mid]
            elif(self.time[mid]<timestamp):
                if(max_time_ind == -1 or curr_time[mid]> curr_time[max_time_ind]): max_time_ind = mid
                i = mid+1
            else: 
                j = mid-1
        
        if(max_time_ind==-1): return ""
        return curr_val[max_time_ind]

        

# class MinStack:

#     def __init__(self):
#         self.st = []
#         self.minSt = []
        

#     def push(self, val: int) -> None:
#         self.st.append(val)
#         if(self.minSt and self.minSt[-1] < val): self.minSt.append(self.minSt[-1])
#         else: self.minSt.append(val)

#     def pop(self) -> None:
#         self.st.pop()
#         self.minSt.pop()
        

#     def top(self) -> int:
#         return self.st[-1]
        

#     def getMin(self) -> int:
#         return self.minSt[-1]

        
