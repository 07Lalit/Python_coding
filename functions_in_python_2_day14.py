"""
Q1. What is Functions in python ?
-> It is a named Piece of code which can be used as
   many time as we want to perform a specific task.

   In python we used a keyword called "def" to make
   function .

    If we want to use than we have to call name
    of the function

    def add(a,b):
        return a+b

    print(add(10,20))  # 30

--------------------------------------------------------

                TYPES OF FUNCTION
                ----------------

-> It is of 3 types-:
    1) Built-in function .
    2) module level function .
    3) user - defined fucntion.

 1) Built-in function -: Create by programming language
         for general use .
    -> We don't need to create we just have to use it.
    -> They are also known as global function
    -> 69+ (built in function in python).

    Built-in Functions

    A
    abs()
    aiter()
    all()
    anext()
    any()
    ascii()

    B
    bin()
    bool()
    breakpoint()
    bytearray()
    bytes()

    C
    callable()
    chr()
    classmethod()
    compile()
    complex()

    D
    delattr()
    dict()
    dir()
    divmod()

    E
    enumerate()
    eval()
    exec()

    F
    filter()
    float()
    format()
    frozenset()

    G
    getattr()
    globals()

    H
    hasattr()
    hash()
    help()
    hex()

    I
    id()
    input()
    int()
    isinstance()
    issubclass()
    iter()
    L
    len()
    list()
    locals()

    M
    map()
    max()
    memoryview()
    min()

    N
    next()

    O
    object()
    oct()
    open()
    ord()

    P
    pow()
    print()
    property()




    R
    range()
    repr()
    reversed()
    round()

    S
    set()
    setattr()
    slice()
    sorted()
    staticmethod()
    str()
    sum()
    super()

    T
    tuple()
    type()

    V
    vars()

    Z
    zip()

    _
    __import__()

    https://docs.python.org/3/library/functions.html


    kisi bhi name ke aage agar paranthesis laga ho to
    ushe function bolte hai.

    ------------------------------------------------------------------------------

                              2) Module -level function
                              -------------------------

  ->  The function cannot be us used directly we need to import
   their corresponding modules.

   ex -: import module_name

   Q What is modules in python ?
   -> Modules is a python file which is a collections of different type
      of class & functions.

   Q What is library/packages ?
   -> library is a collection of modules .
     modules is a collection of  a simple python file which is
     collection of different types of function .
         or
     Library is directory or folder which is a collection of relatable
     modules integerate for a specific task.

     Syntax-:

    import <module_name>
    print(<module_name>.<function_name>(parameter/argument))


-------------------------------------------------------------------------

                        User-defined function
                        --------------------

    -> Created by programmer.
    -> def Keyword is used to create user defined function .

        practical
        ---------




"""
# def add(a, b):
#     return a + b
#
# print(add(10, 20))

# import calendar
# print(calendar.calendar(2025))
a ="Aman hi hai"
b=" falna bhi hai"
c="python"
d="it"
print("Mera dusra pyyar Ashutosh hai parr pehle to "+a +"or "+b)
print(f" hii we are learning {c}")
print(f" we are enjoying learning {d}")

print(max(10,100,30,40,50))
l=[10,30,200,400,33]
print(max(l))
l1=["lalit","himanshu","anushka","krish"]

print(min(l1),max(l1))
print(min(12,30,40,40,1))
print(abs(-12))
a=-30
b=-90
print(abs(a)+abs(b))
print(f"id of a is : {id(a)}")
print(ord("'"))
print(ord('"'))
print(ord("#"))
print(chr(128512))
