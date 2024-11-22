##sep attribute
##sep is used to separate the values
# n1=10
# n2=20
# print(n1,n2,sep="@")










##end attribute
##end is used to give value at end
# n1=10
# n2=20
# print(n1,n2,end="@")










##\n :-  takes cursor on the naext line
# n1=10
# n2=20
# n3=30
# print(n1,"\n")
# print(n2,"\n")
# print(n3,"\n")











##format()  :-method used for string
# name="raj"
# age=23
# city="pune"
# print("my name is {} i am {} years old and i am from {} city".format(name,age,city))


##
# name="raj"
# age=23
# city="pune"
# print("my name is {0} i am {1} years old and i am from {2} city".format(name,age,city))


















##WAP to print fibonaci series
# n1=0
# n2=1
# print(n1, end=" ")
# print(n2, end=" ")
# for i in range(10):
#     n3=n1 + n2
#     print(n3, end=" ")
#     n1=n2
#     n2=n3



##fibonaci series
# first=0
# second=1
# for i in range(10):
#     print(first ,end=" ")
#     first,second=second,first+second



##fibonaci series using while
# first=0
# second=1
# n=int(input("n: "))
# i=1
# while i<=n:
#     print(first ,end=" ")
#     first,second=second,first+second
#     i=i+1
    























##WAP to check if the number is palindrome or not
# str=input("Enter name: ")
# str1=str[::-1]
# if (str==str1):
#     print("string is palindrme")
# else:
#     print("not palindrome")




















##WAP to print max number from the list nut withour using any method or function.
# n1=0
# l=[11,22,33,44,55,66,11]
# for i in l:
#     if (i>n1):
#         n1=i

# print(n1)


##
# l=[11,22,33,44,55,66,11]
# max=l[0]
# for i in l[1:]:
#     if max<i:
#         max=i

# print(max)










##WAP to iterate only alphabets from given string

name="bhu1sh5a6n"
for i in name:
    if(i.isalpha()):
        print(i,end="")

        


    


