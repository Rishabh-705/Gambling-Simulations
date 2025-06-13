# roulette_simulation.py
# Performing Monte Carlo simulation on roulette game

import statistics 
import random

class FairRoulette():
    
    def __init__(self):
        # Creating list of number pockets
        self.pockets = [i for i in range(1, 37)]
        self.ball = None
        self.pocketOdds = len(self.pockets) - 1 
        
    def spin(self):
        self.ball = random.choice(self.pockets)
    
    def betPocket(self, pocket, amt):
        if str(pocket) == str(self.ball):
            return amt * self.pocketOdds
        else:
            return -amt
    
    def __str__(self):
        return 'Fair Roulette'
    
class EuRoulette(FairRoulette):
    def __init__(self):
        super().__init__()
        self.pockets.append('0')
        
class AmRoulette(EuRoulette):
    def __init__(self):
        super().__init__()
        self.pockets.append('00')
    
def playRoulette(game, numSpins, pocket, bet):
    totalPocket = 0
    for _ in range(numSpins):
        game.spin()
        totalPocket += game.betPocket(pocket, bet)
    return totalPocket / numSpins
    
def main():
    fgame = FairRoulette()
    fairList1 = []
    fairList2 = []
    for numSpins in (1000, 1000000):
        for _ in range(20):
            if numSpins == 1000:
                fairList1.append(playRoulette(fgame, numSpins, 2, 1))
            else:
                fairList2.append(playRoulette(fgame, numSpins, 2, 1))

    eugame = EuRoulette()
    EuList1 = []
    EuList2 = []
    for numSpins in (1000, 1000000):
        for _ in range(20):
            if numSpins == 1000:
                EuList1.append(playRoulette(eugame, numSpins, 2, 1))
            else:
                EuList2.append(playRoulette(eugame, numSpins, 2, 1))

    amgame = AmRoulette()
    AmList1 = []
    AmList2 = []
    for numSpins in (1000, 1000000):
        for _ in range(20):
            if numSpins == 1000:
                AmList1.append(playRoulette(amgame, numSpins, 2, 1))
            else:
                AmList2.append(playRoulette(amgame, numSpins, 2, 1))

    print("Simulate 20 trials of 1000 spins each")
    print(f"Exp. return for fair Roulette = {statistics.mean(fairList1)}")
    print(f"Exp. return for european Roulette = {statistics.mean(EuList1)}")
    print(f"Exp. return for american Roulette = {statistics.mean(AmList1)}\n")

    print("Simulate 20 trials of 1000000 spins each")
    print(f"Exp. return for fair Roulette = {statistics.mean(fairList2)}")
    print(f"Exp. return for european Roulette = {statistics.mean(EuList2)}")
    print(f"Exp. return for american Roulette = {statistics.mean(AmList2)}")

if __name__ == "__main__":
    main()
