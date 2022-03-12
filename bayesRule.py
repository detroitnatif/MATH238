from random import randint


def monte():
    patients = []
    sick = 0
    not_sick = 0
    FP = 0
    TP = 0
    for i in range(100_000):
        patients.append(randint(0, 10_001))

    for j in patients:
        if j == 10_000:
            sick += 1
        else:
            not_sick += 1

    print(sick, not_sick)


monte()
