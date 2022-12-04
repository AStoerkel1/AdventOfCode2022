
def fully_contains(l1, l2):
    return (l1[1]) in range(l2[0], l2[1]+1) and l1[0] in range(l2[0], l2[1]+1) or (l2[1] in range(l1[0], l1[1]+1) and l2[0] in range(l1[0], l1[1]+1))

def range_overlaps(l1, l2):
    return (l1[1] in range(l2[0], l2[1]+1) or l1[0] in range(l2[0], l2[1]+1)) or (l2[1] in range(l1[0], l1[1]+1) or l2[0] in range(l1[0], l1[1]+1))

def main() -> None:
    sum = 0
    with open("input.txt", "r") as f:
        for l in f:
            l = [val.split('-') for val in l.strip().split(',')]
            if(range_overlaps([int(val) for val in l[0]], [int(val) for val in l[1]])):
                sum+=1
                # print(l)
                # print(fully_contains(l[0], l[1]))

    print(sum)


if __name__ == "__main__":
    main()
