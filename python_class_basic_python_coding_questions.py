"""
Q1 WAP to take user input and print number from 1 to n  (using while looP )
"""
# n = int(input("Enter a number : "))
# a = 1
# while (a <= n):
#     print(a, end=" ")
#     a = a + 1

"""
Q2 WAP to take user input and print number in reverse order from n to 1 (using while loop) ?
"""
# n = int(input("Enter a number : "))
# a=1
# while (n>=a):
#     print(n, end=" ")
#     n=n-1

"""
Q3 Wap to take input form user and print sum of all the number from 1 to n (using while loop)
"""
# n = int(input("Enter a number : "))
# a=1
# total_sum=0
# while (n>=a):
#     total_sum= total_sum+n
#     n=n-1
# print(f"Total sum : {total_sum}", end=" ")

""" WAP to take input from user and print sum of all even number separately and odd number 
seperately (using while loop and if-else logic of even odd number ) ?"""
# n = int(input("Enter a number : "))
# a=1
# even=0
# odd =0
# while (n>=a):
#     if(n%2==0):
#         even=even+n
#     else:
#         odd =odd+n
#     n=n-1
#
# print(f"even sum : {even}")
# print(f"odd sum : {odd}")

"""
Q5 WAP to take integer input from user and print it's digit one by one (using while loop)
"""
# n= int(input("Enter a number : "))
# while(n!=0):
#     last_digit = n%10
#     print(last_digit)
#     n = n//10

"""
Q6 WAP to take integer input from user and print Sum of all it's digit 
ex-: 1234 
output-: 10
"""
# n= int(input("Enter a number : "))
# total_sum=0
# while(n!=0):
#     total_sum = total_sum + (n%10)
#     n = n//10
# print(f"Sum of all it's digit is : {total_sum}")

"""
Q7 WAP to take a number as a  input from user and convert that number into reverse order
ex-: 1234 
output-: 4321            
"""

# n = int(input("Enter a number : "))
# rev=0
# original_number= n    # so using this variable i can print the original variable in the end
#                       # because n value will be zero after loop termination
#                       # so that's why i declare a variable
# while(n!=0):
#     rev = (rev*10) + (n%10)
#     n= n//10
# print(f"Original number is {original_number}")
# print(f"reverse number is {rev}")

"""
Q8 WAP to Check a number is an armstrong number or not ? (while loop)
"""
# i = int(input("Enter a number to check it's armstrong or not : "))
# num= i
# sum=0
# while(i!=0):
#     a= i%10
#     sum= sum + (a*a*a)
#     i= i//10
# if(num==sum):
#     print("It is an armstrong number")
# else:
#     print("It is not an armstrong number")

"""
Q9 WAP to print fact of any number .
"""
# num = int(input("Enter a number to find factorial of it :  "))
# i =num
# fact=1
# while(num>=1):
#     fact = fact*num
#     num=num-1
# print(f"factorial of {i} is {fact}")
#
#


"""
Q10  WAP to check if a number is a peterson number or not .

"""
# num = int(input("Enter a number : "))
# n = num
# sum = 0
# while (num != 0):
#     a = num % 10
#     i = 1
#     fact = 1
#     while (i <= a):
#         fact = fact * i
#         i = i + 1
#     sum = sum + fact
#     # print(fact , sum)
#     num = num // 10
#
# # print(n,sum)
# if (n == sum):
#     print("it is a peterson number ")
# else:
#     print("It is not an peterson number")












