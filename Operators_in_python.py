"""
                     Operators in python
                     --------------------

-> They are the special symbols or words that perform
   certain operations .

  c = a+b
  c => L.H.S
  a+b => R.H.S

  operands -: c , a , b
  operators -: '+'

-> Values on which operation is performed is called
   operand.
-> Operation which is performed by the special symbol
   are called operator .

----------------------------------------------------------------------

-> So there are 7 type of operators in python.
  1) Arithemetic operator .
  2) Relational / comparison .
  3) Logic operator .
  4) Bitwise operator .
  5) Assignment operator.
  6) Membership operator .
  7) Identity Operator .

Although there are several more operator present .

ex-: index operator [] . slicing operator [::] ,
     memeber access operator   calendar.calendar(2025)

________________________________________________________________________

            1) Arithemetic Operator
            ------------------------

-> So Arithemetic operators are also of 7 types -:
i)    '+'   -> Addition
ii)   '-'   -> Subtraction
iii)  '*'   -> Multiplication
iv)   '/'   -> Division operator
v)    '//'  -> floor division operator or Integer division operator .
vi)    '%'  -> modulo operator or remainder operator
vii)  '**'  -> power Operator .

-> For Arithemetic operators both datatype must convert to similar data type .

-> python always convert from Integer to float but vice versa is not possible .
   because of data lose until programmer force to convert it .

-> If one val



___________________________________________________________________________________________________


"""
                    # 3) Logical operator
                    # -------------------------

#  and -> If first condition is false than it will not check the second cond .
#         ex-: 10>5 and 5<10
#
#  or -> If first condition is True than it will not check for second
#       condition.
#
# not -> not operator works on only one operand .
#
#       a = 10>5
#       print(not(a))
#
#
# _____________________________________________________________________________________________
#

"""

"""
"""
                    3) Logical operator 
                    -------------------------

 and -> If first condition is false than it will not check the second cond .
        ex-: 10>5 and 5<10 

 or -> If first condition is True than it will not check for second 
      condition. 

not -> not operator works on only one operand .

      a = 10>5 
      print(not(a)) 


_____________________________________________________________________________________________

               4) Assignment operator "=" 
               ------------------------------ 

-> We use this operator put / assign value to a variable . 

ex-:  

a = 10 
b = 20.4 
c = True 
d = 45.6+8j 
e = [1,2,3,4] 
f = "python" 
g = {1:"anushka" , 2: "krish"} 

s = (1,2,3,4)


python does not have increment and decrement operator .


              compound assigemnet operator / shorthand operator 
              --------------------------------------------------

-> a = a*10        ->   a*=10  
-> b = b//10       ->   b//=10 
-> c = c+10        ->   c+=10 
-> d = d+1         ->   d+=1
i++ j++ i-- j--  python doesn't support this operator 



______________________________________________________________________________________________________



                     5) Bitwise Operator 
                     --------------------- 

-> It works on bits .
  { 8 bits = 1 byte 
   1024 byte = 1kb 
   1024 kb  =  1 MB  
   1024 MB  =  1 GB 
   1024 GB  =  1 TB 
   1024 TB  =  1 PB 
   1024 PB  =  1 EB 
   1024 EB  =  1 ZB 
   1024 ZB =   1 YB 
   }

 -> This is applicable only for int and boolean data type .

 -> If other datatype -> typeError 

 -> Types of Bitwise operator -: 
   I)    &  -> Bitwise and 

   II)   |  -> Bitwise or 

   III)  ^  -> Bitwise xor 

   IV)   ~  -> Bitwise not 

   V)    >> -> Bitwise right shift 

   VI)   << -> Bitwise left shift 


-> Fast ( it is easy to handle because in bits 0,1 ) in execution time .


-------------------------------------------------------------------------------------

                         I) Bitwise and  "&" 
                        ----------------------

-> Convert number into binary . If bits are one than ans will be one otherwise zero .

   a = 14 
   b = 10 


a=35 
b= 40 
print(a&b)

a=139
b=197 
print(a&b)


______________________________________________________________________________________________________________________


                        II) Bitwise or  
                        ---------------

-> If Bitwise of a|b if one of the  bits are one then answer will be one .

  1 or 0  -> 1 
  0 or 1  -> 1 
  1 or 1  -> 1 
  0 or 0  -> 0  





a= 77 
b = 99 
print(a|b)

c = 159 
d = 229 
print(bin(c),bin(d)


___________________________________________________________________________________________________________________ 

                        III) Bitwise xor operator 
                        -------------------------- 

-> xor operator -> a^b . If both bits is same than answer is zero (0) otherwise (1) .

 Truth table of xor operator -> 

 1 xor 1  -> 0 
 0 xor 0  -> 0 
 1 xor 0  -> 1 
 0 xor 1  -> 1   


"""

a = 10
b = 15
print(a ^ b)

