# Python Interview Programs, May 22, 2022
# Written by V I E R U S
# This program is to see if your user input is a palindrome or not
#----------------------------------------------------------------------------------
#def function calls palidrome, parameters of user's inputted string
def palindrome(Userstring):
    if Userstring.lower() == Userstring[::-1].lower():      #Lower case your input and reverse it then compare if they are the same
        print(Userstring + ": This is a Palindrome")
    else:
        print(Userstring + ": This NOT is a Palindrome")    #If all else it won't be a palidrome
        

#User Input
Userstring = input("Enter your Palidrome: ")

#Calls on function
palindrome(Userstring)
