'''
Martingale Strategy for Roullette 
This simulates the probable outcomes when changing your bet/pot

'''
from random import seed
from random import randint
#inputs
StartingBet = 1
StartingPot = 1000
NumOfTries = 100
EvenBetNumbers = [2,4,6,8,10,12,16,18,20,22,24,26,28,30,32,34,36]
WinningCap = 100

def MartingaleRouletteStrategySim(StartingPot,StartingBet,WinningCap,BettedNumbers,NumOfTries):
    #initializing variables
    Bet = StartingBet
    Pot = StartingPot
    WinCapRatio = (WinningCap + StartingPot)/StartingPot
    Round = 0
    RoulletteNum = 0
    
    for _ in range(NumOfTries):
        RoulletteNum = randint(0, 36)
        Round = Round + 1
        if Pot>0 and Pot <StartingPot*WinCapRatio:
            if RoulletteNum in BettedNumbers:
                Pot = Pot + Bet 
                print ('You win = ' + str(Bet))
                Bet = StartingBet
            Pot = Pot - Bet
            print ('You lost =' + str(Bet))
            Bet = Bet * 2
        elif Pot >= StartingPot*WinCapRatio:
            print('enough for today')
            break
        else:
            print('you lost everything')
            break
    FinalWin = Pot - StartingPot
    return [FinalWin,Round]

Result = MartingaleRouletteStrategySim(StartingPot,StartingBet,WinningCap,EvenBetNumbers,NumOfTries)
print('You won $' + str(Result[0])+ ' in ' + str(Result[1]) + ' Rounds')
