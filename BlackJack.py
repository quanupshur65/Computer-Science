def draw_card(hand, deck):
   
    def calculate_score(hand)
        score = 0
        aces = 0
        
        for card in hand:
            if card is ["J", "Q", "K"]:
                score += 10
            elif card == "A": 
                score += 11
                aces += 1
            else:
                score += int(card)

        while score > 21 and aces > 0:
            score -=10
            aces -=1
        return score
    
def print_status(player_hand, dealer_hand, show_dealer_card=True):
    print("/nPlayer hand:", player_hand)
    print("Player score:", calculate_score(player_hand))

    if show_dealer_card:
        print("Dealer hand:", dealer_hand)
        print("Dealer score:", calculate_score(dealer_hand))
    else:
        print("dealer shows:", dealer_hand[0])
        
def main():
    deck = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    player_hand = []
    dealer_hand = []
    random.shuffle(deck)

    draw_card(dealer_hand, deck)
    draw_card(player_hand, deck)
    draw_card(player_hand, deck)

while True:
    print_status(player_hand, dealer_hand, False)

    if calculate_score(player_hand) > 21:
        print("/nYou busted! Dealer wins.")
        return
    
    choice = input("/nHit or stay? (h/s): ").lower()

    if choice == "h":
        draw_card(player_hand, deck)
    elif choice == "S":
        break
    else:
        print("Please enter 'h' or 's' .")

while calculate_score(dealer_hand) < 17:
    draw_card(dealer_hand, deck)
print_status(player_hand, dealer_hand, True)
player_score = calculate_score(player_hand)
dealer_score = calculate_score(dealer_hand)

if dealer_score > 21:
    print("/nDealer busted! You win!")
elif dealer_score > player_score:
    print("/Dealer wins.")
elif dealer_score < player_score:
    print("/nYou win!")
else:
    print("/nIt's a tie!")
if_name_ == "_main_":
    main()