with open("input.txt", "r") as f:
    num_cards, cards_won = [], []
    for line in f.readlines():
        line = line.strip().split(":")[1].split("|")
        winning, have = line[0].strip().split(), line[1].strip().split()
        winning_num = 0
        for i in have:
            if i in winning:
                if winning_num == 0: winning_num = 1
                else: winning_num += 1
        cards_won.append(winning_num)
        num_cards.append(1)
    for i in range(len(num_cards)):
        cards_won_temp = cards_won[i]
        if cards_won_temp > 0:
            for _ in range(num_cards[i]):
                for j in range(i + 1, cards_won_temp + i + 1):
                    num_cards[j] += 1
    print(sum(num_cards))
