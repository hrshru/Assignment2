#Question2-Reverse each words in sentence without using library function.
list=[]
N=""
String=str(input("Enter the String Value:"))
for i in range(0,len(String)):
    if(String[i]!=" "):
        N=N+String[i]
    else:
        list.append(N)
        N=""
list2=list.append(N)
for j in range(1,len(list)+1):
    print(list[-j],end=" ")
        
