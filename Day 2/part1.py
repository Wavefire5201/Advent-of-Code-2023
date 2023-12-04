with open("input.txt", "r") as f:
    data = f.read().splitlines()
total = 0
possible_cubes = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

for line in data:
    line = line.split(":")
    # print(line)
    game = line[0][-3:].replace("e", "", 1).replace(" ", "")
    print(f"Game number {game}")
    rounds = line[1].split(";")
    print(rounds)
    
    possible = 3
    for round in rounds:
        cubes = {
            "red": 0,
            "green": 0,
            "blue": 0,
        }
        rolls = round.split(",")
        print(rolls)
        for roll in rolls:
            roll = roll.split(" ")
            cubes[roll[2]] += int(roll[1])
            
        print(cubes)
        print(possible_cubes)
        
        for cube in cubes:
            # print(cubes[cube])
            # print(possible_cubes[cube])
            if cubes[cube] > possible_cubes[cube]:
                possible -= 1
            # print(game)
    if possible == 3: 
        total += int(game)
        print(game)
        
    print("\n")
    
            
print(total)