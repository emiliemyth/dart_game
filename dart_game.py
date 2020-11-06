import random


## setup

num_games_desired = int(input("How many games do you want to run? This must be an integer.\n"))

## game level

al_alive = True
ben_alive = True
charlie_alive = True

al_attack_ability = .8
ben_attack_ability = .6
charlie_attack_ability = .4

al_won = 0
ben_won = 0
charlie_won = 0

match = 0
round = 0
num_games_ran = 0

## round

attack_order = []

while len(attack_order) < 3:
    r = random.randint(1,3)
    if r not in attack_order: attack_order.append(r)

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
def match_1():
    global al_alive, ben_alive, charlie_alive, match
    if attack_first == 'al' and al_alive == True:
        if ben_alive == True:
            match += 1
            print("    In this match number {}, Al is attacking Ben.".format(match))
            if random.uniform(0, 1) < al_attack_ability:
                ben_alive = False
                print("        Al was successful at attacking Ben.")
            else: 
                print("        Al was not successful attacking Ben.")
        elif charlie_alive == True:
            match += 1
            print("    In this match number {}, Al is attacking Charlie.".format(match))
            if random.uniform(0, 1) < al_attack_ability:
                charlie_alive = False
                print("        Al was successful at attacking Charlie.")
            else: 
                print("        Al was not successful attacking Charlie.")
    if attack_first == 'ben' and ben_alive == True:
        if al_alive == True:
            match += 1
            print("    In this match number {}, Ben is attacking Al.".format(match))
            if random.uniform(0, 1) < ben_attack_ability:
                al_alive = False
                print("        Ben was successful at attacking Al.")
            else: 
                print("        Ben was not successful attacking Al.")
        elif charlie_alive == True:
            match += 1
            print("    In this match number {}, Ben is attacking Charlie.".format(match))
            if random.uniform(0, 1) < ben_attack_ability:
                charlie_alive = False
                print("        Ben was successful at attacking Charlie.")
            else: 
                print("        Ben was not successful attacking Charlie.")
    if attack_first == 'charlie' and charlie_alive == True:
        if al_alive == True:
            match += 1
            print("    In this match number {}, Charlie is attacking Al.".format(match))
            if random.uniform(0, 1) < charlie_attack_ability:
                al_alive = False
                print("        Charlie was successful at attacking Al.")
            else: 
                print("        Charlie was not successful attacking Al.")
        elif ben_alive == True:
            match += 1
            print("    In this match number {}, Charlie is attacking Ben.".format(match))
            if random.uniform(0, 1) < charlie_attack_ability:
                ben_alive = False
                print("        Charlie was successful at attacking Ben.")
            else: 
                print("        Charlie was not successful attacking Ben.")
    return()

def match_2():  # attack_second
    global al_alive, ben_alive, charlie_alive, match
    if attack_second == 'al' and al_alive == True:
        if ben_alive == True:
            match += 1
            print("    In this match number {}, Al is attacking Ben.".format(match))
            if random.uniform(0, 1) < al_attack_ability:
                ben_alive = False
                print("        Al was successful at attacking Ben.")
            else: 
                print("        Al was not successful attacking Ben.")
        elif charlie_alive == True:
            match += 1
            print("    In this match number {}, Al is attacking Charlie.".format(match))
            if random.uniform(0, 1) < al_attack_ability:
                charlie_alive = False
                print("        Al was successful at attacking Charlie.")
            else: 
                print("        Al was not successful attacking Charlie.")
    if attack_second == 'ben' and ben_alive == True:
        if al_alive == True:
            match += 1
            print("    In this match number {}, Ben is attacking Al.".format(match))
            if random.uniform(0, 1) < ben_attack_ability:
                al_alive = False
                print("        Ben was successful at attacking Al.")
            else: 
                print("        Ben was not successful attacking Al.")
        elif charlie_alive == True:
            match += 1
            print("    In this match number {}, Ben is attacking Charlie.".format(match))
            if random.uniform(0, 1) < ben_attack_ability:
                charlie_alive = False
                print("        Ben was successful at attacking Charlie.")
            else: 
                print("        Ben was not successful attacking Charlie.")
    if attack_second == 'charlie' and charlie_alive == True:
        if al_alive == True:
            match += 1
            print("    In this match number {}, Charlie is attacking Al.".format(match))
            if random.uniform(0, 1) < charlie_attack_ability:
                al_alive = False
                print("        Charlie was successful at attacking Al.")
            else: 
                print("        Charlie was not successful attacking Al.")
        elif ben_alive == True:
            match += 1
            print("    In this match number {}, Charlie is attacking Ben.".format(match))
            if random.uniform(0, 1) < charlie_attack_ability:
                ben_alive = False
                print("        Charlie was successful at attacking Ben.")
            else: 
                print("        Charlie was not successful attacking Ben.")
    return()

