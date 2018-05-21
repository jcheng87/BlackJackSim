from random import shuffle

SUITS = "Diamond Clubs Heart Spade".split()
RANKS = "2 3 4 5 6 7 8 9 10 J Q K A".split()
FACE_CARDS = "10 J Q K".split()


class Deck:
    # create deck
    def __init__(self):
        self.new_deck = [(suit, rank) for suit in SUITS for rank in RANKS]

    # shuffle new_deck
    def shuffle(self):
        shuffle(self.new_deck)
        print(self.new_deck)

    # remove card from deck
    def remove_card(self):
        return self.new_deck.pop()


class Hand:
    # create Hand
    def __init__(self):
        self.hand = []
        self.count = [0, None]  # [mainCount/ altCount]
        self.bust = False

    # draw card to hand
    def draw(self, deck):
        card = deck.remove_card()
        print(card)
        self.hand.append(card)
        rank = card[1]
        main_count, alt_count = self.count

        # when only main count
        if alt_count == None:
            if rank == 'A':
                alt_count = main_count + 11
                main_count += 1
            elif rank in FACE_CARDS:
                main_count += 10
            else:
                main_count += int(rank)

        # when two counts
        else:
            if rank == 'A':
                main_count += 1
                alt_count += 1
            elif rank in FACE_CARDS:
                main_count += 10
                alt_count += 10
            else:
                main_count += int(rank)
                alt_count += int(rank)

        self.count = [main_count, alt_count]

        print('count:', self.count)

        # if main_count > 21 and (alt_count == None or alt_count > 21):
        #   print('BUST')
        #   print(self.count)
        #   self.bust = True
        # elif main_count == 21 or alt_count == 21:
        #   print('21!')
        #   print(self.count)
        # else:
        #   print(self.count)


class Player():

    # create Player
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand


def deal(deck):
    dealer.hand.draw(deck)
    player.hand.draw(deck)
    dealer.hand.draw(deck)
    player.hand.draw(deck)


def choices(self):
    choice = input('1. Hit\n2. Stand\n3. Split')

    if choice == 1:
        pass
    elif choice == 2:
        pass
    elif choice == 3:
        pass
    else:
        print('invalid choice')


# created & shuffles deck
deck_1 = Deck()
deck_1.shuffle()

# created dealer & player
dealer = Player('Dealer', Hand())
playerName = input("Enter Player's Name: ")
player = Player(playerName, Hand())

# deal deck
deal(deck_1)

#


# print(hand.count)
# hand.draw(deck_1.remove_card())
# print(hand.count)
# hand.draw(deck_1.remove_card())
# print(hand.count)
# hand.draw(deck_1.remove_card())