# Python Interview Programs, May 22, 2022
# Written by V I E R U S
# This program reverses a string and a list via user input 
#----------------------------------------------------------------------------------
#STRING-----------------------------------------------------------------
#User Input
Userstring = input("Enter a string to reverse it: ")
Reversestring = Userstring[::-1]                            #slicing
print(Userstring + " is now reversed: " + Reversestring)

#NUMBERS----------------------------------------------------------------
#User Input
Usernum = []                                                #Empty List
Userlist = input("Enter a list with spaces ")               #User Input
Usernum.append(Userlist[::-1])                              #Add input to empty list and Slicing
print(str(Userlist) + " is now reversed: " + str(Usernum))  #Output