def match_3():  # attack_third
    global al_alive, ben_alive, charlie_alive, match
    if attack_third == 'al' and al_alive == True:
        if ben_alive == True:
            match += 1
            print("    In this match number {}, Al is attacking Ben.".format(match))
            if random.uniform(0, 1) < al_attack_ability:
                ben_alive = False
                print("        Al was successful at attacking Ben.")
            else: 
                print("        Al was not successful attacking Ben.")
        elif charlie_alive == True:
            match += 1
            print("    In this match number {}, Al is attacking Charlie.".format(match))
            if random.uniform(0, 1) < al_attack_ability:
                charlie_alive = False
                print("        Al was successful at attacking Charlie.")
            else: 
                print("        Al was not successful attacking Charlie.")
    if attack_third == 'ben' and ben_alive == True:
        if al_alive == True:
            match += 1
            print("    In this match number {}, Ben is attacking Al.".format(match))
            if random.uniform(0, 1) < ben_attack_ability:
                al_alive = False
                print("        Ben was successful at attacking Al.")
            else: 
                print("        Ben was not successful attacking Al.")
        elif charlie_alive == True:
            match += 1
            print("    In this match number {}, Ben is attacking Charlie.".format(match))
            if random.uniform(0, 1) < ben_attack_ability:
                charlie_alive = False
                print("        Ben was successful at attacking Charlie.")
            else: 
                print("        Ben was not successful attacking Charlie.")
    if attack_third == 'charlie' and charlie_alive == True:
        if al_alive == True:
            match += 1
            print("    In this match number {}, Charlie is attacking Al.".format(match))
            if random.uniform(0, 1) < charlie_attack_ability:
                al_alive = False
                print("        Charlie was successful at attacking Al.")
            else: 
                print("        Charlie was not successful attacking Al.")
        elif ben_alive == True:
            match += 1
            print("    In this match number {}, Charlie is attacking Ben.".format(match))
            if random.uniform(0, 1) < charlie_attack_ability:
                ben_alive = False
                print("        Charlie was successful at attacking Ben.")
            else: 
                print("        Charlie was not successful attacking Ben.")
    return()

def round_score():
    global round
    round += 1
    print("After round {}, here are the results:".format(round))
    if al_alive == True:
        print("Al is still alive")
    if ben_alive == True:
        print("Ben is still alive")
    if charlie_alive == True:
        print("Charlie is still alive")
    print("")

def run_game():
    global num_games_ran, al_won, ben_won, charlie_won
    global al_alive, ben_alive, charlie_alive, match, round
    while al_alive + ben_alive + charlie_alive > 1:
        print("Round {}!".format(round + 1))
        match_1()
        # print(al_alive, ben_alive, charlie_alive, match)
        match_2()
        # print(al_alive, ben_alive, charlie_alive, match)
        match_3()
        # print(al_alive, ben_alive, charlie_alive, match)
        round_score()

    if al_alive == True:
        print("Al won the game")
        al_won += 1
    if ben_alive == True:
        print("Ben won the game")
        ben_won += 1
    if charlie_alive == True:
        print("Charlie won the game")
        charlie_won += 1

    num_games_ran += 1
    al_alive = True
    ben_alive = True
    charlie_alive = True
    match = 0
    round = 0


while num_games_ran < num_games_desired:
    run_game()

print("For {} games ran, Al won {} times. Ben won {} times, and Charlie won {} times.".format(num_games_ran, al_won, ben_won, charlie_won))