#encoding=utf-8
number = 23
running = True
while running:
    guess = int(input("Enter an integer :"))
    if guess == number:
        print("Congratulation,you guessed it.")
        running = False#this causes the while loop to stop
    elif guess < number:
        print("No it is a little higher than that")
    else:
        print("No ,it is a little lower than that")
else:
    print("The while loop is over")
    #Do anything else you want to do here
print("done")