
"""
 Q1. What is sep keyword argument in print function ?
 -> So sep is a keyword argument in print function 
    in python . It's default value is space 
    ex =  print("hello","how","are","You",sep=" ")


    a,b,c,d=10,20,30,40
    print("hello","how","are","You" ,sep="->",end="")
    print("1","2","3","4")
    print(a,b,c,d,end="\n")
    print("hello")


    print("abhishek","pratham","Rahul",sep="\n",end="\t")
    print("hello how are you","1,2,3,4",sep="->",end="\n")
    print("we are learning python",sep="?",end='how is the josh')

"""

print("Lalit",sep=" himanshu\tkrish ",end=" devendra\n")
print("amit ","abhishek","Lucky","Vanshaj",sep="\t\\",end="\n")
print("anushka,pallavi,madhu",sep="?",end="\rAman tere sang.. ")

"""
Lalit devendra
amit    \abhishek   \lucky  \vanshaj
Aman tere sang..



print("Lalit",sep=" himanshu\tkrish ",end=" devendra\n")
print("amit ","abhishek","Lucky","Vanshaj",sep="\t\\",end="\n")
print("anushka,pallavi,madhu",sep="?",end="\rAman tere sang.. ")

Lalit himanshu  krish devendra
amit    abhishek    lucky   Vanshaj
Aman tere sang..

Lalit devendra
amit \abhishek\lucky\Vanshaj 
Aman tere sang.. madhu      


"""

