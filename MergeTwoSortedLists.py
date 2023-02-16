l = [1,2,4]
m = [1,3,4]
r = len()
new = [0]*(len(l)+len(m))
if(len(m)==0):
    new = l
elif(len(l)==0):
    new = m 
else:
    for i in range(min(len(l),len(m))):
        if(l[i]<=m[i]): 
            new[2*i] = l[i]
            new[2*i+1]  = m[i]
        else:
            new[2*i] = m[i]
            new[2*i+1] = l[i]    
    if(len(l)>len(m)):
        for i in range(len(l)-len(m)):
            new[2*len(m)+i] = l[len(m)+i]
    if(len(l)<len(m)):
        for i in range(len(m)-len(l)):
            new[2*len(l)+i] = l[len(l)+i]
        
print(new)


