
def countCalories():
    arr = []
    with open('./input.txt', 'r') as f:
        current_sum = 0
        for line in f:
            if line == '\n':
                arr.append(current_sum)
                current_sum = 0
            else:
                current_sum += int(line)
    sume = 0
    for i in range(3):
        temp = 0
        temp = max(arr)
        arr.remove(temp)
        sume += temp
    print(sume)

if __name__ == '__main__':
    countCalories()
        