# if morning (0800 AM)
### Order food from Foodja
### Check Email
### Check Slack
### Check Resolves
# else if lunch time (1 PM) 
### Go to lunch
# else if 4 PM
### Go to QA call
# else if 11:00 AM or 4:30 PM
### Take 15 min break
# else
### Go back to work


# if player navigation path is the shortest path to take
### take that path
# else
### Calcualate the shortest path to take

health = 100
healthy = True

while health > 0:
    
    if not healthy:
        print(health)
        if health > 50:
            healthy = True
        print("I dead")

        health -= 1
    elif health <= 50:
        print("Danger Low on health")
        print("Im Dying")
        print(health)
        health = health - 10
    elif health < 100:
        print("player got shot")
        print("Show damage in UI")
        print("Player should be limping")
        print(health)
        health -= 10
    else:
        print("player at fuill health")
        print(health)
        healthy = False
        health -= 10