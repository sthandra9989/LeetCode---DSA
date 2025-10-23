class Solution:
    def reverseWords(self, s: str) -> str:
        new_str = []
        n = len(s)
        k = 0

        for i in range(n):
            if(s[i] == ' '):
                new_str.append(s[k:i])
                k = i 
        new_str.append(s[k:n])
        
        new_str_c = []
        for i in range(len(new_str)):
            new_str[i] = new_str[i].lstrip()
            new_str[i] = new_str[i].rstrip()
            if(new_str[i] != ''):
                new_str_c.append(new_str[i])
        
        new_str_c = new_str_c[::-1]

        print(new_str_c)

        return ' '.join(new_str_c)










        