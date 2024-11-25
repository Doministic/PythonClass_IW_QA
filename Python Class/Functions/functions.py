
health = 150
def playerHealth(damage, healing):
    player_health = health
    if player_health <= 150:
        player_health += healing
        print(player_health)
    elif player_health >= 150:
        player_health -= damage
        print(player_health)
    else:
        print(f"Player Health: %d", player_health)


def healingPlayer(healing):
    if player is healer:
        healing *= 1.5
    elif player is dps:
        healing *= 0.75
    else:
        healing *= 1.0
    return healing

def damagePlayer(damage):
    if player is dps:
        damage *= 1.5
    elif player is healer:
        damage *= 0.75
    else:
        damage *= 1.0
    return damage

playerHealth(damagePlayer(100), healingPlayer(150))