print(21 ^ 18)
"""



# print(True or False)

# print(True and True)

# if 0.0 and "lalit":
#     print("True")
# else:
#     print("False")

# if "" or 0.1:
#     print("True")
# else:
#     print("False")

# if not "lalit":
#     print("True")
# else:
#     print("False")

# if( "himanshu" or "0") and (0.0 and 1.0) :
#     print("True")
# else:
#     print("False")


# if "0" and 1.0:
#     print("True")
# else:
#     print("False")


________________________________________________________________________________


                IV) Bitwise complementary operator 
                ----------------------------------

-> The bitwise complement operator is a unary operator (works on only 
    one operand). It takes one number and inverts all bits of it. When 
    bitwise operator is applied on bits then, all the 1’s become 0’s and
    vice versa. The operator for the bitwise complement is ~ (Tilde).
    
    For any integer n, the bitwise complement of n will be -(n+1)
    
-> So in our memory positive number is directly represent in memory.

-> negative number represent in 2's compliment form in memory .


    
    ex-:
    
    Bitwise complement Operation of 2 (~ 0010 ): 
    0010 
   +   1
   -------- 
    0011   that is 3 but of negative
    

Note: 
The bitwise Complement of 2 is same as  the binary representation of -3 

____________________________________________________________________________________________________________________

                    V) Bitwise Left shift operator  "<<"
                    --------------------------------------
                    
-> x << b  -> The binary of x is shifted by x bits towards left. 

                      

n = 16
print(n<<2)

a = 99 
print(a<<2)

b = 122 
print(b<<4)

c = 69
print(c<<3)


                    VI) Bitwise Right shift operator 
                    ------------------------------------- 
                    
-> Binary of x will be shifted in right side by given bits 

Note-:
-> last bit of every odd number is always 1 .
 ex-: odd(11) -> 1011 in binary & 1 -> 1 
 ex-: even(10) -> 1010 & 1 -> 0 
ex -> 20>>2 


-> var = 10 
 left shift 10<<1  -> 10*2 -> 20 
 right shift 10>>1 -> 10//2 -> 5 

print(16>>2)

a = 99
print(a>>2)

b = 122 
print(b>>4)

c = 69
print(c>>3)

______________________________________________________________________________________________________

"""

                        6) Membership Operators
                        -------------------------
                        
-> Membership operators are used to test whether a particular 
   value is present in a sequence 
   (like a list, tuple, string, etc.).

->Operators:
-------------------------

i) in: Returns True if the specified value is found in the sequence.

ii) not in: Returns True if the specified value is not found in the sequence.

Examples:

# Using 'in' operator
----------------------
print("A" in "ANUSHKA")  # Output: True
print("Y" in "KANCHAN")  # Output: False


# Using 'not in' operator
--------------------------
print(2 not in [4, 6, 8, 2, 5])  # Output: False
print(5 not in [1, 2, 3, 4])      # Output: True

# Empty string check
print("" in "KRISH")             # Output: True (empty string is a 
                                                substring of every string)
print("abc" in "abcd")           # Output: True
print("xy" in "abcd")           # Output: False


Key Points:
-----------

->Membership operators work with sequence data 
    types like strings, lists, tuples, and sets.

->Empty strings are considered substrings of all strings.

_________________________________________________________________________________________

                            7) Identity Operators
                            -------------------------- 
                            
-> Identity operators compare the memory location of two objects. 
   They check whether two variables point to the same object in memory.
   
   if we have given any arithemetic operator in value1  means left hand part 
   and after evalutaion done . if the value 2 that is the right hand part of is
   also same than final  answer will  be True otherwise False because of 
   immutability concept in python .
   
   

Operators:
---------

I) is: Returns True if both variables refer to the same object.

II) is not: Returns True if the variables refer to different objects.

Examples:

# Example 1
x = 10
y = 10
z = 20
print(x is y)        # Output: True (both refer to the same object in memory)
print(x is z)        # Output: False


# Example 2
lst1 = [1, 2, 3]
lst2 = [1, 2, 3]
print(lst1 is lst2)  # Output: False (different objects, even if contents are the same)
print(lst1 == lst2)  # Output: True (contents are the same)

Key Points:
-----------

->  is checks for object identity, not value equality.

->  == checks for value equality.

  
x = 256
y = 256
print(x is y)  # Output: True

x = 300
y = 300
print(x is y)  # Output: False


___________________________________________________________________________________________

                 #Ternary Operator
                 -------------------
                 
-> The ternary operator allows for a single-line if-else condition.

Syntax:
value = `true_value` if `condition` else `false_value`
Examples:
# Example 1
x = 10
y = "EVEN" if x % 2 == 0 else "ODD"
print(y)  # Output: EVEN

# Example 2
a, b = 10, 20
result = a if a > b else b
print(result)  # Output: 20


_________________________________________________________________________________________________

                                # Operator Precedence
                                ----------------------
-> Operator precedence determines the order in which operators 
   are evaluated in an expression.

-> Precedence Order (Highest to Lowest):
 
1) Parentheses: ()

2) Exponentiation: **

3) Unary operators: +, -

4) Multiplication/Division: *, /, //, %

5) Addition/Subtraction: +, -

6) Relational operators: <, <=, >, >=

7) Equality operators: ==, !=

8) Logical AND: and

9) Logical OR: or

-> Example:
x = 10 + 20 * 2
print(x)  # Output: 50 (multiplication has higher precedence than addition)

x = (10 + 20) * 2
print(x)  # Output: 60 (parentheses alter the precedence)


_____________________________________________________________________________________________ 

                        #eval() Function
                        -----------------
-> The eval() function parses the expression passed to it and 
   evaluates it as a Python expression.

Syntax:
eval(expression)
expression: A string representing a valid Python expression.

Examples:
# Mathematical expression
result = eval("20 * 3 + 5")
print(result)  # Output: 65

# Using variables in eval
x = 10
y = 5
expression = "x * y + 10"
print(eval(expression))  # Output: 60


#  Key Points-: 

1) eval() is powerful but should be used with caution,
   especially with untrusted input.

2) It can execute arbitrary code, leading to security vulnerabilities.


___________________________________________________________________________________ 

                  # Unicode and chr() / ord() Functions
                  --------------------------------------
                  
I) ord() Function-: Returns the Unicode code of a given character.

print(ord("A"))  # Output: 65
print(ord("a"))  # Output: 97

II) chr() Function-: Returns the character corresponding 
       to a given Unicode code.

"""

a = 10 
b = 10 
c = 20 
print(id(a) , id(b) , id(c) , id(a+b))
print(id(a+b) )
print(a+b is c)

"""







