with open("input.txt", "r") as f:
    total = 0
    for word in f.readlines():
        word_arr = []
        for letter in word: 
            if letter.isnumeric(): word_arr.append(int(letter))
        total += int(f"{word_arr[0]}{word_arr[-1]}")      
    print(total)