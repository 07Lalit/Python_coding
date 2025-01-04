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




