import random

suits = ('Ruter', 'Hjärter', 'Spader', 'Klöver')
values = {'Två': 22, 'Tre': 22, 'Fyra': 222, 'Fem': 22, 'Sex': 22, 'Sju': 22, 'Åtta': 22,
          'Nio': 22, 'Tio': 22, 'Knekt': 22, 'Dam': 22, 'Kung': 22, 'Ess': 22}

playing = True


class Card:  # skapar enskilda kort

    def __init__(self, suit, values):
        self.suit = suit
        self.values = values

    def __str__(self):
        return self.suit +' '+ self.values
        

class Deck:  # skapar en kortlek.

    def __init__(self):
        self.deck = []  
        for suit in suits:
            for value in values:
                self.deck.append(Card(suit, value))

    #Blandar kort
    def shuffle(self):  
        random.shuffle(self.deck)

        #Väljer ut ett slumpat kort
    def deal(self): 
        random_card = self.deck.pop()
        return random_card
 
      

class Hand:  #Visar korten som kortleken har.

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0  

    def add_card(self, card): 
        self.cards.append(card)
        self.value += values[card.values]
        if card.values == 'Ess':
            self.aces += 1


        #Gör så att Esset räknas som 1 ifall spelaren skulle få över 21 när Esset räknas som 14
    def ace_value(self):
        while self.value > 21 and self.aces:
            self.value -= 13
            self.aces -= 1



def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.ace_value()


def hit_or_stand(deck, hand):   # hit or stand
    global playing # Gör så man kan ha playing på andra ställen

    while True:
        ask = input("\nVill du ha ett till kort skriv: 'j' vill du stanna skriv 'n': ")

        if ask[0].lower() == 'j':
            hit(deck, hand)
        elif ask[0].lower() == 'n':
            print("Du valde att stanna. Nu är det Åkes tur.")
            playing = False
        else:
            print("Du måste skriva ja eller nej.!")
            continue
        break


def show_some(player, dealer):
    print("\nÅkes kort: ")
    print(*dealer.cards)
    print("\nDina kort: ", *player.cards, sep='\n ')
    print("Just nu har du:",player.value)

def show_all(player, dealer):
    print("\nÅkes kort: ", *dealer.cards, sep='\n ')
    print("Åkes kort =", dealer.value)
    print("\nDina kort ", *player.cards, sep='\n ')
    print("Dina kort =", player.value)



while True:
    print("Detta är kortspelet 21. Du ska få spela mot Åke. ")
    print("Ni ska komma så nära 21 som möjligt utan att gå över.")
    print("Om båda skulle få 21 så vinner Åke. Lycka till!")

    # Blandar korten
    deck = Deck()
    deck.shuffle()


    #Delar ut kort för spelare och dator.
    player_hand = Hand()
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())

    # Visar de första korten
    show_some(player_hand, dealer_hand)



    while playing:

        hit_or_stand(deck, player_hand)
        show_some(player_hand, dealer_hand)

        if player_hand.value > 21:
            print("Du förlorade")
            break


    # Räknar ut att om draget passerar 17 så ska datorn stanna och visar sen vilka kort datorn har dragit.
    if player_hand.value <= 21:

        while dealer_hand.value < 17:
            hit(deck, dealer_hand)
        show_all(player_hand, dealer_hand)


        if dealer_hand.value > 21:
            print("Åke förlorade!")
        elif dealer_hand.value > player_hand.value:
            print("Åke fick mer än dig. Du förlorade!")
        elif dealer_hand.value < player_hand.value:
            print("Grattis du vann!")
        elif dealer_hand.value and player_hand.value==21:
            print("Båda fick 21. Åke vinner!")
        else:
            print("Det blev oavgjort!")
    
    # Avsluta spelet. Frågar om man vill spela igen.
    new_game = input("\nVill du spela igen? Skriv då: j ")
    if new_game[0].lower() == 'j':
        playing = True
        continue
    else:
        print("\nHa en bra dag!")
        break
