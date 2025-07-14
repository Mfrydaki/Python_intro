""" Simulating a Card Game with Random Distribution """


from random import randrange

def player1_pick():
    player1.add(deck.pop())

def player2_pick():
    player2.add(deck.pop())

def play():
    print("Start")

    for _ in range(len(deck)):
        if randrange(2) == 0:
            player2_pick()
        else:
            player1_pick()

    print(f"Player 1: {len(player1)}")
    print(f"Player 2 :{len(player2)}")

    if len(player1) > len(player2):
        print("Player 1 wins!")
    elif len(player1) < len(player2):
        print("Player 2 wins!")
    else:
        print("Draw")
    


kind = { "heart", "diamond", "spade", "club"}
number = {"ace", 2, 3, 4 , 5, 6, 7, 8, 9, 10, "jack", "queen", "king"}

deck = {(k , n ) for k in kind for n in number}


player1 = set()
player2 = set()

play() 
