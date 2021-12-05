import random

# A match is when one player attacks one other player.
# A round is when each player (if still alive) gets one attempt to attack another.
# A game is every time one player is left alive.

## Getting the number of games a user wants to run.
num_games_desired = int(input("How many games do you want to run? This must be an integer.\n"))

## game level
## At the begining of every game, each player is still alive.
al_alive = True
ben_alive = True
charlie_alive = True

## Each player has a different likelihood of success. This doesn't change from game to game.
al_attack_ability = .8
ben_attack_ability = .6
charlie_attack_ability = .4

## This is the number of games each player has won.
al_won = 0
ben_won = 0
charlie_won = 0
num_games_ran = 0


attack_first = ''
attack_second = ''
attack_third = ''
match = 0
round = 0

## Attack order
def attack_order():
    global attack_first, attack_second, attack_third

    attack_order = []

    ## Should be a more efficient way of doing this.
    ## This creates an array of 1, 2, and 3 placed in a random order.
    while len(attack_order) < 3:
        r = random.randint(1,3)
        if r not in attack_order: attack_order.append(r)

    # print(attack_order)

    if attack_order[0] == 1:
        attack_first = 'al'
    elif attack_order[0] == 2:
        attack_first = 'ben'
    else:
        attack_first = 'charlie'

    if attack_order[1] == 1:
        attack_second = 'al'
    elif attack_order[1] == 2:
        attack_second = 'ben'
    else:
        attack_second = 'charlie'

    if attack_order[2] == 1:
        attack_third = 'al'
    elif attack_order[2] == 2:
        attack_third = 'ben'
    else:
        attack_third = 'charlie'

## Matches
def match_1(): # First Match of this Round
    global al_alive, ben_alive, charlie_alive
    global num_games_ran, round, match

    if attack_first == 'al' and al_alive == True:
        if ben_alive == True:
            if random.uniform(0, 1) < al_attack_ability:
                ben_alive = False

        elif charlie_alive == True:
            if random.uniform(0, 1) < al_attack_ability:
                charlie_alive = False

    if attack_first == 'ben' and ben_alive == True:
        if al_alive == True:
            if random.uniform(0, 1) < ben_attack_ability:
                al_alive = False

        elif charlie_alive == True:
            if random.uniform(0, 1) < ben_attack_ability:
                charlie_alive = False

    if attack_first == 'charlie' and charlie_alive == True:
        if al_alive == True:
            if random.uniform(0, 1) < charlie_attack_ability:
                al_alive = False

        elif ben_alive == True:
            if random.uniform(0, 1) < charlie_attack_ability:
                ben_alive = False

    print("This is game {}, round {} match {}".format(num_games_ran, round, match))
    print("Al is alive: {}   Ben is alive: {}   Charlie is alive: {}".format(al_alive, ben_alive, charlie_alive))

    return()

def match_2():  # Second match of this round
    global al_alive, ben_alive, charlie_alive
    global num_games_ran, round, match

    if attack_second == 'al' and al_alive == True:
        if ben_alive == True:

            if random.uniform(0, 1) < al_attack_ability:
                ben_alive = False

        elif charlie_alive == True:

            if random.uniform(0, 1) < al_attack_ability:
                charlie_alive = False

    if attack_second == 'ben' and ben_alive == True:
        if al_alive == True:

            if random.uniform(0, 1) < ben_attack_ability:
                al_alive = False

        elif charlie_alive == True:

            if random.uniform(0, 1) < ben_attack_ability:
                charlie_alive = False

    if attack_second == 'charlie' and charlie_alive == True:
        if al_alive == True:

            if random.uniform(0, 1) < charlie_attack_ability:
                al_alive = False

        elif ben_alive == True:

            if random.uniform(0, 1) < charlie_attack_ability:
                ben_alive = False

    print("This is game {}, round {} match {}".format(num_games_ran, round, match))
    print("Al is alive: {}   Ben is alive: {}   Charlie is alive: {}".format(al_alive, ben_alive, charlie_alive))

    return()

def match_3():  # Third match of this round
    global al_alive, ben_alive, charlie_alive
    global num_games_ran, round, match

    if attack_third == 'al' and al_alive == True:
        if ben_alive == True:

            if random.uniform(0, 1) < al_attack_ability:
                ben_alive = False

        elif charlie_alive == True:

            if random.uniform(0, 1) < al_attack_ability:
                charlie_alive = False

    if attack_third == 'ben' and ben_alive == True:
        if al_alive == True:

            if random.uniform(0, 1) < ben_attack_ability:
                al_alive = False

        elif charlie_alive == True:

            if random.uniform(0, 1) < ben_attack_ability:
                charlie_alive = False

    if attack_third == 'charlie' and charlie_alive == True:
        if al_alive == True:

            if random.uniform(0, 1) < charlie_attack_ability:
                al_alive = False

        elif ben_alive == True:

            if random.uniform(0, 1) < charlie_attack_ability:
                ben_alive = False

    print("This is game {}, round {} match {}".format(num_games_ran, round, match))
    print("Al is alive: {}   Ben is alive: {}   Charlie is alive: {}".format(al_alive, ben_alive, charlie_alive))

    return()


def run_game():
    global num_games_ran, al_won, ben_won, charlie_won
    global al_alive, ben_alive, charlie_alive, match, round
    global attack_first, attack_second, attack_third

    while al_alive + ben_alive + charlie_alive > 1:
        attack_order()
        match = 0
        match_1()
        match = 1
        match_2()
        match = 2
        match_3()
        round += 1

    if al_alive == True:
        al_won += 1
    elif ben_alive == True:
        ben_won += 1
    elif charlie_alive == True:
        charlie_won += 1

    num_games_ran += 1
    al_alive = True
    ben_alive = True
    charlie_alive = True
    match = 0
    round = 0
    attack_first = ''
    attack_second = ''
    attack_third = ''

    print ()

    return()


while num_games_ran < num_games_desired:
    run_game()

print("For {} games ran, Al won {} times. Ben won {} times, and Charlie won {} times.".format(num_games_ran, al_won, ben_won, charlie_won))
print(num_games_ran)
print(al_won)
print(ben_won)
print(charlie_won)