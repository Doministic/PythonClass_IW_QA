playerId = 0
playerTeamRed = []
playerTeamBlue = []


while True:
    print(f"Blue player Team size: %d", len(playerTeamBlue))
    print(f"Red player Team size: %d", len(playerTeamRed))
    
    if playerId % 2 == 0:
        playerTeamBlue.append(playerId)
        playerId += 3
    else:
        playerTeamRed.append(playerId)
        playerId += 1

    if len(playerTeamBlue) >= 4 and len(playerTeamRed) >= 4:
        print(f"Blue player Team size: %d", len(playerTeamBlue))
        print(f"Red player Team size: %d", len(playerTeamRed))
        break


