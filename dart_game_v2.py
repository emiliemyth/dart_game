import random

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
attack_order = []
match = 0
round = 0


## Attack order
def determine_attack_order():
    global attack_order

    attack_order = []

    ## This creates a list of 0, 1, and 2 placed in a random order.
    while len(attack_order) < 3:
        r = random.randint(0,2)
        if r not in attack_order: attack_order.append(r)

    # print(attack_order)

## Matches
def match_1(): # First Match of this Round
    global al_alive, ben_alive, charlie_alive, match
    global attack_order

    if attack_order[0] == 0 and al_alive == True:
        if ben_alive == True:
            match += 1
            if random.uniform(0, 1) < al_attack_ability:
                ben_alive = False

        elif charlie_alive == True:
            match += 1
            if random.uniform(0, 1) < al_attack_ability:
                charlie_alive = False

    if attack_order[0] == 1 and ben_alive == True:
        if al_alive == True:
            match += 1
            if random.uniform(0, 1) < ben_attack_ability:
                al_alive = False

        elif charlie_alive == True:
            match += 1
            if random.uniform(0, 1) < ben_attack_ability:
                charlie_alive = False

    if attack_order[0] == 2 and charlie_alive == True:
        if al_alive == True:
            match += 1
            if random.uniform(0, 1) < charlie_attack_ability:
                al_alive = False

        elif ben_alive == True:
            match += 1
            if random.uniform(0, 1) < charlie_attack_ability:
                ben_alive = False

    return()

def match_2():  # Second match of this round
    global al_alive, ben_alive, charlie_alive, match
    global attack_order

    if attack_order[1] == 0 and al_alive == True:
        if ben_alive == True:
            match += 1

            if random.uniform(0, 1) < al_attack_ability:
                ben_alive = False

        elif charlie_alive == True:
            match += 1

            if random.uniform(0, 1) < al_attack_ability:
                charlie_alive = False

    if attack_order[1] == 1 and ben_alive == True:
        if al_alive == True:
            match += 1

            if random.uniform(0, 1) < ben_attack_ability:
                al_alive = False

        elif charlie_alive == True:
            match += 1

            if random.uniform(0, 1) < ben_attack_ability:
                charlie_alive = False

    if attack_order[1] == 2 and charlie_alive == True:
        if al_alive == True:
            match += 1

            if random.uniform(0, 1) < charlie_attack_ability:
                al_alive = False

        elif ben_alive == True:
            match += 1

            if random.uniform(0, 1) < charlie_attack_ability:
                ben_alive = False

    return()

def match_3():  # Third match of this round
    global al_alive, ben_alive, charlie_alive, match
    global attack_order

    if attack_order[2] == 0 and al_alive == True:
        if ben_alive == True:
            match += 1

            if random.uniform(0, 1) < al_attack_ability:
                ben_alive = False

        elif charlie_alive == True:
            match += 1

            if random.uniform(0, 1) < al_attack_ability:
                charlie_alive = False

    if attack_order[2] == 1 and ben_alive == True:
        if al_alive == True:
            match += 1

            if random.uniform(0, 1) < ben_attack_ability:
                al_alive = False

        elif charlie_alive == True:
            match += 1

            if random.uniform(0, 1) < ben_attack_ability:
                charlie_alive = False

    if attack_order[2] == 2 and charlie_alive == True:
        if al_alive == True:
            match += 1

            if random.uniform(0, 1) < charlie_attack_ability:
                al_alive = False

        elif ben_alive == True:
            match += 1

            if random.uniform(0, 1) < charlie_attack_ability:
                ben_alive = False

    return()

def round_score():
    global round
    round += 1


def run_game():
    global num_games_ran, al_won, ben_won, charlie_won
    global al_alive, ben_alive, charlie_alive, match, round
    global attack_first, attack_second, attack_third

    determine_attack_order()

    while al_alive + ben_alive + charlie_alive > 1:
        match_1()
        match_2()
        match_3()
        round_score()

    if al_alive == True:
        al_won += 1
    if ben_alive == True:
        ben_won += 1
    if charlie_alive == True:
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

while num_games_ran < num_games_desired:
    run_game()

print("For {} games ran, Al won {} times. Ben won {} times, and Charlie won {} times.".format(num_games_ran, al_won, ben_won, charlie_won))
print(f"Al won {100 * al_won / num_games_ran}% of the time,")
print(f"Ben won {100 * ben_won / num_games_ran}% of the time,")
print(f"and Charlie won {100 * charlie_won / num_games_ran}% of the time,")
