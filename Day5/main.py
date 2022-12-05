
'''
[V]     [B]                     [F]
[N] [Q] [W]                 [R] [B]
[F] [D] [S]     [B]         [L] [P]
[S] [J] [C]     [F] [C]     [D] [G]
[M] [M] [H] [L] [P] [N]     [P] [V]
[P] [L] [D] [C] [T] [Q] [R] [S] [J]
[H] [R] [Q] [S] [V] [R] [V] [Z] [S]
[J] [S] [N] [R] [M] [T] [G] [C] [D]
 1   2   3   4   5   6   7   8   9 
'''

'''
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 
'''

dic = {
    1: ['J','H', 'P', 'M', 'S', 'F', 'N', 'V'],
    2: ['S', 'R', 'L', 'M', 'J', 'D', 'Q'],
    3: ['N','Q','D', 'H', 'C', 'S', 'W', 'B'],
    4: ['R', 'S', 'C', 'L'],
    5: ['M', 'V', 'T', 'P', 'F', 'B'],
    6: ['T', 'R', 'Q', 'N', 'C'],
    7: ['G', 'V', 'R'],
    8: ['C','Z','S','P','D','L','R'],
    9: ['D', 'S', 'J','V','G','P','B','F'],
    'switch': []
}

def main() -> None:
    with open("input.txt", "r") as f:
        for l in f:
            l = l.strip().split(' ')
            number = int(l[1])
            fromStack = int(l[3])
            toStack = int(l[5])
            for i in range(number):
                b = dic[fromStack].pop()
                dic['switch'].append(b)
            for i in range(number):
                b = dic['switch'].pop()
                dic[toStack].append(b)
        for i, k in enumerate(dic):
            if k == 'switch':
                print()
            else: 
                print(dic[k][-1], end="")




if __name__ == "__main__":
    main()
