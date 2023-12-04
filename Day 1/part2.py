with open("input.txt", "r") as f:
    data = f.read().splitlines()
total = 0
replace_dict = {
    "two": "t2o",
    "one": "o1e",
    "three": "t3e",
    "four": "f4r",
    "five" : "f5e",
    "six": "s6x",
    "seven": "s7n",
    "nine": "n9e",
    "eight": "e8t",
}

for word in data:
    nums = []
    print(word)
    for i in range(3):
        for num in replace_dict:
            if num in word:
                word = word.replace(num, replace_dict[num], 1)
    for letter in word:
        if letter.isnumeric(): nums.append(int(letter))
    total += int(f"{nums[0]}{nums[-1]}")
print(total)