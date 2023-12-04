with open("input.txt", "r") as f:
    total = 0
    for line in f.readlines():
        line = line.strip().split(":")[1].split("|")
        winning = line[0].strip().split()
        have = line[1].strip().split()
        winning_num = 0
        for i in have:
            if i in winning:
                if winning_num == 0: winning_num = 1
                else: winning_num *= 2
        total += winning_num
    print(total)
    