'''
A = rock
B = paper
c = Scicors
x = rock
y = paper
z = scissors
'''

comp = {
    'X': 'A',
    'Y': 'B',
    'Z': 'C',
}

win = {
    'A': 'C',
    'B': 'A',
    'C': 'B'
}

lose = {
    'A': 'B',
    'B': 'C',
    'C': 'A'
}

score = {
    'A': 1,
    'B': 2,
    'C': 3
}

'''
A X Rock
B Y Paper
C Z Scissors
'''
'''
X lose
Y draw
Z win
'''

def winOrLose(i):
    if i == 'X':
        return 0
    if i == 'Y':
        return 3
    if i == 'Z':
        return 6

def myChoice(them, cond):
    if winOrLose(cond) == 0:
        return win[them]
    if winOrLose(cond) == 3:
        return them
    if winOrLose(cond) == 6:
        return lose[them]


def main():
    with open('input.txt', 'r') as f:
        choice = ''
        total = 0
        for line in f:
            i = line.split()
            choice = myChoice(i[0], i[1])
            total += score[choice] + winOrLose(i[1])
        print(total)


if __name__ == '__main__':
    main()
