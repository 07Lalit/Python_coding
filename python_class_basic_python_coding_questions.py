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

"""
Q11 WAP to check if a number is a palindrome or not ?

"""
# n= int(input("Enter a number : "))
# num=n
# rev=0
# while(n!=0):
#     rev = (rev*10) + (n%10)
#     n= n//10
# if (num==rev):
#     print(f"It is a palindrome number as reverse number {rev} == given number {num} ")
# else:
#     print("It is not a palindrome number ")


"""
Q12 WAP check if a number is a prime number or not ?
"""
# a= int(input("Enter a number to check it's a prime or not : "))
# i = 2
# if (a>1):
#     while(i<a):
#
#         if (a%i==0):
#             print("It is not an prime number ")
#             break
#         i=i+1
#     else:
#         print("It is a prime number ")
# else:
#     print("It is not a prime number")


"""
Q 13  WAP to print to convert number to their corresponding unicode values ?  (using while loop)
 Unicode values   :  A-Z -> 65-90
                     a-z -> 97-122
                     0-9 -> 47-52
                     
using chr() function .

"""
# import time
#
# a = True
# while (a):
#     print("\n")
#     ask = int(input(f"""
#
#                                     Welcome to program to convert number to their corresponding unicode values
#                                  ------------------------------------------------------------------------------------
#
#                   what you want to print on screen press number from (1-5) :
#
#                   1) capital_alphabet (A-Z)
#
#                   2) small_alphabet   (a-z)
#
#                   3) number(0-9)
#
#                   4) other unicode values
#
#                   5) Quit a program.
#
#
#
#                   Enter Your input -> """))
#
#     if (ask == 1):
#         num = 65
#         while (num <= 90):
#             print(f"{num} : {chr(num)}")
#             num = num + 1
#         print(f"\n Thank You !!!{chr(128512)}")
#
#     elif (ask == 2):
#         num = 97
#         while (num <= 122):
#             print(f"{num} : {chr(num)}")
#             num = num + 1
#         print(f"\n Thank you!!!{chr(128513)}")
#
#     elif (ask == 3):
#         num = 48
#         while (num <= 57):
#             print(f"{num} : {chr(num)}")
#             num = num + 1
#         print(f"\n Thank You!!{chr(128512)}")
#
#     elif (ask == 4):
#         i = int(input("\nEnter a number for that you want to see their corresponding unicode value : "))
#         print(f"unicode value of number {i} is : {chr(i)}")
#         print(f"\n Thank you !!!{chr(128512)}")
#
#     elif (ask == 5):
#         print(f"\n Thank You {chr(128516)}")
#         break
#
#     else:
#         print(f"""\n You entered a wrong number {chr(128514)}
#                      please try again!!!""")
#


"""
 Q14 WAP to find the simple Interest by taking amount ,rate, & time in years from the user ?
 
 -> 
Simple Interest (S.I) is the method of calculating the interest amount for some principal amount of money.
 Have you ever borrowed money from your siblings when your pocket money is exhausted? Or lent him maybe?
  What happens when you borrow money? You use that money for the purpose you had borrowed it in the first place.
   After that, you return the money whenever you get the next month’s pocket money from your parents. 
   This is how borrowing and lending work at home
   
But in the real world, money is not free to borrow. You often have to borrow money from banks in the form of a loan. 
During payback, apart from the loan amount, you pay some more money that depends on the loan amount as well as the time 
for which you borrow. This is called simple interest. This term finds extensive usage in banking.

Where SI = simple interest

P = principal

R = interest rate (in percentage)

T = time duration (in years)
 
 The list of formulas of simple interest for when the time period is given in years, months and days are tabulated below:

Time	Simple interest Formula	Explanation
Years	PTR/100	T = Number of years
Months	(P × n × R)/ (12 ×100)	n = Number of months
Days	(P × d × R)/ (365 ×100)	d = Number of days (non-leap year)
 
"""
# Principle_amount= int(input("Enter the amount that you want to take a loan : "))
# rate = int(input("Enter the rate of interest : "))
# time = int(input("Enter the time in years for how many years you want a loan : "))
# Simple_Interest = (Principle_amount*rate*time)/100
# print(f"""
#                            Simple Interest Calculator
#                            ---------------------------
#
#             so the amount of loan is : {Principle_amount}
#             rate of : {rate}%
#             for {time} years
#
#             So the amount you have to pay after {time} year is  : {Simple_Interest+Principle_amount}
#             so you have to pay {Simple_Interest} this much amount extra as a Interest
# """)

