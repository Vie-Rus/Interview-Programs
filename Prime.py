# Python Interview Programs, May 22, 2022
# Written by V I E R U S
# This program finds out if the number you inputted was a prime number or not.
#----------------------------------------------------------------------------------
#User Input
Usernum = int(input("Enter a number: "))

if Usernum > 1:
    for i in range(2, Usernum):
        if (Usernum % i)==0:
            print(Usernum, ": is NOT a prime number")
            break                                       #Break once it figures out its not prime
    else:
        print(Usernum, ": is a prime number")           #Else it's prime
else:
    print(Usernum, "is not a prime number")             #If all else it won't be prime