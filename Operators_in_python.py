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

-> If one value is float all calculation is in float .
   ex-:  10.2/2 => 5.0
   ex-:  10.2//2 => 5.0

-> '/' -> return float till 16 digit precision .

-> Arithemetic opearator can be used for all Number type (int,float , complex) .

-> + & * these two operators can also used on strings .



ex-: a ="101"
     b = "La"
     c = "303"
     d = "lit"

     print(a+c)
     print(b+d)

-> Arithametic operator can be used for all Numbertype (int,float , complex)
-> "+" & "*" these two operators can also used on strings.
-> if we add two string using + operator than in programming we call it we have done
   concationation of two strings .

-> "*" -> string multiplication operator or normal multiplication operator
-> '+" -> string concatination operator .


___________________________________________________________________________________________

                         comments in python
                         ------------------

-> In python there are two types of comments
  1) Single line comments .
  2) Multi line comments .

1) Single line comments -> Single line comment is the official way of comment (rocommendation)
                          by python .

2) Multiline comment is unofficial way of comment (not recommended)

-> PEP( python Enhancement proposal)
  # It is a type of rule book of python (psf or develper of python)
  # It is a python style guide .
  # Website -: developed by psf which tell's which things are recommendation by tpython .






"""
#print(2.0//2)
#print(22/7)
a= 121
b= 200
c = "11"
d= "22"
e = "la"
f ="lit"
print(a+b ,type(a), type(b))
print(c+d , type(c) ,type(d))
print(e+f , type(e) , type(f))

a ="*"
for i in range(1,6):
    print(i*a)


n = int(input("Enter a number till you want sum of n nutural number : "))
print((n*(n+1))//2)





