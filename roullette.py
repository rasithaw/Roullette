'''
Double Or Nothing Strategy for Roullette 
'''
from random import seed
from random import randint

StartingBet = 1
StartingPot = 100
NumOfTries = 100
Pot = StartingPot
Bet = StartingBet
Round = 0
RoulletteNum = 0
BettedNumbers = [2,4,6,8,10,12,16,18,20,22,24,26,28,30,32,34,36]

for _ in range(NumOfTries):
    RoulletteNum = randint(0, 36)
    Round = Round + 1
    if Pot>0 and Pot <StartingPot*1.2:
        if RoulletteNum in BettedNumbers:
            Pot = Pot + Bet 
            print ('You win = ' + str(Bet))
            Bet = StartingBet
        Pot = Pot - Bet
        print ('You lost =' + str(Bet))
        Bet = Bet * 2
    elif Pot >= StartingPot*1.2:
        print('enough for today')
        break
    else:
        print('you lost everything')
        break
    
print('final winnings = ' + str(Pot - StartingPot) + ' in round = ' + str(Round))