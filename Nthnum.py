#Question1- Program to find the sum of first N numbers which are either multiple of 3 or 5
n=int(input("Enter the Nth Number:"))
for i in range(1,n+1):
    if(i%3==0) or (i%5==0):
        print(i,end=" ")
print()        
