

with open("input","r") as fp:
    lines = fp.readlines()

sum=0
for line in lines:
    cubes={"red": 1, "green": 1, "blue": 1}
    game_no=int(line.split(":")[0].split()[1])
    game_sets=line.split(":")[1].split(";")
    game_cube_power=1
    for gameset in game_sets:
        gameset_list=gameset.split(",")
        for cube in gameset_list:
            cube_no=int(cube.split()[0])
            cube_color=cube.split()[1]
            if cubes[cube_color] < cube_no:
                cubes[cube_color]=cube_no

    game_cube_power=cubes["red"]*cubes["green"]*cubes["blue"]
    print(cubes['red'],cubes['green'],cubes['blue'])
    sum+=game_cube_power
   
print(sum)

