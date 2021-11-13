
#Def a function checking the sequance
def fibo(n):
    if n<=1:
        return n
    else:
        return fibo(n-1)+fibo(n-2)

#loop with a counter implementing the function
#for i in range(15):
#    print(fibo(i))

#taking input from users
ncount=int(input("How many numbers you need?"))

for i in range(ncount):
    print(fibo(i))