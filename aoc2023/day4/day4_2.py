
with open("input","r") as fp:
    lines = fp.readlines()

sum=0
for line in lines:
    x=line.split("|")
    winning_no=x[0].split(":")[1].split()
    listofno=x[1].split()

    winning_count=0
    winning_point=0
    for i in winning_no:
        if i in listofno:
            winning_point=2**winning_count
            winning_count+=1
    sum+=winning_point

print(sum)
