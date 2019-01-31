#Question2-Reverse each words in sentence without using library function.
def revstr():
    l=""
    a=""
    strg=str(input("enter the string:"))
    le=len(strg)
    for i in (strg):
        if(i!=" "):
            a=a+i
        else:
            l=a+" "+l
            a=""
    l=a+" "+l
    print(l)
revstr()

        
