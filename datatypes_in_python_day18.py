"""
                      Sequence group
                      ----------------

  String datatype ->

  -> So sequence of charcters is known as string
    characters ka matlab hota kuch bhi "abc 1243 #%%%" agar quotes
    ke andare likha ho either a number , alphabets or special characters

     ex-: a ="kgjgal"
      print(type(a)) # <class 'str'>

  -> define in string class.
  -> str() is also a function in python used for typecasting .
  -> If we talk about other programming language
     there is a character datatype but in python
     there is no character datatype even character
     is treated in string .

  -> char in python is also represent in string .
  -> python string represent internally by
    using unicode value.

  string can be represnt using
  single ,double or triple quotes .
-----------------------------------------------------------------------------------------------
                       String datatype in python
                       -------------------------


  In Python, Strings are arrays of bytes
  representing Unicode characters.

Example:

"Geeksforgeeks" or 'Geeksforgeeks'
Python does not have a character data type, a single character
is simply a string with a length of 1. Square brackets
can be used to access elements of the string.

print("A Computer Science portal for geeks")


1) Creating a string ->

#using single quotes
a = 'lalit'
print(type(a))

# using double quotes
b= "anushka Gour"
print(b,type(b))

#using triple quotes ->
1) using single triple quotes
2) using double triple quotes

c = '''
    hello anushka & krish hope you are enjoying learning python
    hii
    hello
    how are
    you
    '''

print(c,type(c))
print(d,type(d))

# taking user input of string

str function is used .

a= str(input("Enter your name : " ))
print(a,type(a))

# str function is optional while taking input because input() function already take
 everthing as string .

# python is a case sensitive language  so it you declare two varible
a = 'lalit'
A = 'lalit'

---------------------------------------------------------------------------------------

                                 Indexing
                                 ---------

-> Each character of string get a number called Index .
   index denotes the location of a char in the string .

-> python support both positive (forward) and negative (negative)  indexing .


   a = 'lalit'
   This is Forward indexing or positive indexing
   start from  left to right (-> 0 to n) :
   l = 0
   a = 1
   l = 2
   i = 3
   t = 4

   but python also support negative indexing
   strats from ending to start or we can say right to left . (n-1 ,n-2 ..)

   l = -5
   a =  -4
   l = -3
   i = -2
   t = -1
  python has an opertor name index operator =   varibale[index]

  print(a[3])
->i

   print(a[5])

-> so there is a popular error known as index error which we get if we give
  wrong index in our index operator .

  ex- : a ='apple'
        print( a ,type(a) , a[6])

Note-: forward indexing availabe in all other programming languages but negative indexing
      only in python .


1) Forward indexing -:  > positive (+) index values
                        > left to right
                        > 0 based indexing (index start from zero )

2) backward indexing -: > -ve index values
                        > right to left
                        > -1 based indexing (as start from -1) from the ending character to first char

zero is non negative number
a = "mango"
print(a[0]) -> m
print(a[-0]) -> m

Note-: Index operator always take inter index value
print(a[3.5]) -> Run time error  , type error

______________________________________________________________________________________________________________

                         String slicing in python
                         -----------------------
-> Slicing is a way to extract portion of a string by
specifying the start and end indexes. The syntax for
slicing is string[start:end], where start starting
index and end is stopping index (excluded).

Slicing in python is the process fetching substring from a given string

"""

# a = 'lalit '
# print(a,type(a))
#
# b= ("anushka Gour")
# print(b,type(b))
#
# c = '''
#     hello anushka & krish hope you are enjoying learning python
#     hii
#     byee
#     '''
#
# d="""
# hello
# hii
# annu
# krish
# himanshu
# kanchan
# """
# print(c,type(c))
# print(d,type(d))
#
# #a= str(input("Enter your name : " ))
# #print(a,type(a))
#
# a = 'lalit'
# print(a,type(a))
# print(f"value at index 3 is : {a[3]}")
# print(a[5])

st = 'Manali'
#print(st[5]) #i
#print(st[4-2])#n
#print(st[4-3.0])
#print(st[3*2])

#print(st[-0])
# print(st[-4]) # n
# print(st[-3-1]) #n
# print(st[-6]) #M
# print(st[-7]) # IndexError


# slicing in python
#------------------

var = "VRINDHAVAN"
print(len(var) , type(var) ,var)

print(var[::1])
print(var[:])
print(var[::-2])
