x = 121
val=0
l = list(str(x))
for i in range(len(l)//2+1):
    if(l[i]==l[len(l)-1-i]):
        val = 1
    else:
        val = 0
        break
if(val==1):    
    print(True)
else:
    print(False)            
