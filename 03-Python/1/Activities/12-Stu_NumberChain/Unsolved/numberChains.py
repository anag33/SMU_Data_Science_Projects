#Ask user for a number

#print that range of numbers out to console

#wrap it all in a while loop

# inputNumber = int(input("How many numbers? "))
# for num in range(inputNumber):
#     print(num)


#check to keep going
keepGoing = "yes"
# WHILE LOOP
while keepGoing == "yes":
    #Prompt user
    inputNumber = int(input("How many numbers? "))
    #print numbers
    for num in range(inputNumber):
        print(num) #print

    #OUT OF FOR BLOCK
    keepGoing = input("Continue? ")