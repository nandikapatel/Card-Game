app.background = 'beige'

playerPile = Group()
computerPile = Group()

screen = Group()
continueButton = Group()
screen.toFront()
continueButton.toFront()

playerCards = []
computerCards = []

#score needed to win the game 
winningScore = 10

#create a list for ranks and a list for suits
ranks = ['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
suits = ['Spades', 'Hearts', 'Diamonds', 'Clubs']

#states the winner of the round
roundWinner = Label(' ', 120, 35, fill='black', size=22, font='caveat',bold=True)

#rules on how to play/win the game
def howToPlay():
    screen.add(
        Rect(0,0,400,400,fill = 'lavender'),
        Label("WAR", 200,50, size = 40, font = 'cinzel', bold = True),
        Label("How To Play:",75,110, size = 20, font = 'montserrat', bold = True, italic = True),
        Label("In this game of War, you must click on", 200,140,size = 18, font = 'montserrat'),
        Label("your pile of cards (the one on the right) to", 200,160,size = 18, font = 'montserrat'),
        Label("draw a card from the top of the pile and", 200,180,size = 18, font = 'montserrat'),
        Label("onto the table. Your card is then ", 200,200,size = 18, font = 'montserrat'),
        Label("comprared to the computer's card, (with", 200,220,size = 18, font = 'montserrat'),
        Label("Ace being the smallest value, and King the", 200,240,size = 18, font = 'montserrat'),
        Label("largest value). Whoever has the greater", 200,260,size = 18, font = 'montserrat'),
        Label("card value, will win a point.", 200,280,size = 18, font = 'montserrat'),
        Label("The first one to 10 points, wins the game!", 200,300,size = 18, font = 'montserrat')
        )
    continueButton.add(
        Rect(50,320,300,60, fill = "darkSlateBlue", border = 'white'),
        Label("PLAY", 200,350, size = 40, fill = 'white', font = 'montserrat', bold = True )
        )
howToPlay()

#draw the table
def createTable():
    table = Rect(0, 250, 400, 150, fill='sienna')
    table.toBack()
createTable()

#draw the computer player
def createComputer():
    computer = Group(
        Circle(200,130,70),
        Rect(130,137,140,100),
        Polygon(120, 250, 155, 200, 245, 200, 280, 250, fill='red'),
        Rect(185,160,30,40, fill = 'tan'),
        Circle(200,130,50, fill = 'tan'),
        Oval(220,120,20,25, fill = 'white'),
        Oval(180,120,20,25, fill = 'white'),
        Circle(220, 120, 5, fill=rgb(60, 60, 60)),
        Circle(180, 120, 5, fill=rgb(60, 60, 60)),
        Oval(200, 150, 50, 30),
        Oval(200, 150, 40, 20, fill = 'tan'),
        Rect(175,135,50,15, fill = 'tan'),
        Polygon(196, 130, 204, 130, 207, 145, 193, 145, fill=rgb(160, 140, 110)),
        Arc(200, 200, 30, 30, 90, 180, fill = 'tan')
        )
    computer.toBack()
createComputer()

#make scoreBoard to keep score
def makeScoreboard():
    scoreboard = Group(
        Line(255,45,395,45),
        Line(255,25,395,25),
        Line(325,25,325,80),
        Label('Score', 325,15, size = 16),
        Label('Computer',290,35)
        )
    scoreboard.toBack()
makeScoreboard()

#allow the player to input their name
playerName = app.getTextInput("Enter Your Name")
playerNameLabel = Label(playerName,360,35 )
playerNameLabel.toBack()

#collect and display the scores
computerScore = Label(0,290,60, size = 18)
computerScore.toBack()
playerScore = Label(0,360,60, size = 18)
playerScore.toBack()

#draw the card that the player flipped over (player's' card is on the right)
playerDrawnCard = Group(
    Polygon(210, 300, 270, 300, 275, 350, 215, 350, fill='white'),
    )
playerDrawnCard.visible = False

playerRankLabel = Label(0, 240, 315)
playerRankLabel.visible = False

playerSuitLabel = Label(0, 245, 335)
playerSuitLabel.visible = False
    
#draw the card that the computer flipped over (computer's' card is on the left)
computerDrawnCard = Group(
    Polygon(130, 300, 190, 300, 195, 350, 135, 350, fill='white'),
    )
computerDrawnCard.visible = False

computerRankLabel = Label(0, 160, 315)
computerRankLabel.visible = False

computerSuitLabel = Label(0, 165, 335)
computerSuitLabel.visible = False

#draws out each 'pile of cards' on the right of the player and computer
def makePileOfCards():
    playerPile.add(
        Rect(330, 350, 40, 10, fill='white'),
        Polygon(325, 320, 365, 320, 370, 350, 330, 350, fill='black'),
        Polygon(325, 320, 330, 350, 330, 360, 325,330, fill = 'white'),
        # Star(345, 335, 10, 5, fill = 'gold')
        Line(330,352,370,352, lineWidth = 0.3),
        Line(330,356,370,356, lineWidth = 0.3)
        )
    
    computerPile.add(
        Rect(70, 290, 40, 10, fill='white'),
        Polygon(65, 260, 105, 260, 110, 290, 70, 290, fill='black'),
        Polygon(65, 260, 70, 290, 70, 300, 65, 270, fill = 'white'),
        # Star(345, 335, 10, 5, fill = 'gold')
        Line(70,292,110,292, lineWidth = 0.3),
        Line(70,296,110,296, lineWidth = 0.3)
        )
makePileOfCards() 

#for every suit and rank, create a group called "card" and assign custom properties to them (suit and rank) 
#and then assign the respective list to it and add the groups to the "deck" list (creates a virtual deck of cards)
def getCards():
    deck = []
    for suit in suits:
        for rank in ranks:
            card = Group()
            card.suit = suit
            card.rank = rank
            deck.append(card)
    return (deck)

#randomly assigns half of the card groups in the "deck" list to the "playerCards" list and then takes them out 
#of the deck list so that they cannot be choosen again, and then remaining half is added to the "computerCards" list
def shuffleCard():
    deck = getCards()
    for i in range (26):
        playerChooseRandom = randrange(0,len(deck))
        cardP = deck[playerChooseRandom]
        deck.pop(playerChooseRandom)
        playerCards.append(cardP)
    
    for j in range (26):
        computerChooseRandom = randrange(0,len(deck))
        cardC = deck[computerChooseRandom]
        deck.pop(computerChooseRandom)
        computerCards.append(cardC)

#since the ranks Ace, Jack, Queen, and King cannot be converted to integers in order to compared them to 
#other cards this function checks if the rank is one of those cards and then returns a number indicating its value
def convertFaceCardtoValue(rank):
    if (rank == 'Ace'):
        return ('1')
    elif (rank == 'Jack'):
        return ('11')
    elif (rank == 'Queen'):
        return ('12')
    elif (rank == 'King'):
        return ('13')
    else:
        return rank

#if the computer and player card have the same rank, the program goes to compare the cards' suits
#(spades being the greatest value and clubs being the lowest value), it returns a number from 1-4 
#depending on the suit of the card
def convertSuitToValue(suit):
    if (suit == 'Clubs'):
        return ('1')
    elif (suit == 'Diamonds'):
        return ('2')
    elif (suit == 'Hearts'):
        return ('3')
    elif (suit == 'Spades'):
        return ('4')

#compares the card values
def playGame():
    #takes out a card group from the playerCards list, so that cards do not repeat
    cardPlayedPlayer = playerCards.pop()
    playerDrawnCard.visible = True
    
    #draws a randomly chosen card onto the player's card
    playerRankLabel.value = cardPlayedPlayer.rank
    playerRankLabel.visible = True 
    playerSuitLabel.value = cardPlayedPlayer.suit
    playerSuitLabel.visible = True 
    
    #takes out a card group from the computerCards list, so that cards do not repeat
    cardPlayedComputer = computerCards.pop()
    computerDrawnCard.visible = True
    
    #draws a randomly chosen card onto the computer's card
    computerRankLabel.value = cardPlayedComputer.rank
    computerRankLabel.visible = True 
    computerSuitLabel.value = cardPlayedComputer.suit
    computerSuitLabel.visible = True
    
    #calls the function to change the card's rank value to a 
    #string that is convertable to an integer of not already
    cardPlayedPlayer.rank = convertFaceCardtoValue(cardPlayedPlayer.rank)
    cardPlayedComputer.rank = convertFaceCardtoValue(cardPlayedComputer.rank)
    
    #calls the function to change the card's suit value to a 
    #string that is convertable to an integer 
    #this is for when the ranks are the same value
    cardPlayedPlayer.suit = convertSuitToValue(cardPlayedPlayer.suit)
    cardPlayedComputer.suit = convertSuitToValue(cardPlayedComputer.suit)
    
    #turns the ranks of the drawed cards into integers and compares them
    if (int(cardPlayedPlayer.rank) > int(cardPlayedComputer.rank)):
        playerScore.value += 1
        #annouces the winner of the round
        roundWinner.value = str(playerName) + ' won this round! :)'
    
    elif (int(cardPlayedPlayer.rank) < int(cardPlayedComputer.rank)):
        computerScore.value += 1
        roundWinner.value = 'The computer won this round :('    
    
    #for the same rank:
    else:
        if (int(cardPlayedPlayer.suit) > int(cardPlayedComputer.suit)):
            playerScore.value += 1
            roundWinner.value = str(playerName) + ' won this round! :)'
        else:
            computerScore.value += 1
            roundWinner.value = 'The computer won this round :('

#checks whether the computer's score or the player's score is equal to 10 and if it is, then it 
#displays a banner announcing if the player won or lost and then stops the game 
def checkWinner():
    if (playerScore.value == winningScore):
        roundWinner.visible = False
        Rect(0, 180, 400, 100, fill = gradient('paleGreen', 'mediumAquamarine'))
        Label('YOU WIN!', 200, 230, fill='white', size=50, font='caveat', bold=True)
        app.stop()
    
    elif (computerScore.value == winningScore):
        roundWinner.visible = False
        Rect(0, 180, 400, 100, fill = gradient('maroon', 'crimson'))
        Label('YOU LOSE!', 200, 230, fill='white', size=50, font='caveat', bold=True)
        app.stop()
    
def onMousePress(mouseX,mouseY):
    #checks if the mouse hits the play button at the beginning of the same, if yes, it makes then invisible
    hitContinueButton = continueButton .hitTest(mouseX,mouseY)
    if (hitContinueButton != None):
        continueButton .visible = False
        screen.visible = False
    shuffleCard()
    #checks if the mouse hits the player's pile of cards to 'draw a card', if yes, it places both the computer's
    #and the player's cards face up on the table
    hitPlayerCardPile = playerPile.hitTest(mouseX,mouseY)
    if (hitPlayerCardPile != None):
        playGame()
        checkWinner()
