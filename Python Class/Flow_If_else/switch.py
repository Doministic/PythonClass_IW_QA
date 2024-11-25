
var = 1


def switch_example(value):
    switch = {
        1: "defaut", 
        2: "Bumper Jumper", 
        3: "Tactical", 
        4: "Inverted Tactical"
    }

    print(switch.get(value, "value is not in list"))

while True:
    switch_example(var)
    var += 1
    if var > 5:
        break

