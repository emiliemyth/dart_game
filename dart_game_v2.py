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

## Each player has a preference to attacking someone
al_attack_first  = 'ben'
al_attack_second = 'charlie'

ben_attack_first  = 'al'
ben_attack_second = 'charlie'

charlie_attack_first  = 'al'
charlie_attack_second = 'ben'

## The number of games each player has won.
al_won = 0
ben_won = 0
charlie_won = 0
num_games_ran = 0

match = 0
round = 0

attack_first = ''
attack_second = ''
attack_third = ''

## Building strategy dictionary
strategy_dictionary = {
    "first_match_player_offense":        "",
    "first_match_player_first_defense":  "",
    "first_match_player_second_defense": "",

    "second_match_player_offense":        "",
    "second_match_player_first_defense":  "",
    "second_match_player_second_defense": "",

    "third_match_player_offense":        "",
    "third_match_player_first_defense":  "",
    "third_match_player_second_defense": ""
}

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

strategy_dictionary["first_match_player_offense"] = attack_first

if strategy_dictionary["first_match_player_offense"] == 'al':
    strategy_dictionary["first_match_player_first_defense"] = al_attack_first
    strategy_dictionary["first_match_player_second_defense"] = al_attack_second

elif strategy_dictionary["first_match_player_offense"] == 'ben':
    strategy_dictionary["first_match_player_first_defense"] = ben_attack_first
    strategy_dictionary["first_match_player_second_defense"] = ben_attack_second

elif strategy_dictionary["first_match_player_offense"] == 'charlie':
    strategy_dictionary["first_match_player_first_defense"] = charlie_attack_first
    strategy_dictionary["first_match_player_second_defense"] = charlie_attack_second


strategy_dictionary["second_match_player_offense"] = attack_second

if strategy_dictionary["second_match_player_offense"] == 'al':
    strategy_dictionary["second_match_player_first_defense"] = al_attack_first
    strategy_dictionary["second_match_player_second_defense"] = al_attack_second

elif strategy_dictionary["second_match_player_offense"] == 'ben':
    strategy_dictionary["second_match_player_first_defense"] = ben_attack_first
    strategy_dictionary["second_match_player_second_defense"] = ben_attack_second

elif strategy_dictionary["second_match_player_offense"] == 'charlie':
    strategy_dictionary["second_match_player_first_defense"] = charlie_attack_first
    strategy_dictionary["second_match_player_second_defense"] = charlie_attack_second


strategy_dictionary["third_match_player_offense"]  = attack_third

if strategy_dictionary["third_match_player_offense"] == 'al':
    strategy_dictionary["third_match_player_first_defense"] = al_attack_first
    strategy_dictionary["third_match_player_second_defense"] = al_attack_second

elif strategy_dictionary["third_match_player_offense"] == 'ben':
    strategy_dictionary["third_match_player_first_defense"] = ben_attack_first
    strategy_dictionary["third_match_player_second_defense"] = ben_attack_second

elif strategy_dictionary["third_match_player_offense"] == 'charlie':
    strategy_dictionary["third_match_player_first_defense"] = charlie_attack_first
    strategy_dictionary["third_match_player_second_defense"] = charlie_attack_second


## Matches
def match_(): # First Match of this Round
    global al_alive, ben_alive, charlie_alive, match
    global attack_first, attack_second, attack_third


    if match == 0:
        attack_first


    attack_first == 'al' and al_alive == True:
        if ben_alive == True:
            match += 1
            if random.uniform(0, 1) < al_attack_ability:
                ben_alive = False

        elif charlie_alive == True:
            match += 1
            if random.uniform(0, 1) < al_attack_ability:
                charlie_alive = False

    if attack_first == 'ben' and ben_alive == True:
        if al_alive == True:
            match += 1
            if random.uniform(0, 1) < ben_attack_ability:
                al_alive = False

        elif charlie_alive == True:
            match += 1
            if random.uniform(0, 1) < ben_attack_ability:
                charlie_alive = False

    if attack_first == 'charlie' and charlie_alive == True:
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

    attack_order()

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
print(num_games_ran)
print(al_won)
print(ben_won)
print(charlie_won)