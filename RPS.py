import random
list = ['Rock','Paper','Scissor']
player1=input("Enter the name of Player 1: ")
player2=input("Enter the name of Player 2: ")


choice = 1
while choice:
    player1_Pick = random.choice(list)
    player2_Pick = random.choice(list)

    print(f"{player1} : {player1_Pick}")
    print(f"{player2} : {player2_Pick}")
    
    if player1_Pick == player2_Pick:
        print("Tie")
    elif player1_Pick == 'Rock' and player2_Pick == 'Scissor':
        print(f"!!!{player1} Wins!!!")
    elif player1_Pick == 'Rock' and player2_Pick == 'Paper':
        print(f"!!!{player2} Wins!!!")
    elif player1_Pick == 'Paper' and player2_Pick == 'Scissor':
        print(f"!!!{player2} Wins!!!")
    elif player1_Pick == 'Paper' and player2_Pick == 'Rock':
        print(f"!!!{player1} Wins!!!")
    elif player1_Pick == 'Scissor' and player2_Pick == 'Paper':
        print(f"!!!{player1} Wins!!!")
    elif player1_Pick == 'Scissor' and player2_Pick == 'Rock':
        print(f"!!!{player2} Wins!!!")
    print("---------------------------------------\n")
    entry = int(input("Again : 1\nQuit : 0\nchoice : "))
    if entry == 0:
        choice = 0
    
print("Thanks for playing the Game")