
MESSAGE_LEN = 14
with open('input.txt', 'r') as f:
    l = list(f.readline())
    for i in range(len(l)):
        if( len(set(l[i:i+MESSAGE_LEN])) == MESSAGE_LEN ):
            print(i+MESSAGE_LEN)
            break