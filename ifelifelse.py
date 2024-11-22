##ifelifelse control statement

# if:
#      body
# elif:
#      body
# else:














# s1=int(input('Enter the age:' ))
# s2=int(input('Enter the age:' ))
# s3=int(input('Enter the age:' ))

# if s1>s2 and s2>s3:
#     print(s1)
# elif s2>s3 and s2>s1:
#     print(s2)
# else:
#     print(s3)

















##Write a program to print Grades according to percentage


# p1=int(input('Enter the percentage: '))

# if p1>=90:
#     print('A+')
# elif p1>=80 and p1<90:
#     print('A')
# elif p1>=70 and p1<80:
#     print('B+')
# elif p1>=60 and p1<70:
#     print('B')
# else:
#     print('C') 















##Write a program to indentify which number is greater or smaller or equal between two inputs

# s1=int(input('Enter a number: '))
# s2=int(input('Enter another number: '))

# if s1>s2:
#     print(s1, 'is greater')
# elif s2>s1:
#     print(s2, 'is greater')
# else:
#     print('Both are equal')














##Write a program and find whether the number is positive , negative or zero


# s1=eval(input('Enter the number: '))

# if s1>0:
#     print('Number is positive')
# elif s1<0:
#     print('Number is negative')
# else:
#     print('Number is zero ')

































##Write a program to create a calculator for the user

# n1=int(input('Enter first number: '))
# opr=input('Enter the operator: ')
# n2=int(input('Enter second number: '))

# if opr=='+':
#     print(n1+n2)
# elif opr=='-':
#     print(n1-n2)
# elif opr=='*':
#     print(n1*n2)
# elif opr=='/':
#     if n2!=0:
#         print(n1/n2)
#     else:
#         print('Divisibilitiy not possible by zero ')
# else: 
#     print('Error: Enter valid opeartor')






















##Write a program to sort out names with first capital letter from the list
## isupper is a method which checks if the string is in uppercase

# l=['rajesh','Dipak','soham','Rohan']

# for name in l:
#     if name[0].isupper():
#         print(name)















##Write a program having letter v at last
##Method endswith check last character of a string

# l=['rajiv','Dipak','soham','Raghav']

# for name in l:
#     if name[-1]=='v' or name[-1]=='V':
#         print(name)

# OR

# l=['raju','Dipak','soham','Raghav']

# for name in l:
#     if name.endswith('v'):
#         print(name)

     





























##Write a program which has more than five characters
## Method len() checks length of a string

# l=['rajiv','Dipak','soham','Raghav']

# for name in l:
#     if len(name)>5:
#         print(name)









##Write a program to sort the names written in lowercase and print in a list
##Method append adds the given data in list/dictionary/set, etc.

# l=['rajiv','Dipak','soham','Raghav']
# n=[]

# for name in l:
#     if name.islower():
#         n.append(name)

# print(n)








##WAP to sort people as poor,middleclass,rich from the dictionary

#d1={'rahul':'200000','shubham':'500000','rohan':'150000','soham':'300000'}

