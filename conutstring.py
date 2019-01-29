#Question3-Count words in sentence without using library function.
list=[]
n=""
Count=0
String=str(input("Enter the String:"))
for i in range(0,len(String)):
    if(String[i]!=" "):
        n+=String[i]
    else:
        list.append(n)
        n=""
list.append(n)
for j in range(0,len(list)):
    Count+=1
print(Count)    
        
