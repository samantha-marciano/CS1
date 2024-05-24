

#bring in the random library, which allows you to randomize things
import random

#displays the string "hi and welcome"
print("Hi and welcome!")

#set the initial user and computer scores as 0
user_score = 0
com_score = 0


#enter a forever loop
while True:

    #randomly select an integer between 1 and 5
    real_num = random.randint(1, 5)

    #prompt the user to guess an integer between 1 and 5 and store it in the variable guess
    guess = input("enter an integer between 1 and 5: ")

    #if the user enters "stop"
    if guess == "stop":

        #say bye and break the while loop, ending the program
        print("Bye!")
        break

    #otherwise, if the user's number is equal to the randomly generated number
    elif int(guess) == real_num:

        #then tell the user they won and add a point to their score
        print("You got it! Good job")
        user_score += 1

    #lastly, if the user's number is not equal to the randomly generated number   
    else:

        #then tell the user they lost and add a point to the computer's score
        print("Wrong number! Sorry")
        com_score += 1

    #at the end of the each round, print the score
    print("The score is: You - " + str(user_score) + ", Computer - " + str(com_score))

        


    
