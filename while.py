# While loop

#   ICU

# Initialization
# while CONDITION:
#     body
#     UPDATE



##First basic code
# i=1
# while i<11:
#     print(i)
#     i=i+1 
# print('hello')




##WAP a program to print numbers from 21 to 30 by using while loop
# i=21
# while i<=30:
#     print(i)
#     i+=1
# print('end')     




##WAP to print numbers from 11 to 1

# i=11
# while i>=1:
#     print(i)
#     i=i-1
# print('end')



##WAP to print dict of squares of numbers from 1 to 10 by using while loop

# d1={}
# i=1
# while i<=10:
#     d1[i]=i**2
#     i=i+1
# print(d1)    



##WAP to print sqaure of eleven numbers from 1 to 20
 
# d1={}
# i=1
# while i<=20:
#     if i%2==0:
#        d1[i]=i**2
#     i=i+1
# print(d1)    









##WAP to print names from the list

# l=['rahul','sahil','raj']
# i=0
# while i<len(l):
#     print(l[i])
#     i=i+1
# print('end')








##WAP to print factorial of any number

# num=eval(input('Enter any number: '))
# fact=1
# while num > 1:
#     fact = num * fact
#     num -= 1  # Decrease num by 1 in each iteration
# print(fact)



    









##WAP to check if number is prime or not

# n=eval(input('Eneter the number: '))

# i=0
# while n<=1:
#     if n%1==0:
#        if n%n==0:
#            print('It is prime number')
   
              






























##WAP a program to print addition of numbers from list

# l=[1,2,3,4,5,6,7,8,9,10,11]
# ad=0
# i=0
# while i<len(l):
#     ad=ad+l[i]
#     i=i+1
# print(ad)








##WAP to check if the given number is perfect or not

# num=eval(input('Enter the number: '))
# sum=0

# i=1
# while i<num:
#     if num%i==0:
#        sum=sum+i
#     i=i+1
        
# if sum==num:
#     print('It is a perfect number')
# else:
#     print('Not a perfect number')    














##fibonaci series using while
# first=0
# second=1
# n=int(input("n: "))
# i=1
# while i<=n:
#     print(first ,end=" ")
#     first,second=second,first+second
#     i=i+1