"""
Q14 wap to find compount Interest ?

Compound interest is the interest calculated on the principal and the interest accumulated over the previous period. 
It is different from simple interest, where interest is not added to the principal while calculating the interest 
during the next period. In Mathematics, compound interest is usually denoted by C.I.

"""
# #Taking input from user.
# principal = int(input("Enter the principal amount: "))
# rate = int(input("Enter rate of interest: "))
# time = int(input("Enter time in years: " ))
# #
# # # Calculates compound interest
# Amount = principal * (pow((1 + rate / 100), time))
# CI = Amount - principal
# print("Compound interest is",  int(CI) )
# print(f"Total amount you have to pay after {time} year is {int(CI+principal)}")


"""
Q15 WAP to find the sum of square of first n natural number .
"""
# n=int(input("Enter a number till you want sum of square of Natural number : "))
# sum=0
# a=1
# while(a<=n):
#     sum= sum+ (a*a)
#     a=a+1
# print(f"Sum of Square of n natural number is : {sum} ")

"""
Q16 WAP to find the sum of cube of first n nutaurl number ?
"""
# n=int(input("Enter a number till you want sum of Cube of Natural number : "))
# sum=0
# a=1
# while(a<=n):
#     sum= sum+ (a*a*a)
#     a=a+1
# print(f"Sum of Cube of n natural number is : {sum} ")

"""
Q17 WAP to calculate area of triangle ?
"""
# base = int(input("Enter a base of triangle : "))
# height = int(input("Enter a height of triangle : "))
# area = (1/2)* (base* height)
# print(f"Area of Triangle is : {area}")



"""
Q18 WAP to find the square root of any number in python ?

In Python, the ** operator is used:
1. Exponentiation:
When used between two numeric values, the ** operator performs exponentiation, raising the left operand to the power of the right operand.
x = 2
y = 3
result = x ** y  # result will be 8 (2^3)
# or we can also use math.sqrt() function 
"""

# num = float(input("Enter a number to find it's square root : "))
# num_sqrt = num ** 0.5
# print(f"The square root of {num} is {num_sqrt}")


"""
Q19  WAP to swap two number ? 
 Input-:   a= 10  ;   b= 20  
 outpur-:  a=20   ;   b=10 
 
 So there are many ways to do it 
 1) using extra variable  -: 
     i) create a temporary varaible  temp  
     ii) intilize the value of  first variable that is a  into temp  
     iii)  then in the next line Initilize the  value of b  into a  
     iv)  at last inlize the value of temp variable in b  
     
     temp = a     # a= 10 , b=20  , temp=10                   # so  before swaping our a value is 10 & b value is 20
     a = b        # a= 20 , b= 20 , temp=10 
     b = temp     # a=20  , b=10  , temp= 10                  # so after swapping our a value is 20 & b value is 10 
     
2) using arithemetic opeators 
  i) + & - 
  ii) * & // 

logic of + & - : # a=10 , b=20
a= a + b       # a=10+20   # a=30
b = a- b       # b= 30-20  # b=10 
a = a- b       # a= 30-10  # a = 20    

so after swapping a value is 20 and  b value is 10    

logic of * & // : # a = 10 , b= 20 
a= a*b     # a= 10 * 20   # a=200
b = a//b   # b = 200//20  # b= 10 
a = a//b   # a = 200//10  # a = 20 
so after swapping a value is 20 and  b value is 10

3) using xor (^) operator it bits are same (0 & 1) answer is 0 else different than 1
a= a^b    # a = 01010^10100 = 30
b= a^b    # b = 11110^10100 = 10 
a= a^b    # c = 11110^01010 = 20
so after swapping a value is 20 and  b value is 10
"""
# writing a code

# a = int(input("Enter a value of a : "))
# b = int(input("Enter a value of b : "))
# temp = None    # so decalare a variable temp with none vale initially
# # printing before swapping :
# print(f"value before swapping of a : {a}   ,  value of b is : {b}")
# temp = a
# a = b
# b = temp
# print(f"Value after swapping of a: {a}  , value of b is : {b} ")




