"""
                                  Type Casting / Type conversion
                                  -------------------------------

-> It is a process of conversion of one datatype into another datatype .
-> Every data type is not possible to convert into any of the datatype .

ex-: ans = 1  # it is of integer type
     ans = 1.0 # it is of float type

     Type conversion are of the two types -:
     1) Implicit type conversion.
     2) Explicit type casting .

I) Implicit type conversion -: This type conversion is done automatically by python
                               itself.
                               python perform when it is required not every time.

II) Explicit type conversion -: This to be done by programmer .
                                We use some in-built function for type casting .


__________________________________________________________________________________________________________

                     Explicit type casting
                     ---------------------

-> It is done by using inbuilt function
1) int()
2) float()
3) complex()
4) bool()
5) str()

-------------------------------------------------------------------------------
                                 1) int()
-> so we will study that what are datatypes we can change explicitly using int() .
-> int() will convert the provided data type value to integer data .

    float -> int conversion is possible
    boolean -> int conversion is possible
    int -> integer conversion is possible
    complex -> integer conversion is not possible .

a= 10
a = int(a)

a = 10.23
a = int(a)   # 10

a = 2.2 + 3j
a = int(a)    # It is not possible to convert complex to integer datatype

# a= int(4+5j)
# print(a)     # typeError

c = 4+5j
print(int(c.real),int(c.imag))

d = 0b1010
print(int(d))

#e= "ten"
#print(int(e))  # value error

print(int(23.456))

print(int("345.23"))   # valueError


a = "-123"
b = "-13"
c = "+123"
print(int(b))

Conclusion -:  We can convert any datatype to integer except complex.
               If we want to convert string type into int type , compulsory string should only
               contain integeral value & should be specified in base 10 .


________________________________________________________________________________________________________

                               2) float()
                               ----------

-> This is used to convert the value to float datatype .
 ex-:  a = 10
       print(float(a))  -> 10.0

 i) Integer -> float is possible
   ex-: int(10)  -> 10.0

 ii) Complex to float is not possible
     ex-:  print(float(3+9j))  # TypeError

 iii) Boolean to float possible .
    ex-: print(float(True))   -> 1.1
    ex-: print(float(False))  -> 0.0

 iv) string to float is possible -:
    ex-: print(float("+123"))  # 123.0
    ex-: print(float("-22.4"))  # -22.4
    ex-: print(float("seven")) # not possible valueError
        print(float("001076"))
v) integer to float example edge cases for leading zeros .
    print(float(00+001))   # synatx error  : leading zeros in decimal integer
    print(float(00+101))  # 101.0


conclusion -:  We can convert any value to float type except complex datatype values
               In string many cases are possible string should either int literal

______________________________________________________________________________________________________

                                III)  complex()
                                --------------
-> This function convert value of any datatype to complex datatype .
-> There are actually 2 parameters  complex(real , imag)

print(complex(3,4))  -> (3+4j)

print(complex(-3,4) -> (-3+4j)

print(complex(-3,-4)) -> (-3-4j)

print(complex(3,)) -> (3,0j)

print(complex(,-4)) -> Invalid syntax Error

print(complex(6))  ->  6+0j

print(complex(10.5)) -> (10.5 + 0j )

print(complex(True,False)) -> 1+0j

print(complex(False)) -> 0j

print(complex("ten"))  -> value error

print(complex("10")) -> (10+0j)

conculision -: Every datatype can be converted to complex datatype .

In string datatype if convert those string in which integer literal ,
float literal  wiht base 10 specify .

_____________________________________________________________________________________

                       Boolean()
                       ---------

-> Boolean datatype convet any datatype to True or False  .

  Note -: 1) Anything which is equivalant to zero or empty is -: False
          ex-:  0 ,  0.0 , 0+0j , " " , [] , False

          2) Anything except the first point is True
          ex-: True , 1, 1.1 , 1+0j , "lalit" , [2], ...

a = 0
print(bool(a)) -> False
b = 'lalit'
print(bool(b) ) -> True

print(bool("False") -: False
pritn(bool("d")) -: True

conclusion -: Each & every datatype can be converted to boolean datatype
         without any error .

---------------------------------------------------------------------------------------------

                    str()
                    ----

-> So each & every datatype can be converted to string using str() function
  without any error .

-> isme bass quotes hi lagana hai python ko so it's very easy .

ex- : print(str(22+0j)) -: '22+0j'
ex-: print(str(True)) -: 'True'
ex-: print(str(10)) -:  '10'
ex-:  print(str(20.33) -: '20.33'


-------------------------------------------------------------------------------









"""
#Implicit type casting example
# a = 10
# b = 2.5
# c= a+b
# print(type(a),type(b),type(c),c)
#
# a = False
# b = 100
# print(a*b)

# s = True
# b = True
# print(s+b)
print(complex("10"))

# a= int(4+5j)
# print(a)     # typeError

c = 4+5j
print(int(c.real),int(c.imag))

d = 0b1010
print(int(d))

#e= "ten"
#print(int(e))  # value error

print(int(23.456))

#print(int("345.23"))   # valueError


# a = "-123"
# b = "1-3"
# c = "-123"
# print(int(b))

#print(complex(,4))
# print(float("001076"))
# print(float(00+001))   # synatx error  : leading zeros in decimal integer
# print(float(00+101))  # 101.0

#print(complex(0,0))
#print(complex(False,False))

print(complex(-3,-4))