from clear_screen import clear_screen
from logo import logo
from question import quiz
from time import sleep
#Welcome message
print(logo)
print()
print("There are a total of 6 questions. You can skip a question anytime by pressing 'skip' ")
input("Press enter to get started...")
#input the players
players = input("Enter name of players seperated by a space: ").title()
#convert the input to a list
players_list = players.split(" ")
#convert the list to dictionary keys
dict_players = {}.fromkeys(players_list, 0)
#print(dict_players)
#iterate the players starting from the first
for index in range(0, len(players_list)):
    current_player = players_list[index]
    point = "..............................."
    for questions in quiz:
        print(point)
        print(f"It is {current_player}'s turn")
        attempts = 2
        while attempts > 0:
            print(f"> {str(quiz[questions]["question"]).title()}")
            answer = input("Enter an answer. (press skip to move to the next question): ").lower()
            if answer == "skip":
                break
            elif answer == quiz[questions]["answer"]:
                print("correct answer".title())
                dict_players[current_player] += 1
                attempts -= 1
                print(f"{current_player}'s score is {dict_players[current_player]}")
                break
            else:
                attempts -= 1
                print(f"Wrong answer \n you have {attempts} remaining for this question")
    if index < (len(players_list)-1):
        print(f"Goodbye {current_player}, {players_list[index + 1]}'s quiz is comming up in 10 seconds\n\
            The scren will be cleared so note your final result")
        sleep(10)
        clear_screen()
