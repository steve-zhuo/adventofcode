
with open("input","r") as fp:
    lines = fp.readlines()

sum=0
origininal_winning_count=[]
total_lines=len(lines)
copies_winning_count= [ []*total_lines for i in range(total_lines)]
#copies_winning_count = [[0 for j in range(total_lines)] for i in range(total_lines)]

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
    origininal_winning_count.append(winning_count)
 
    sum+=winning_point

start_index=0
for j in origininal_winning_count:
    copies=int(j)
    for k in range(start_index,copies+start_index):
        copies_winning_count[k].append(1)
    start_index+=1 

total_scratch_cards=copies_winning_count[:]

print(copies_winning_count)

index=1
number=2
origin_index=1
for l in origininal_winning_count[1:]:
  #  print("original: ",l)
    copies=int(l)

  
    for m in copies_winning_count:
        m_len=len(m)
 #       print("m: ", m)
        for k in range(index,copies+index):
            if k >=total_lines-1:
                break
            #print("copies: ",l, "start: ", index, "end: ",copies+index, "k: ", k)
            #if len(copies_winning_count[index])>0:
            if len(m) >0:
#print("copies: ", k, copies_winning_count[k])
                copies_winning_count[k].append(number)
                print("number: ",number, copies, origin_index)
                number+=1
                print(m)
            print(m_len)
           
        if m_len == 1:
            index+=1
    index+=1
    origin_index+=1


       
print(copies_winning_count)
print(origininal_winning_count)
#print(sum)

