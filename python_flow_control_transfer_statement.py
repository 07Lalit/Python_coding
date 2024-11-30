"""
                                         Flow Control
                                         ------------

3)Transfer Statement-:
  ----------------
-> Jump Statement/transfer statement are used to unconditionally transfer the program control
   to another part of the program .
   -> pass
   -> continue
   -> break

=> pass
--------
-> pass is a keyword .
-> In programming if we need such block which won't do anything than we can
   define that empty block with pass keyword .

   if True:                          while (10>4):
#     pass                           #     pass

 pass -> 1) It is a empty statement .
         2) It is a null statement .
         3) It won't do anything .

def fact(n):
    pass

--------------------------------------------------------------------------------------------------

                                      break
                                      -----

-> This statement is used to jump out of the loop .
-> This statement change the flow control of a particular program. It  basically  transfer
   the execution  of code .

   syntax-:

   while (True):
        break

   for i in  range(10):
        if i==6:
            break
        else:
           print("hello duniya")

-> so the break statement must be used inside a loop only .

-> break is used to terminate on loop based  or some condition .

-> when python executes a break statement inside a loop , it ends the exection of loop
   of control comes out of the loop . the remaining iteration of the loop won't happen .



------------------------------------------------------------------------------------------

                              continue
                              --------

-> We can use continue statement to skip current iteration and continue next iteration.
-> When python encounter an continue statement , it repeat the execution of
  all the remaining statement in the current Iteration of the loop and transfer the
  control to the top of the loop

ex-:
v=1
while v!=1 :
    if v%2==0:
        continue:
    else:
        print(v)
    v=v+1

output: 1 3 5 7 9


"""
# i=1
# while (i<=10):
#     if (i==4):
#         break
#     if(i==3):
#         break
#     if(i==1):
#         print("hello guys!!")
#     else:
#         print(i)
#     i=i+1
#



# for i in range(1,11):
#     if(i==6):
#         pass
#     if(i==1):
#         print("hello annu")
#     elif(i==4):
#         print("hello Kanchan")
#     if(i==1):
#         pass
#     elif(i==4):
#         pass
#     else:
#         print(i)
# print("hope you are enjoying class",chr(128512))


# i=1
# while i<=10:
#     if(i%2==0):
#         print("Code is like Humor when you have to explain it's bad ")
#     elif(i==7):
#         break
#     elif(i==5):
#         print("Everybody should learn to program because it teaches you how to think")
#     else:
#         print("Consistency is what transforms average into excellence ")
#
#     i=i+1


# brain=True
# empty=False
# if (brain != empty):
#     print("keep coding")
# else:
#     print("order coffee")



"""

"""