"""
Q20  WAP Python program to solve quadratic equation ? 

A quadratic equation is a polynomial equation of degree 2, which means it contains a term with a variable raised to the power of 2. It takes the form:

ax2 + bx + c = 0
where,
a, b, and c are coefficient and real numbers and also a ≠ 0.
If a is equal to 0 that equation is not valid quadratic equation.


"""

# Python program to find roots of a quadratic equation

# Importing the math module
# import math
#
# # Taking input from the user for coefficients
# a = float(input("Enter coefficient a: "))
# b = float(input("Enter coefficient b: "))
# c = float(input("Enter coefficient c: "))
#
# # Step 1: Check if a is zero (then it's not a quadratic equation)
# if a == 0:
#     print("Input correct quadratic equation")
# else:
#     # Step 2: Calculate the discriminant
#     dis = b * b - 4 * a * c
#     sqrt_val = math.sqrt(abs(dis))
#
#     # Step 3: Check the condition for discriminant
#     if dis > 0:
#         print("Real and different roots")
#         root1 = (-b + sqrt_val) / (2 * a)
#         root2 = (-b - sqrt_val) / (2 * a)
#         print("Root 1:", root1)
#         print("Root 2:", root2)
#     elif dis == 0:
#         print("Real and same roots")
#         root = -b / (2 * a)
#         print("Root:", root)
#     else:
#         print("Complex Roots")
#         real_part = -b / (2 * a)
#         imaginary_part = sqrt_val / (2 * a)
#         print("Root 1:", real_part, "+ i", imaginary_part)
#         print("Root 2:", real_part, "- i", imaginary_part)


"""
Q21 WAP to calculate area & perimeter & volume of 
-> cicle 
-> square 
-> rectangle 
-> rhombus 
-> cylinder 
"""

#Circle
# Program to calculate area and perimeter of a circle
# Import the math module
# import math
#
# # Take input from user
# radius = float(input("Enter the radius of the circle: "))
#
# # Calculate area and perimeter
# area = math.pi * radius * radius
# perimeter = 2 * math.pi * radius
# print("Area of the circle is:", area)
# print("Perimeter (Circumference) of the circle is:", perimeter)
#
# #__________________________________________________________________________________________________________________________________________
#
# #Rectangle
# # Program to calculate area and perimeter of a rectangle
# length = float(input("Enter the length of the rectangle: "))
# width = float(input("Enter the width of the rectangle: "))
#
# # Calculate area and perimeter
# area = length * width
# perimeter = 2 * (length + width)
#
# # Display the results
# print("Area of the rectangle is:", area)
# print("Perimeter of the rectangle is:", perimeter)
#
# #__________________________________________________________________________________________________________________________________________
#
# #Square
#
# # Program to calculate area and perimeter of a square
#
# # Take input from user
# side = float(input("Enter the side length of the square: "))
#
# # Calculate area and perimeter
# area = side * side
# perimeter = 4 * side
#
# # Display the results
# print("Area of the square is:", area)
# print("Perimeter of the square is:", perimeter)
#
# #__________________________________________________________________________________________________________________________________________
#
# #Cylinder
# # Program to calculate surface area and volume of a cylinder
#
# # Import the math module
# import math
#
# # Take input from user
# radius = float(input("Enter the radius of the base of the cylinder: "))
# height = float(input("Enter the height of the cylinder: "))
#
# # Calculate surface area and volume
# surface_area = 2 * math.pi * radius * height + 2 * math.pi * radius * radius
# volume = math.pi * radius * radius * height
#
# # Display the results
# print("Surface area of the cylinder is:", surface_area)
# print("Volume of the cylinder is:", volume)
#
# #__________________________________________________________________________________________________________________________________________
#
# #Rhombus
# # Program to calculate area and perimeter of a rhombus
#
# # Take input from user
# diagonal1 = float(input("Enter the length of the first diagonal of the rhombus: "))
# diagonal2 = float(input("Enter the length of the second diagonal of the rhombus: "))
# side = float(input("Enter the length of a side of the rhombus: "))
#
# # Calculate area and perimeter
# area = (diagonal1 * diagonal2) / 2
# perimeter = 4 * side
#
# # Display the results
# print("Area of the rhombus is:", area)
# print("Perimeter of the rhombus is:", perimeter)


#________________________________________________________________________________________________________________________________________________________________________________________


