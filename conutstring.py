#Question3-Count words in sentence without using library function.
def revstr():
    l=""
    a=""
    count=1
    strg=str(input("enter the string:"))
    le=len(strg)
    for i in (strg):
        if(i!=" "):
            a=a+i
        else:
            l=a+" "+l
            count+=1
            a=""
    l=a+" "+l
        
    print(count)
revstr()
   
        
