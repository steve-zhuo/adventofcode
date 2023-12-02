cubes={"red": 12, "green": 13, "blue": 14}

with open("input","r") as fp:
    lines = fp.readlines()

sum=0
for line in lines:
    game_no=int(line.split(":")[0].split()[1])
    game_sets=line.split(":")[1].split(";")
    game_cube_count=0
    possible_game_cube_no=0
    for gameset in game_sets:
        gameset_list=gameset.split(",")
        game_cube_count+=len(gameset_list)
        for cube in gameset_list:
            cube_no=int(cube.split()[0])
            cube_color=cube.split()[1]
            if cubes[cube_color] < cube_no:
                break
            else:
                possible_game_cube_no+=1
    if game_cube_count == possible_game_cube_no:
        sum+=game_no
   
print(sum)

