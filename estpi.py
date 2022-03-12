import random
import math


def calc_pi(num_of_shots):
    circle_hits = []
    square_hits = []
    for i in range(num_of_shots):
        xvals = random.uniform(-1, 1)
        yvals = random.uniform(-1, 1)

        d = math.sqrt(xvals ** 2 + yvals ** 2)

        if d <= 1:
            circle_hits.append(1)
            square_hits.append(0)
        elif d > 1:
            square_hits.append(1)
            circle_hits.append(0)

        pi = 4 * sum(circle_hits) / num_of_shots
    return pi


print(calc_pi(10))
print(calc_pi(1000))
print(calc_pi(10_000))
# print(calc_pi(1_000_000))
