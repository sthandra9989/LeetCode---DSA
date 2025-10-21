class Solution:
    def palindrome(self,new_str:str) -> str:
        m = len(new_str)
        z = (m-1)
        p = 0
        q = m//2
        while(q != 0):
            if(new_str[p] != new_str[z]):
                return False
            p += 1 
            z -= 1
            q -= 1
        return True


    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if(n==1):
            return s
        if(self.palindrome(s)):
            return s
        res = ''
        for i in range(n):
            for j in range(i,n+1):
                if(self.palindrome(s[i:j])):
                    res = max(res,s[i:j],key=len)
        return res


                




        