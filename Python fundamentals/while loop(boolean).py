play_game = True

while play_game:
    continue_playing = input("Would you like to continue playing the game? y/n")

# we use the function .lower() to tell python y and Y are the same
# in python lower case is a different string to uppercase
    if continue_playing.lower() == "y":
        print("You have decided to continue playing the game.")
    elif continue_playing.lower() == "n":
        print("Now closing the game...")
        play_game = False
    else:
        print("That is not a valid option. Please try again.")

print("Thanks for playing")