
def fully_contains(l1, l2):
    return (int(l1[1]) in range(int(l2[0]), int(l2[1])+1) and int(l1[0]) in range(int(l2[0]), int(l2[1])+1)) or (int(l2[1]) in range(int(l1[0]), int(l1[1])+1) and int(l2[0]) in range(int(l1[0]), int(l1[1])+1))

def range_overlaps(l1, l2):
    return (int(l1[1]) in range(int(l2[0]), int(l2[1])+1) or int(l1[0]) in range(int(l2[0]), int(l2[1])+1)) or (int(l2[1]) in range(int(l1[0]), int(l1[1])+1) or int(l2[0]) in range(int(l1[0]), int(l1[1])+1))

def main() -> None:
    sum = 0
    with open("input.txt", "r") as f:
        for l in f:
            l = [val.split('-') for val in l.strip().split(',')]
            if(range_overlaps(l[0], l[1])):
                sum+=1
                # print(l)
                # print(fully_contains(l[0], l[1]))

    print(sum)


if __name__ == "__main__":
    main()
