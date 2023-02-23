def lengthOfLongestSubstring(s):
        """
        :type s: str
        :rtype: int
        """
        d = dict()
        for i in range(len(s)):
            if(s[i] in list(d)):
                d[s[i]] += 1
            else:
                d[s[i]] = 1
        n = ''.join([i for i in list(d)])
        if(n in s):
             return len(n)
        else:
            temp = n
            l = [0]*100
            
            for i in range(1,len(temp)):
                new = ''.join([temp[j] for j in range(i,len(temp)) ])        
                if(new in s):
                    l[i] = len(new)
            return max(l)      
s = "abcabcbb"
print(lengthOfLongestSubstring(s))