""" Nested loop & pattern printing
    ------------------------------

for i in range(n):       #outer loop
    for j in range(n):   #inner loop
        #print()


while(condition):
    while(condition):
        print(logic of your program)

if (Condtion):
    pass
    if(condition):
        pass
        if(condion):
else:
    pass

"""

# i = int(input("Enter a number: "))
# if(i>=0):
#     print("I am inside if block")
#     if(i>=10):
#         print("i am inside nested if block (if-if)")
#         if(i>=20):
#             print("i am inside nested if block(if-if-if)")
#             print(f"I your i value is {i}")
#         else:
#             print("i am inside nested else block (if-if-else")
#
#     else:
#         print("i am inside nested else block (if-else)")
# else:
#     print("print your name",i,"hello",i,"hii")

# num=1
# for i in range(5):
#     for j in range(i):
#         print(num,end=' ')
#         num=num+1
#     print()


"""
Q1 WAP to print a pattern like this ?
->  
# # # # #
# # # # #
# # # # #
# # # # #
# # # # #
# # # # #


for i in range(1, 7):
    for j in range(1, 7):
        print("#", end=" ")
    print()
"""

"""
Q2  Wap to print pattern like this ?
# # # # #
* * * * *
# # # # #
* * * * *
# # # # #
* * * * *

for i in range(1, 7):
    for j in range(1, 7):
        if (i % 2 == 0):
            print("#", end=" ")
        else:
            print("*", end=" ")
    print()

"""

"""
Q3 WAP to print a pattern like this ?
->
# 
# # 
# # # 
# # # # 
# # # # #

"""

"""
Q4 WAP to print a pattern like this?
-> 
1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5 

a = 5
for i in range(1, a + 1):
    for j in range(1, i + 1):
        print(i, end=" ")
    print() 

"""

"""
Q5 WAP to print a pattern like this? 
1 
1 2 
1 2 3 
1 2 3 4
1 2 3 4 5

a = 5
for i in range(1, a + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
"""

"""
Q6 WAP to print a pattern like this ?
-> 
1 
2 3 
4 5 6 
7 8 9 10 
11 12 13 14 15 

count = 1
for i in range(1, 6):
    for j in range(1, i + 1):
        print(count, end=" ")
        count = count + 1
    print()

"""

"""
Q7 WAP to print a pattern like this ? 
-> 
A 
B C 
D E F 
G H I J 
K L M N O 
P Q R S T U 
V W X Y Z  



count = 65
for i in range(1, 8):
    for j in range(i):
        if (i == 7 and (j == 7 or j == 6 or j == 5)):
            print(chr(128512), end=" ")
        else:
            print(chr(count), end=" ")
        count = count + 1
    print()

"""


"""

Q8 WAP to print patter like this ?

* * * * * 
* * * * 
* * * 
* * 
* 

for i in range(5,0,-1):
    for j in range(i):
        print("*",end=" ") 
    print()
"""

"""
Q9 WAP to print pattern like this ?

_ _ _ _ * 
_ _ _ * * 
_ _ * * * 
_ * * * * 
* * * * * 


n=5
for i in range(1,n+1):
    for j in range(n-i):
        print("_",end=" ")
    for k in range(i):
        print("*",end=" ")
    print()
"""


"""
Q10 WAP to print pattern like this ?

1 2 3 4 5
1 2 3 4
1 2 3 
1 2 
1

for i in range(5,0,-1):
    for j in range(i,0,-1):
        print(j,end=" ")
    print()

"""

"""
Q11 WAP to print pattern like this ? 

_ _ _ _ * 
_ _ _ * * 
_ _ * * * 
_ * * * * 
* * * * * 

n=5
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end=" ")
    for k in range(i):
        print("*",end=" ")
    print()

"""


"""

Q12  WAP to print pattern like this ?

 _ _ _ _ *
 _ _ _ * * * 
 _ _ * * * * * 
 _ * * * * * * * 
 * * * * * * * * * 
n=5
for i in range(0,n):
    for j in range(0,n-i-1):
        print(" ",end=" ")
    for k in range(i+1):
        print("*",end=" ")
    for m in range(i):
        print("*",end=" ")
    print()

"""

