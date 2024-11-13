"""
 Q.1  What are Datatypes in python?
 -> It represent the type of value get stored in a variable .
    data+type = Datatype

 -> In python we don't need to specify the data type explicitly
    ( alag se/khud se) . based on the value the type will be
    assigned automatically hence python is called Dynamic typed
    programming language.

    c ->  int a =10;      python ->  a=10 , a="krish"

    In python datatypes are grouped in 6 types (total 14 ) -:
    1) Numeric type -: int , float , complex .
    2) Sequence type -: String , list,tuples, bytes,byte arrays,range.
    3) Boolean type -:  bool
    4) Set type  -: set , frozenset
    5) Mapping type-: dictionary
    6) None type -: None

    So there are some major points we should remember about the
    data type they are-:
    1) Data type are dynamic type in nature.(matlab run time prr
       interpreter decide karta hai ki variable kis datatype ka
       hai variable ki value ko dekh karr).
    2) python me data type ka size fix nahi hota hai .
    3) The size of any data type can be expand and shrink according
       to the value assigned to it .
    4) In python we can change the datatype of any variable
       anytime or anywhere in the code
       example-:
           a= 10
           print(a)
           a="lalit"
    5) datatype in python are unbounded.
    -> There is no any predefined range of values for any
       datatype.
    -> we can store as many as big value as we can.
       (jab tak ki apki ram ki memory full nahi ho
        jati utni badi value rakh sakte hai in python)
    example-:
    c,c++-:                        python-:
    int a= 1239595                 a=8958295339205829528058
    long int  a =18483953893

__________________________________________________________________

                    I) Numeric Data type
                    -------------------
     1) Integer type -> int
     -------------

     declare  a= 10;  # integer type
     #  type(a)    #< class int >
     In python there are four ways to represent integer .
     ( we can assign an integer value to a variable in many way)

 1) Decimal form  -> range(0,9)
 2) Binary form   -> range(0,1)
 3) Octal form    -> range(0-7)
 4) Hexadecimal form  -> range(0-9-A-F)

 bin() , oct(12) , hex() .

a= 0B1010  # zero and b ko B small ya capital lena hai  # binary type
print(type(a), a)

b = 0o01237
print(type(b),b)

c = 0XFACE
print(type(c),c)

print(bin(20))
print(format(20,'0o'))

   # w3school python course
   # geeksforgeeks python course


 important rules-:

 i) For python the default form is decimal .
 ii) It can take values of integer in any form but return it as always decimal.
 iii) being a programmer be can specify integer literal value in  decimal,
      binary , octal & hexadecimal form but PVM (interpreter) will always
      provides value only in decimal form.

    2) binary form(0-1) -:  So,the prefix is 0b or 0B .
        ex-:  num= 0b1010  # 10 (decimal form me output milega print karenge to )

    3) Octal form(0-7) -: Prefix 0O or 0o .
        ex-:  num= 0o1293  # decimal me convert
        print(type(num))  -: <class 'int'>

    4) Hexadecimal form(0-9,A-F,a-f) -: prefix used in 0x or 0X .
        ex-: num= 0xFace   # decimal me convert kar dega.

------------------------------------------------------------------------------------

            Base Conversion in python
            -------------------------

    1) bin() -: convert any number form to binary
    2) oct() -: convet any number form to octal form
    3) hex() -: convet any number form to hexadecimal form.

    But when we convert them using these function we also get prefix of
    them in the starting after converting

    ex-: num = 10
         print(bin(10))
         # output-: 0b1010

    So to remove that prefix value form the number python introduce a new
    function named is format()

    -------------------------------------------------------------------------------

                            format()
                            --------

    -> So this function takes two parameter from the user
       first is the number that we want to convert .
       second we have to write the prefix to the type in which we want to convet
       ex is '0b' , '0x' , '0o' .
       but we should take care that we should always pass the prefix in
       lower case and also using single quotes if not then we will get error.

       so let's give one ex -:   num=10
                                 print(format(num,'0b'))
                                 output: 1010

       so there is one special case also we can d

       ex-: num = 0000001010

       note=: format function always return the value in string form
              you can check using type function .







"""
# num1 = 0b1010
# num2 = 20
# print(num1+num2)

