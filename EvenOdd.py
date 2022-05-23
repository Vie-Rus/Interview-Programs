# Python Interview Programs, May 22, 2022
# Written by V I E R U S
# This program checks if your inputted number is even or odd
#----------------------------------------------------------------------------------
#User Input
Usernum = int(input("Enter a number: "))

if Usernum % 2 == 0:                    #If divided by 2 and equals 0 its even
    print(str(Usernum) + " is Even.")
else:                                   #Else it's odd
    print(str(Usernum) + " is Odd.")