"""

Q13 WAP to print pattern like this ?

* * * * * * * * *
_ * * * * * * * 
_ _ * * * * * 
_ _ _ * * * 
_ _ _ _ * 



n = 5
for i in range(n,0,-1):
    for j in range(n-i):
        print("_",end=" ")
    for k in range(i):
        print("*",end=" ")
    for l in range(i-1):
        print("*",end=" ")
    print()

"""

"""
Q14 WAP to print pattern like this ?

                  * 
                * * * 
              * * * * * 
            * * * * * * * 
          * * * * * * * * * 
        * * * * * * * * * * * 
      * * * * * * * * * * * * * 
    * * * * * * * * * * * * * * * 
  * * * * * * * * * * * * * * * * * 
* * * * * * * * * * * * * * * * * * * 
* * * * * * * * * * * * * * * * * * * 
  * * * * * * * * * * * * * * * * * 
    * * * * * * * * * * * * * * * 
      * * * * * * * * * * * * * 
        * * * * * * * * * * * 
          * * * * * * * * * 
            * * * * * * * 
              * * * * * 
                * * * 
                  * 

a = int(input(" Enter a number : "))
n = a//2
for i in range(0,n):
    for j in range(0,n-i-1):
        print(" ",end=" ")
    for k in range(i+1):
        print("*",end=" ")
    for m in range(i):
        print("*",end=" ")
    print()

for i in range(n,0,-1):
    for j in range(n-i):
        print(" ",end=" ")
    for k in range(i):
        print("*",end=" ")
    for l in range(i-1):
        print("*",end=" ")
    print()

"""

"""
Q15 WAP to print pattern like this ?

* 
* * 
* * * 
* * * * 
* * * * * 
* * * * * 
* * * * 
* * * 
* * 
* 


n=5
for i in range(1, n+1):
    for j in range(i):
        print("*",end=" ")
    print()
for i in range(n,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()
    
"""
"""  
Q16 WAP to print pattern like this ?
1 
0 1 
1 0 1 
0 1 0 1 
1 0 1 0 1 


for i in range(0,5):
    for j in range(0,i+1):
        if((i==j) or  ((i+j)%2 == 0) ):
            print("1",end=" ")
        else:
            print("0",end=" ")
    print()

"""

"""
Q17 WAP to print pattern like this ?

1 _ _ _ _ _ _ _ _ 1 
1 2 _ _ _ _ _ _ 1 2 
1 2 3 _ _ _ _ 1 2 3 
1 2 3 4 _ _ 1 2 3 4 
1 2 3 4 5 1 2 3 4 5

n=5 
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    for k in range(n-i):
        print("_",end=" ")
    for l in range(n-i):
        print("_",end=" ")
    for m in range(1,i+1):
        print(m,end=" ")
        
    print()
"""

"""
Q18 WAP to print the given pattern ?
A 
A B 
A B C 
A B C D 
A B C D E

n=5
ch= 65
for i in range(1,n+1):
    for j in range(ch,i+ch):
        print(chr(j),end=" ")
    print()
"""



"""
Q19 WAP to print given pattern ? 
A B C D E 
A B C D 
A B C 
A B 
A 

n=5 
ch= 65        
for i in range(n,0,-1):
    for j in range(ch,i+ch):
        print(chr(j),end=" ")
    print()
"""


"""
Q20 WAP to print pattern like this ? 

A 
B B 
C C C 
D D D D 
E E E E E 

n= 5 
ch= 65 
for i in range(ch,n+ch):
    for j in range(ch,i+1):
        print(chr(i),end=" ") 
    print()
"""

"""
Q21 WAP to print like this?
_ _ _ _ A 
_ _ _ A B A 
_ _ A B C A B 
_ A B C D A B C 
A B C D E A B C D 

n= 5 
ch= 65 
for i in range(1,n+1):
    for j in range(n-i):
        print("_",end=" ")
    for k in range(ch,ch+i):
        print(chr(k),end=" ")
    for l in range(0,i-1):
        print(chr(ch+l),end=" ")
    print()
"""


