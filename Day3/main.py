dic = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6,
    'g': 7,
    'h': 8,
    'i': 9,
    'j': 10,
    'k': 11,
    'l': 12,
    'm': 13,
    'n': 14,
    'o': 15,
    'p': 16,
    'q': 17,
    'r': 18,
    's': 19,
    't': 20,
    'u': 21,
    'v': 22,
    'w': 23,
    'x': 24,
    'y': 25,
    'z': 26,
    'A': 27,
    'B': 28,
    'C': 29,
    'D': 30,
    'E': 31,
    'F': 32,
    'G': 33,
    'H': 34,
    'I': 35,
    'J': 36,
    'K': 37,
    'L': 38,
    'M': 39,
    'N': 40,
    'O': 41,
    'P': 42,
    'Q': 43,
    'R': 44,
    'S': 45,
    'T': 46,
    'U': 47,
    'V': 48,
    'W': 49,
    'X': 50,
    'Y': 51,
    'Z': 52,
}

def tripIntersect(l1, l2, l3):
    return [val2 for val2 in intersection(l1, l2) if val2 in l3]
    

def intersection(l1, l2):
    return [val for val in l1 if val in l2]


def main():
    group = []
    tracker = 1
    sum = 0
    with open('input.txt', 'r') as f:
        for l in f:
            # first = list(l[:int(len(l)/2)])
            # second = list(l[int(len(l)/2):])
            # sum += dic[intersection(first, second)[0]]
            group.append(list(l))
            if tracker == 3:
                sum+=dic[tripIntersect(group[0], group[1], group[2])[0]]
                tracker = 0
                group = []
            tracker+=1
            
    print(sum)

if __name__ == "__main__":
    main()