num_int = int(input("Input a number: "))    # Do not change this line
 #I ask the user for input. max_int takes the value of the higest integer that has been entered.
 #The while loop asks for input until a negative integer is intered.
max_int=0

while num_int>=0:
    if max_int < num_int:
        max_int=num_int
    num_int=int(input("Input a number: "))
print("The maximum is", max_int)    # Do not change this line

