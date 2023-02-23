
def reverse( x):
        """
        :type x: int
        :rtype: int
        """
        res = ""
        if(str(x)[0]=="-"):
            l = ''.join([str(x)[i] for i in range(1,len(str(x)))])
        else:
            l = str(x)
        for i in range(len(l)-1,-1,-1):
            res += l[i]
        if(str(x)[0]=="-"):
            res = "-"+str(int(res))  
        if(int(res)>2**31 or int(res)<-2**31):
            return 0      
        return int(res) 
print(reverse(1534236469))