class Solution:

    def impl1(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(speed)
        cars = [list(car) for car in sorted(zip(position, speed))]
        st = []

        for i in range(n-1, -1, -1):
            if not st : 
                st.append(i)
            else:
                st_ind = st[-1]
                pos_ind = cars[st_ind][0]; spd_ind = cars[st_ind][1];
                pos_curr = cars[i][0]; spd_curr = cars[i][1];

                time_ind = (target-pos_ind)/spd_ind; time_curr = (target-pos_curr)/spd_curr;

                if(time_curr > time_ind): 
                    st.append(i)
        
        return len(st)

        

    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # n = len(speed)
        # cars = sorted(zip(position, speed))
        # a = [0] * n
        # free = [True] * n
        # count = 0
        # cars = [list(car) for car in sorted(zip(position, speed))]

        # while(True):

        #     for i in range(n-1, -1, -1):
        #         pos = cars[i][0]; sp = cars[i][1];
        #         if(i == n-1):
        #             cars[i][0] = min(pos + sp, target)
        #         else: 
        #             curr_cap = min(pos + sp, target)
        #             if(curr_cap<cars[i+1][0]):
        #                 cars[i][0] = curr_cap
        #             else:
        #                 cars[i][0] = cars[i+1][0]
        #                 cars[i][1] = cars[i+1][1]
        #                 free[i] = False

        #     allReached = True
        #     for i in range(n):
        #         if(cars[i][0]<target):
        #             allReached = False
        #             break
        #     if(allReached): break


        # print(f"final free array : {free}")
        # for val in free:
        #     if(val): count+=1
        # return count

        return self.impl1(target, position, speed)

        

# 0 1 4 7
# 1 2 2 1

# 1  3  6  8
# 2  5  8  9
# 3  7  10 10
# 4  9  10 10
# 4  10 10 10 
# .  .  .  .
# 10 10 10 10 


# 1  4
# 3  2

# 4  6
# 7  8
# 10 10
