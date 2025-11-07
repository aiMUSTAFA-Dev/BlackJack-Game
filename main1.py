import random

def blackjack():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    player_points = []
    computer_points = []

    player_points = random.sample(cards, 2)
    computer_points = random.sample(cards, 2)
    # print(player_points, computer_points)

    print(f"Your cards: {player_points}, current score: ", sum(player_points))
    print(f"Computer's first card: ", computer_points[0])

    # FOR PLAYER 
    new_cards = True
    execute = True
    while new_cards:
        choice = input(f"Type 'y' to get another card, type 'n' to pass: ")
        if choice == 'y':
            new = random.choice(cards)
            player_points.append(new)
            print(player_points)
        else:
            new_cards = False

        if sum(player_points) > 21:
            print(f"Your final hand: {player_points}, final score: ", sum(player_points))
            print(f"Computer's final hand: {computer_points}, final score: ", sum(computer_points))
            print("You went over so you lose😢😢😢")
            execute = False
            break

    # FOR COMPUTER 
    execute2 = True
    if execute == True:
        while sum(computer_points) < 17: #take cards until sum is smaller than 17 ... >= this means when >= 17 then take cards.. else don't even take cards if smaller than 17
            new = random.choice(cards)
            computer_points.append(new)
            if sum(computer_points) > 21:
                print(f"Your final hand: {player_points}, final score: ", sum(player_points))
                print(f"Computer's final hand: {computer_points}, final score: ", sum(computer_points))
                print("Computer went over so you won😍😍😍")
                execute2 = False
                break

    if execute == True and execute2 == True : # neither went over so...
        print(f"Your final hand: {player_points}, final score: ", sum(player_points))
        print(f"Computer's final hand: {computer_points}, final score: ", sum(computer_points))

        if sum(player_points) > sum(computer_points):
            print("YOU win the game!!!!")
        elif sum(computer_points) > sum(player_points):
            print("COMPUTER win the game!!!!")
        else:
            print("The game is Draw!!")

    choice = input("Enter do you want to play Blackjack. IF yes click 'Y' otherwise 'N'").lower()
    if choice == "y":
        blackjack()

blackjack()


# random.sample .. gives unique element, no repetition but rep exists in blackjack game!