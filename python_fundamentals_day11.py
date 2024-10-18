"""
                Escape Sequence
                ---------------

  -> In python there are some sequence of character
    which cannot be print by using print function
    on the screen .

    These escape sequence have different meaning for
    python.

    1) \  -> backslash
    2) \\ => doubleslash is used to insert a backslash
    3) \n => It is used to insert a newline
    4) \t => It is used to move cursor to next tab space.
    5) \r => carriage return
    6) \f => formfeed




#
# print("Lalit\\\\gour")
# print("Hello welcome to today's class \nKrish")
# print("Anushka\t\t\tgour")
# print("lalit\rgour\ranushka")

----------------------------------------------------------
Q What is print function in Python ?
-> So if you want to print anything on the screen
  you have to use print function
  print()
  -> print("hwwl wotril")
     print("jkgsl")
   python me apne app automatically line change
   ho jati hai jitni baar bhi print() use karoge
   to cursor next line prr switch ho jayega.

  -> print ek function hai or jiss name ke aage paranthesis () hoga
     bo python me or sabhi language me function hoga .

  print("" , end="\n",sep=" ")

  -> python me internally line change hoti hai . kisi bhi function
     ke andar jo paranthesis ke andar pass karte argument ya fir
     parameter bolte hai .

   so python has different types of parameters

   for example

   print("Lalit",end="\n",sep=" ")
   so lalit -> is a Positional argument
   and jo iske andar internally end,sep hai unhe bolte hai Keyword
   arguments .






"""

# print("himansu amit gourav harsh",end="\r")
# print("krish")
#himanshu amit gaourav harsh    krish

print("apple",end="?")
print("bannana",end="\t")
print("mango",end="orange\tchiku")

#apple?bannana  mangoorange chiku

"""
What we should not do  while using keyword argument end-:
1) print("lalit",end="\n",end="\t") 
2) print(end="\n","hii i am Lalit"
"""

