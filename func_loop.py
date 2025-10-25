n = int(input("Enter the number: "))
# sum =0
# i=0
# while(i<=n):
#     sum=sum+i
#     i=i+1
# print(sum)
if(n==1 or n==0):
    print("factprial is 1")

fact=1
for i in range(1, n+1):
    fact=fact*i
    
print(fact)