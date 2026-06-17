class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cnt = {}; curr_len = 0; res = 0; start_ind=-1;
        for i,c in enumerate(s):
            print(f"current len is {curr_len}")
            if(c in cnt and cnt[c]>=start_ind):
                res = max(curr_len, res)
                new_start_ind = cnt[c]+1
                curr_len = i - new_start_ind + 1
                for j in range(start_ind, new_start_ind):
                    cnt.pop(s[j])
                cnt[c] = i
                start_ind = new_start_ind
            else:
                if(start_ind==-1): start_ind = i
                cnt[c] = i
                curr_len += 1
        
        print(f"current len is {curr_len}")
        res = max(res, curr_len)
        return res