class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)

        i = 0; j = n-1;

        while (i<j):
            while not s[i].isalnum() and i < j:
                print(f"at i char is {s[i]}")
                i += 1
            while not s[j].isalnum() and i < j:
                print(f"at j char is {s[j]}")
                j -= 1
            ci = s[i].lower()
            cj = s[j].lower()

            if ci != cj : 
                print(f"unequal i and j {s[i]} and {s[j]}")
                return False
            
            i += 1
            j -= 1
        
        return True
        