#writting a function
def hello():
    print("Hello")
    print("AMR")

print("My code")
#calling function
hello()

#function with arguments
def add(x,y):
    n = x+y
    return n

#A function passing two operations sub and add
def add_sub(x,y):
    n = x+y
    x= x-y
    return n, x
z, b = add_sub(20,12)
print("addition: ",z)
print("Subt: ",b)

print (add(3,5)+2)
