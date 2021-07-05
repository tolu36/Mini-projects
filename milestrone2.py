import random

suits = ("Clubs", "Diamonds", "Hearts", "Spades")
ranks = (
    "Two",
    "Three",
    "Four",
    "Five",
    "Six",
    "Seven",
    "Eight",
    "Nine",
    "Ten",
    "Jack",
    "Queen",
    "King",
    "Ace",
)
bj_values = {
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5,
    "Six": 6,
    "Seven": 7,
    "Eight": 8,
    "Nine": 9,
    "Ten": 10,
    "Jack": 10,
    "Queen": 10,
    "King": 10,
    "Ace": 11,
}


class BJ_Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = bj_values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit


class BJ_Deck:
    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                create_card = BJ_Card(suit, rank)
                self.all_cards.append(create_card)

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        try:
            return self.all_cards.pop()
        except:
            return "No more cards left to deal."


class BJ_Player:
    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def add_cards(self, new_cards):
        if type(new_cards) == list:
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)

    def sum_value(self):
        total_value = 0
        for card in self.all_cards:
            total_value += card.value
        return total_value

    def clear_hand(self):
        self.all_cards.clear()

    def __str__(self):
        return f"Player {self.name} has {len(self.all_cards)} cards."


class BJ_Account:
    def __init__(self, name, balance):
        self.balance = balance
        self.name = name

    def __str__(self):
        return f"Account owner: {self.name}\nAccount balance: ${self.balance}"

    def deposit(self, num):
        try:
            self.balance = self.balance + num
            return f"You won ${num}, and your new balance is {self.balance}."
        except:
            return "Please enter a valid integer amount."

    def withdraw(self, number):
        try:
            if self.balance < number:
                return "Withdrawals may not exceed the available balance."
            else:
                self.balance = self.balance - number
                return f"{self.name}, you bet {number}."
        except:
            return "Please enter a valid integer amount."


def bet():
    bet_amount = ""
    while type(bet_amount) != int or bet_amount > player_one_bal.balance:
        try:
            bet_amount = int(input(f"{player_one.name}, enter your betting amount."))
        except:
            print("Please enter a proper integer.")
            continue
        if bet_amount > player_one_bal.balance:
            print("Bet amount can not exceed your current balance. Try again.")
            continue
    return bet_amount


def deal():
    deal = ""
    while deal not in ["Yes", "No"]:
        deal = input(
            f"{player_one.name} would you like to hit? (Yes or No)"
        ).capitalize()
        if deal not in ["Yes", "No"]:
            print("Wrong answer, try again.")
    return deal


def keep_playing():
    keep_playing = ""
    while keep_playing not in ["Yes", "No"]:
        keep_playing = input(
            f"{player_one.name}, do you want to keep playing Yes/No?"
        ).capitalize()
        if keep_playing not in ["Yes", "No"]:
            print("Wrong answer, try again.")
    return keep_playing


def ace_value():
    ace_value = ""
    while type(ace_value) != int or ace_value not in [1, 11]:
        try:
            ace_value = int(
                input(f"{player_one.name}, enter the value this Ace should be.")
            )
        except:
            print("Please enter a proper integer; either 1 or 11.")
            continue
    return ace_value


name = input("Enter Player's name. ").capitalize()
player_one = BJ_Player(name)
player_one_bal = BJ_Account(name, 1000)
player_two = BJ_Player("House")

new_deck = BJ_Deck()
new_deck.shuffle()

game_on = True

adj_ace = 0

round_num = 0
while game_on or len(new_deck.all_cards) != 0:
    round_num += 1
    adj_ace = 0
    print(f"Round {round_num}.")
    print(player_one_bal)
    player_bet = bet()
    print(f"{player_one.name} is betting ${player_bet}.")
    player_one_bal.withdraw(player_bet)
    player_one.add_cards(new_deck.deal_one())
    print(f"House deals {player_one.all_cards[-1]}")
    if player_one.all_cards[-1].rank == "Ace" and ace_value() == 1:
        adj_ace = 10
    print(f"{player_one.name}'s sum amount is {player_one.sum_value()-adj_ace}.")

    while (player_one.sum_value() - adj_ace) < 22 or len(new_deck.all_cards) != 0:
        pl2 = "No"
        if deal() == "Yes":
            player_one.add_cards(new_deck.deal_one())
            print(f"House deals {player_one.all_cards[-1]}")
            if player_one.all_cards[-1].rank == "Ace" and ace_value() == 1:
                adj_ace = 10
            print(
                f"{player_one.name}'s sum amount is {player_one.sum_value()-adj_ace}."
            )
            if (player_one.sum_value() - adj_ace) > 21:
                print(f"{player_one.name} you lost!")
                print(player_one_bal)
                if player_one_bal.balance > 0 and keep_playing() == "Yes":
                    player_one.clear_hand()
                    break
                else:
                    print("Game over.")
                    player_one.clear_hand()
                    print(player_one_bal)
                    game_on = False
                    break
            elif (player_one.sum_value() - adj_ace) == 21:
                print(f"{player_one.name} you won!")
                player_one_bal.deposit((player_bet * 2))
                print(player_one_bal)
                if keep_playing() == "Yes":
                    player_one.clear_hand()
                    break
        else:
            pl2 = "Yes"
            break
    if pl2 == "Yes":
        player_two.add_cards(new_deck.deal_one())
        print(f"House deals {player_two.all_cards[-1]}")
        while player_two.sum_value() < 22 or len(new_deck.all_cards) != 0:
            player_two.add_cards(new_deck.deal_one())
            print(f"House deals {player_two.all_cards[-1]}")
            print(f"{player_two.name}'s sum amount is {player_two.sum_value()}.")
            if player_two.sum_value() > 21:
                print(f"{player_one.name} you won!")
                player_one_bal.deposit((player_bet * 2))
                print(player_one_bal)
                if keep_playing() == "Yes":
                    player_two.clear_hand()
                    player_one.clear_hand()
                    break
                else:
                    print("Game over.")
                    player_two.clear_hand()
                    player_one.clear_hand()
                    print(player_one_bal)
                    game_on = False
                    break
            elif player_two.sum_value() == 21:
                print(f"{player_two.name} wins!")
                print(player_one_bal)
                if keep_playing() == "Yes":
                    player_two.clear_hand()
                    player_one.clear_hand()
                    break
                else:
                    print("Game over.")
                    player_two.clear_hand()
                    player_one.clear_hand()
                    print(player_one_bal)
                    game_on = False
                    break
            elif len(player_two.all_cards) == 3:
                if player_two.sum_value() > (player_one.sum_value() - adj_ace):
                    print(f"{player_two.name} wins!")
                    print(player_one_bal)
                    if keep_playing() == "Yes":
                        player_two.clear_hand()
                        player_one.clear_hand()
                        break
                    else:
                        print("Game over.")
                        player_two.clear_hand()
                        player_one.clear_hand()
                        print(player_one_bal)
                        game_on = False
                        break
                else:
                    print(f"{player_one.name} you won!")
                    player_one_bal.deposit((player_bet * 2))
                    print(player_one_bal)
                    if keep_playing() == "Yes":
                        player_two.clear_hand()
                        player_one.clear_hand()
                        break
                    else:
                        print("Game over.")
                        player_two.clear_hand()
                        player_one.clear_hand()
                        print(player_one_bal)
                        game_on = False
                        break
