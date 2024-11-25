playerListBlueTeam = [0, 1, 2, 7]
playerListRedTeam = [3, 4, 5, 6]

numRedDeadTeam = 0
numBlueDeadTeam = 0
playerDeadList = []

for player in playerListBlueTeam:
    playerDeadList.append(player)

for player in playerListRedTeam:
    playerDeadList.append(player)

for player in playerListRedTeam:
    if playerDeadList[players] == playerListRedTeam[players]:
        numRedDeadTeam += 1
        if len(playerListRedTeam) >= numRedDeadTeam:
            print("You Lose Red Team")

for players in playerListBlueTeam:   
    if playerDeadList[players] == playerListBlueTeam[players]:
        numBlueDeadTeam += 1
        if len(playerListBlueTeam) >= numBlueDeadTeam:
            print("You Lose Blue Team")

for player in playerDeadList:
    for players in playerListBlueTeam:
        print("Blue Team")
    for players in playerListRedTeam:
        print("Red Team")