"""
Q22 WAP to print pattern like this ? 

* * * * * * * * * * * * * * * * * * * * 
* * * * * * * * *     * * * * * * * * * 
* * * * * * * *         * * * * * * * * 
* * * * * * *             * * * * * * * 
* * * * * *                 * * * * * * 
* * * * *                     * * * * * 
* * * *                         * * * * 
* * *                             * * * 
* *                                 * * 
*                                     * 
*                                     * 
* *                                 * * 
* * *                             * * * 
* * * *                         * * * * 
* * * * *                     * * * * * 
* * * * * *                 * * * * * * 
* * * * * * *             * * * * * * * 
* * * * * * * *         * * * * * * * * 
* * * * * * * * *     * * * * * * * * * 
* * * * * * * * * * * * * * * * * * * *

n= 20
for i in range(0,n//2):
    for j in range(n//2 - i):
        print("*",end=" ")
    for k in range(i):
        print(" ",end=" ")
        
        
    for l in range(i):
        print(" ",end=" ")
    for m in range(n//2 - i):
        print("*",end=" ")
    print()
    
for i in range(1,n//2 + 1):
    for j in range(i):
        print("*",end=" ")
    for k in range(n//2 - i):
        print(" ",end=" ")
        
    for l in range(n//2 - i):
        print(" ",end=" ")
    
    for m in range(i):
        print("*",end=" ")
    print()

"""


"""
Q23 WAP to print like this ?

* _ _ _ _ _ _ _ _ * 
* * _ _ _ _ _ _ * * 
* * * _ _ _ _ * * * 
* * * * _ _ * * * * 
* * * * * * * * * * 
* * * * _ _ * * * * 
* * * _ _ _ _ * * * 
* * _ _ _ _ _ _ * * 
* _ _ _ _ _ _ _ _ * 

n=5 
for i in range(1,n+1):
    for j in range(i):
        print("*",end=" ")
    for k in range(n-i):
        print("_",end=" ")
    for l in range(n-i):
        print("_",end=" ")
    for m in range(i):
        print("*",end=" ")
    print()
    
for i in range(1,n):
    for j in range(n-i):
        print("*",end=" ")
        
    for k in range(i):
        print("_",end=" ")
    
    for l in range(i):
        print("_",end=" ")
        
    for m in range(n-i):
        print("*",end=" ")
    print()
"""



"""
Q24 WAP to print pattern like this ? 
-> * * * * * 
   *       * 
   *       * 
   *       * 
   * * * * * 
   
n= 5 

for i in range(0,n+1):
    for j in range(0,n+1):
        if (i==0 or j==0 or i==n or j==n):
            print("*",end=" ")
        else:
            print(" ",end=" ")
            
    print()
    
"""


"""
Q25 WAP to print pattern like this ? 

1 1 1 1 1 1 
1 1 0 0 0 1 
1 0 1 0 0 1 
1 0 0 1 0 1 
1 0 0 0 1 1 
1 1 1 1 1 1

n = 5

for i in range(0, n + 1):
    for j in range(0, n + 1):
        if (i == 0 or j == 0 or i == n or j == n or i==j):
            print("1", end=" ")
        else:
            print("0", end=" ")

    print()

"""

"""
Q26 WAP to print pattern like this ? 
-> 
5 5 5 5 5 5 5 5 5 5 
5 4 4 4 4 4 4 4 4 5 
5 4 3 3 3 3 3 3 4 5 
5 4 3 2 2 2 2 3 4 5 
5 4 3 2 1 1 2 3 4 5 
5 4 3 2 1 1 2 3 4 5 
5 4 3 2 2 2 2 3 4 5 
5 4 3 3 3 3 3 3 4 5 
5 4 4 4 4 4 4 4 4 5 
5 5 5 5 5 5 5 5 5 5

n= 10
for i in range(n):
    for j in range(n):
        if (i==0 or j==0 or i==n-1 or j==n-1 ):
            print("5",end=" ")
        elif(i==1 or j==1 or i==n-2 or j==n-2):
            print("4",end=" ")
        elif(i==2 or j==2 or i==n-3 or j==n-3):
            print("3",end=" ")
        elif(i==3 or j==3 or i==n-4 or j==n-4):
            print("2",end=" ")
        else:
            print("1",end=" ")
    print()


"""




