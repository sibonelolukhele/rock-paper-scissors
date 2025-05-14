import random

print("Welcome to Rock, Paper, Scissors!")


while True:

    options = ["rock", "paper", "scissors"]
    syschoice = random.choice(options)
    
    useranswer = input("\nSelect an option between Rock, Paper and Scissors to play the game and enter exit to stop: ").lower().strip()

    if useranswer == syschoice:
        print(f"\nSystem Choice: {syschoice.capitalize()}.\nYour Choice: {useranswer.capitalize()}.\nYou have tied!")
    elif useranswer == "rock" and syschoice == "paper":
        print(f"\nSystem Choice: {syschoice.capitalize()}.\nYour Choice: {useranswer.capitalize()}.\nYou have lost!")
    elif useranswer == "paper" and syschoice == "scissors":
        print(f"\nSystem Choice: {syschoice.capitalize()}.\nYour Choice: {useranswer.capitalize()}.\nYou have lost!")
    elif useranswer == "scissors" and syschoice == "rock":
        print(f"\nSystem Choice: {syschoice.capitalize()}.\nYour Choice: {useranswer.capitalize()}.\nYou have lost!")
    elif useranswer == "paper" and syschoice == "rock":
        print(f"\nSystem Choice: {syschoice.capitalize()}.\nYour Choice: {useranswer.capitalize()}.\nYou have Won, Congrats!")
    elif useranswer == "scissors" and syschoice == "paper":
        print(f"\nSystem Choice: {syschoice.capitalize()}.\nYour Choice: {useranswer.capitalize()}.\nYou have Won, Congrats!")
    elif useranswer == "rock" and syschoice == "scissors":
        print(f"\nSystem Choice: {syschoice.capitalize()}.\nYour Choice: {useranswer.capitalize()}.\nYou have Won, Congrats!")
    elif useranswer == "exit":
        break
    else:
        print("Please enter a valid option!")