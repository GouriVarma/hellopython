#FINAL PROJECT: THE NUMBER GUESSING GAME.

#Asking player's name 
player_name = input("Please enter you name: ")
print("Hello "+str(player_name)+"! Welcome to guess the number game")  #print function

#declaring a function
def guess_game():
    level = int(input("\nPick a level of difficulty\n1 for easy,2 for medium,3 for hard: "))  #asking the player for a difficulty level
                                                                                              #\n for new line
    
    #easy level
    if level == 1 :   # if statement
        print("\nOk,you have selected easy.you have 3 attempts\nHint: the number is between 1 and 10")
        hidden_num = 6   #assigning hidden number into a variable 
        attempts = 0     #assigning chances to another variable 
        
        while attempts<4:  #while loop with a condition
            guess = int(float(input("\nTake a guess ")))    #taking a guess from the player and converting to integer type
            attempts = attempts+1                         #incrementing chances until limit
            if guess<hidden_num and guess>0:              #using if statement and logical operator for accurate guesses
                print("Guess is too low. ")
            elif guess>hidden_num and guess<11:
                print("Guess is too higher ")
            elif guess==hidden_num:
                break                                     #break statement to stop the loop
            else:
                print("Hint: The number is a postive integer")
                continue                                  #continue statement to continue loop
        if guess==hidden_num:  # if statement
            print("\nCongratulations!,you guessed the number in",str(attempts),"guesses")     #correct guess
            
        elif guess != hidden_num:                 #(!=)  not equal to 
            print("\nOops,you have reached the guessing limit")      # player exhausted no of chances
           
    
    #medium level    
    elif level == 2:      
        print("\nOk,you have selected medium.you have 5 attempts\nHint: the number is between 1 and 50")
        hidden_num = 27             #assigning hidden number into a variable 
        attempts = 0                #assigning chances to another variable 
        while attempts<6:           #while loop with a condition
            guess = int(float(input("\nTake a guess ")))      #taking a guess from the player and converting to integer type
            attempts = attempts + 1
            if guess<hidden_num and guess>0:           # if statement and logical operator
                print("Guess is too low. ")
            elif guess>hidden_num and guess< 51:
                print("Guess is too higher ")
            elif guess==hidden_num :
                break
            else:
                print("Hint: The number is a postive integer")
                continue
        if guess==hidden_num:                         # if statement
            print("\nCongratulations!,you guessed the number in",str(attempts),"guesses")
            
        elif guess != hidden_num:
            print("\nOops,you have reached the guessing limit")
           
    
    #hard level
    elif level == 3:             
        print("\nOk,you have selected hard.you have 8 attempts\nHint: the number is between 1 and 100")
        hidden_num = 59               #assigning hidden number into a variable 
        attempts = 0                  #assigning chances to another variable 
        while attempts<9:             #while loop with a condition
            guess = int(float(input("\nTake a guess ")))  #taking a guess from the player and converting to integer type
            attempts = attempts + 1
            if guess<hidden_num and guess>0:          # if statement and logical operator
                print("Guess is too low. ")
            elif guess>hidden_num and guess<101:
                print("Guess is too higher ")
            elif guess==hidden_num:
                break
            else:
                print("Hint: The number is a postive integer ")
                continue
        if guess==hidden_num:                    # if statement
            print("\nCongratulations!,you guessed the number in",str(attempts),"guesses")
            
        elif guess != hidden_num:
            print("\nOops,you have reached the guessing limit")
        
        
    else:
        print("\nInvalid input: You have not selected any of the given levels") #executes if the player gives any other value for level
        return level    #return statement
#playing again
    while True :            
        play_again = input("\nDo you want to play again(y/n): ")           #asking the player to play again or not
        if play_again == "y":        # if statement
            print ("\n",guess_game()) #if the player wants to play again printing or calling the guess_game function again until player enters no
        elif play_again == "n":
            print("\nThankyou for playing")
            break                              #breaking the loop
        else:
            print("\nPlease enter y/n")
            continue                           #continuing in loop 

guess_game()   #funcion calling
