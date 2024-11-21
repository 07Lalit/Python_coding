"""
               Flow control
               ------------

 ->    Flow control describes that order in which statement excutes at runtime.

  1) Conditional statement :
   if , elif , else .


  2) Transfer statement-:
  break , continue ,pass


  3) Iterative statements
  while , for loop .

  ------------------------------------------------------------------------

                     A) Conditional statement
                     ---------------------------
    if -> agar
    else -> yaa to / nahi to

    use -: used in decision making .

    1)  if is a keyword in python  :
      syntax-: if (condition):
                   prin
                   fijsgj
                   fkjg
               else:
                   rpitn;k

    -> parenthesis is optional in condtion .
      we must give 4 space identation to make a block of code .

    -> We cannot write any line between if -else .otherwise we get syntax error .

    if (condition):
        //abcd
        //abcd
    else:
        //abcd
        //abcd

    -> if block is possible without an else block but an else block is not possible
    without  if (because else block only runs if an condition of if block fails ) .

    if(10<5) :
        print()
    elif(5<10):
        print()
    elif(4>2):
        print()
    else:
        print()

    **********************************

    if(5>2):
        print("hello")
    if(2<1):
        print("hii")                          if -else
                                              if -elif -elif -else        if      if -elif

    elif(5>2):
        print('annu')
    if(55>=55):
        print('krish')

    elif():
       print('lalit')
    else:
        print('himanshu')

   #output -: hello




**********************************************************************************************************************************

                            Ternary operator
                            ------------------

->  In python there is no ternary operator we use single line if-else as ternary operator

    In c,c++ & java ternary operator are like this
    example to ternary operator in c,c++,java-:

    var_name = <condition> ? expression1 : expression2
    String result =   percentage>=40 ? "pass" : "fail" ;

->  Actually Guido van Rossum is against the ternary operator because it reduce the
    redability of a code so, it provides an alternative of it that is

    -> single line if-else :
    example:      ( var = expression1 if (conditon) else expression2  )
                    var =  "eligible to vote"  if (age>=18) else " Not eligible"


                        III) if-elif-else
                        ------------------

=>  if-else :   when do hi condition ho or in  case only two answer is possible.
    when we have multiple decision/condition we use if-elif-else .

    We can make code of month 0-12 print month name otherwise error.

    Note-:
-> if block is mandatory at the top
-> without if block ,elif block is not possible and also elif block is not possible
-> There must be atlest one if block .
-> else block is optional if-elif-else  ladder possible

-> If any of the if or elif block is executed than rest of
   or no other line or block will not be executed .

-> we cannot write anything b/w if elif else ladder .
    if(conditon):
        ------
    elif(condition):
        ---------
    elif(condition):
        ---------
    else:
        print()

-------------------------------------------------------------------------------













"""
# a =  int(input(" Enter a number: "))
# if (a%2==0):
#     print("even")
# else:
#     print("odd")

# num = int(input("Enter a number btw 1-7 :  "))
# if (num==1):
#     print("Monday")
# elif (num==2):
#     print("Tuesday")
# elif (num==3):
#     print("wednesday")
# elif (num==4):
#     print("Thursday")
# elif (num==5):
#     print("Friday")
# elif (num==6):
#     print("saturday")
# elif (num==7):
#     print("Sunday")
# else:
#     print("You entered a wrong input..!!")



# num = int(input("enter a number  "))
# print("squar of this number: ", num*num)
# print(f"cube of this number: {num*num*num}")


# age = int(input("Enter a number  "))
# if (age>=18):
#     print("he is eligible for vote ")
# else:
#     print("he is not eligible for vote ")


# age = int(input("Enter a number "))
# if(age<0):
#     print("incorrect age",chr(128514))
# elif(age<18):
#     print("minor",chr(128514))
# elif(age>18):
#     print("adult",chr(128515))
# else:
#     print("you are old")


# for i in range(1,11):
#     print(f" 2*{i} = {2 * i}")


# a = int(input("enter a number one:  " ))
# b = int(input("enter a number two:  " ))
# c = int(input("enter a number three:  " ))

# if(a>=b and a>=c):
#     print("largest a")
# elif(b>=a and b>=c):
#     print("largest b")
# else:
#     print("largest c")


# if(True):
#     print("hello anushka")
# str = "KANCHAN"
# print(str[::-1])
#
# print(chr(133))
#
# if(10>5):
#     print("hello world")
# if(False):
#     print("hii")
# else:
#     print("apple")
# if(10==10):
#     print("orange")
# elif(4>2):
#     print("byee")
# else:
#     print("how are you!!")

print( "hello world" if (35>10 and 40>99) else "hello Duniya")
print( "anushka " if 10<5 else "krish" if 200>5 else "Lalit" )

