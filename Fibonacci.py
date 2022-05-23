# Python Interview Programs, May 23, 2022
# Written by V I E R U S
# Fibonacci - in which each fib number, is the sum of the two preceding number
#----------------------------------------------------------------------------------
#Calls on def fibonacci, parameter of user inputted number
def fibonacci(num):
    num1 = 0                                
    num2 = 1
    
    for i in range(num):                    #for range of your number, it counts how many times it should loop
        num3 = num1 + num2                  #add the two numbers equals to num3
        num1 = num2
        num2 = num3
        print(num3)                         #prints out the outcome and reloops 


#User Input
Usernum = int(input("Enter a number: "))
fibonacci(Usernum)                          #Calls on fibonacci fuction with your user number as a parameter








