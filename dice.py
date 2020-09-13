from random import choices 
ntrials=15000
player1wins=0
for i in range(ntrials):
    dice2=choices(range(1,7),k=2)
    if dice2[0]==dice2[1]:
            continue
    total2=dice2[0]+dice2[1]
    dice1=choices(range(1,7),k=3)
    dice1.sort(reverse=True)
    total1=dice1[0]+dice1[1]
    if total1 > total2:
            player1wins+=1
print("Ratio of Player 1 winning", player1wins/ntrials)
