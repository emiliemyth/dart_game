## At what point should we expect a series of coin flips to reach 50 / 50 ?

import random
rounds = 10000000
x = 0
n1 = 0
n0 = 0

while x < rounds:
    r = random.randint(0,1)

    if r == 1:
        n1 = n1 + 1

    if r == 0:
        n0 = n0 + 1

    x = x + 1


print("With {} rounds, 0 happened {} times and 1 happend {} times.".format(rounds, n0, n1))
