#Q1- Create a function to calculate the area of a circle by taking radius from user.
radius = float(input("enter radius:"))
def area(r):
    print("area of circle with radius %0.2f is"%(r),3.14*r*r)

area(radius)

print("\n\n",10*"*")





#Q2-to find perfect no. between 1 and 1000
print("\n\nperfect no. between 1 and 1000:\n")
for num in range(1,1000):
    sum = 0 
    for i in range(1,num):
        if(num % i == 0):
            sum += i
    if(sum == num):
        print(num)

print("\n\n",10*"*")





#Q.3- Print multiplication table of 12 using recursion.
print("\n\nmultiplication table of 12 using recursion:\n")
def multiply(i):
    if(i<=10):
        print("12 * ",i,"=",12*i)
        multiply(i+1)
    else:
        return
multiply(1)

print("\n\n",10*"*")







#Q.4- Write a function to calculate power of a number raised to other ( a^b ) using recursion.
print("\n\nto calculate power of a number raised to other ( a^b ):\n")
a=int(input("enter number:"))
b=int(input("enter power:"))
def power(a,b):
    if(b == 0):
        return 1
    else:
        return (a * power(a,b - 1))
print("%d ^ %d is "%(a,b),power(a,b))

print("\n\n",10*"*")







#Q.5- Write a function to find factorial of a number but also store the factorials calculated in a dictionary.
print("\n\nTo find factorial:\n")
def fact(n):
    if (n == 1):
        return 1
    else:
      return  n * fact(n-1)

x = int(input("enter the no. of elements :"))
list1=[]
dict={}
for i in range(x):
    num = int(input("enter number:"))
    list1.append(num)
for j in list1:
    temp = fact(j)
    dict[j] = temp
print("\n\nnumber factorial")
for k,v in dict.items():
    print(k,"\t",v)

print("\n\n",10*"*")
