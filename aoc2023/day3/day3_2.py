import re

with open("input","r") as fp:
    #lines = fp.readlines()
    line_m=fp.read().splitlines()
row_len=0
partno_list=[]
adj_symbol_index=[]
row_index=0
word_index=0
        
#define adjacent indexes
same_row_right=line_m[row_index][word_index+1]
same_row_left=line_m[row_index][word_index-1]
diag_left_bottom=line_m[row_index+1][word_index-1]
diag_right_bottom=line_m[row_index+1][word_index+1]
diag_left_top=line_m[row_index-1][word_index-1]
diag_right_top=line_m[row_index-1][word_index+1]
top_row_straight=line_m[row_index-1][word_index]
bottom_row_straight=line_m[row_index+1][word_index]

for line in line_m:
    row_len=len(line)
    numbers=re.findall('\d+', line)
    start_index=0
    for i in numbers:
        word_length=len(i)
        word_index=line.find(i,start_index,row_len)
        for j in range(1, word_length+1):
            if (row_index==0 and word_index ==0): 
                same_row_right=line_m[row_index][word_index+1]
                diag_right_bottom=line_m[row_index+1][word_index+1]
                bottom_row_straight=line_m[row_index+1][word_index]

                if (not same_row_right.isdigit() and not same_row_right=="."):
                    partno_list.append(i)
                    adj_symbol_index.append(str(row_index)+"-"+str(word_index+1))
                    break
                elif  (not diag_right_bottom.isdigit() and not diag_right_bottom=="."):
                    partno_list.append(i)
                    adj_symbol_index.append(str(row_index+1)+"-"+str(word_index+1))
                    break
                    
                elif  (not bottom_row_straight.isdigit() and not bottom_row_straight=="."):
                    partno_list.append(i)
                    adj_symbol_index.append(str(row_index+1)+"-"+str(word_index))
                    break

                
            elif(row_index==0 and word_index ==row_len-1):
                same_row_left=line_m[row_index][word_index-1]
                diag_left_bottom=line_m[row_index+1][word_index-1]
                bottom_row_straight=line_m[row_index+1][word_index]

                if(not same_row_left.isdigit() and not same_row_left=="."):
                    partno_list.append(i)
                    adj_symbol_index.append(str(row_index)+"-"+str(word_index-1))
                    break
                elif (not diag_left_bottom.isdigit() and not diag_left_bottom=="."):
                    partno_list.append(i)
                    adj_symbol_index.append(str(row_index+1)+"-"+str(word_index-1))
                    break

                elif (not bottom_row_straight.isdigit() and not bottom_row_straight=="."):
                    partno_list.append(i)
                    adj_symbol_index.append(str(row_index+1)+"-"+str(word_index))
                    break
            elif(row_index==row_len-1 and word_index==0):
                top_row_straight=line_m[row_index-1][word_index]
                same_row_right=line_m[row_index][word_index+1]
                diag_right_top=line_m[row_index-1][word_index+1]
                
                if(not top_row_straight.isdigit() and not top_row_straight=="."):
                    partno_list.append(i)
                    adj_symbol_index.append(str(row_index-1)+"-"+str(word_index))
                    break 
                elif (not same_row_right.isdigit() and not same_row_right=="."):
                    partno_list.append(i)
                    adj_symbol_index.append(str(row_index)+"-"+str(word_index+1))
                    break
                elif (not diag_right_top.isdigit() and not diag_right_top=="."):
                    partno_list.append(i)
                    adj_symbol_index.append(str(row_index-1)+"-"+str(word_index+1))
                    break
            elif(row_index==row_len-1 and word_index==row_len-1):
                top_row_straight=line_m[row_index-1][word_index]
                diag_left_top=line_m[row_index-1][word_index-1]
                same_row_left=line_m[row_index][word_index-1]

                if (not top_row_straight.isdigit() and not top_row_straight=="."):
                    partno_list.append(i)
                    adj_symbol_index.append(str(row_index-1)+"-"+str(word_index))
                    break
                elif (not diag_left_top.isdigit() and not diag_left_top=="."):
                    partno_list.append(i)
                    adj_symbol_index.append(str(row_index-1)+"-"+str(word_index-1))
                    break
                elif (not same_row_left.isdigit() and not same_row_left=="."):
                    partno_list.append(i)
                    adj_symbol_index.append(str(row_index)+"-"+str(word_index-1))
                    break
            elif(row_index==0):
                same_row_right=line_m[row_index][word_index+1]
                same_row_left=line_m[row_index][word_index-1]
                diag_left_bottom=line_m[row_index+1][word_index-1]
                diag_right_bottom=line_m[row_index+1][word_index+1]
                bottom_row_straight=line_m[row_index+1][word_index]
               
                if(not same_row_left.isdigit() and not same_row_left=="."):
                    partno_list.append(i)
                    adj_symbol_index(str(row_index)+"-"+str(word_index-1))
                    break 
                elif (not same_row_right.isdigit() and not same_row_right=="."):
                    partno_list.append(i)
                    adj_symbol_index(str(row_index)+"-"+str(word_index+1))
                    break
                elif (not diag_left_bottom.isdigit() and not diag_left_bottom=="."):
                    partno_list.append(i)
                    adj_symbol_index.append(str(row_index+1)+"-"+str(word_index-1))
                    break
                elif (not bottom_row_straight.isdigit() and not bottom_row_straight=="."):
                    partno_list.append(i)
                    adj_symbol_index.append(str(row_index+1)+"-"+str(word_index))
                    break
                elif (not diag_right_bottom.isdigit() and not diag_right_bottom=="."):
                    partno_list.append(i)
                    adj_symbol_index.append(str(row_index+1)+"-"+str(word_index+1))
                    break
            elif(row_index==row_len-1):
                same_row_left=line_m[row_index][word_index-1]
                same_row_right=line_m[row_index][word_index+1]
                diag_left_top=line_m[row_index-1][word_index-1]
                top_row_straight=line_m[row_index-1][word_index]
                diag_right_top=line_m[row_index-1][word_index+1]

                if(not same_row_left.isdigit() and not same_row_left=="."):
                    partno_list.append(i)
                    adj_symbol_index.append(str(row_index)+"-"+str(word_index-1))
                    break
                elif (not same_row_right.isdigit() and not same_row_right=="."):
                    partno_list.append(i)
                    adj_symbol_index.append(str(row_index)+"-"+str(word_index+1))
                    break 
                elif (not diag_left_top.isdigit() and not diag_left_top=="."):
                    partno_list.append(i)
                    adj_symbol_index.append(str(row_index-1)+"-"+str(word_index-1))
                    break
                elif (not top_row_straight.isdigit() and not top_row_straight=="."):
                    partno_list.append(i)
                    adj_symbol_index.append(str(row_index-1)+"-"+str(word_index))
                    break 
                elif (not diag_right_top.isdigit() and not diag_right_top=="."):
                    partno_list.append(i)
                    adj_symbol_index.append(str(row_index-1)+"-"+str(word_index+1))
                    break
            elif(word_index==0):
 
                top_row_straight=line_m[row_index-1][word_index]
                bottom_row_straight=line_m[row_index+1][word_index]
                diag_right_bottom=line_m[row_index+1][word_index+1]
                same_row_right=line_m[row_index][word_index+1]
                diag_right_top=line_m[row_index-1][word_index+1]

                if(not top_row_straight.isdigit() and not top_row_straight=="."):
                    partno_list.append(i)
                    adj_symbol_index.append(str(row_index-1)+"-"+str(word_index))
                    break 
                elif (not bottom_row_straight.isdigit() and not bottom_row_straight=="."):
                    partno_list.append(i)
                    adj_symbol_index.append(str(row_index+1)+"-"+str(word_index))
                    break
                elif (not diag_right_top.isdigit() and not diag_right_top=="."):
                    partno_list.append(i)
                    adj_symbol_index.append(str(row_index-1)+"-"+str(word_index+1))
                    break
                elif (not same_row_right.isdigit() and not same_row_right=="."):
                    partno_list.append(i)
                    adj_symbol_index.append(str(row_index)+"-"+str(word_index+1))

                elif (not diag_right_bottom.isdigit() and not diag_right_bottom=="."):
                    partno_list.append(i)
                    adj_symbol_index.append(str(row_index+1)+"-"+str(word_index+1))
                    break
            elif(word_index==row_len-1):
                diag_left_top=line_m[row_index-1][word_index-1]
                same_row_left=line_m[row_index][word_index-1]
                diag_left_bottom=line_m[row_index+1][word_index-1]
                top_row_straight=line_m[row_index-1][word_index]
                bottom_row_straight=line_m[row_index+1][word_index]

                if(not diag_left_top.isdigit() and not diag_left_top=="."):
                    partno_list.append(i)
                    adj_symbol_index.append(str(row_index-1)+"-"+str(word_index-1))
                    break
                elif (not same_row_left.isdigit() and not same_row_left=="."):
                    partno_list.append(i)
                    adj_symbol_index.append(str(row_index)+"-"+str(word_index-1))
                    break
                elif (not diag_left_bottom.isdigit and not diag_left_bottom=="."):
                    partno_list.append(i)
                    adj_symbol_index.append(str(row_index+1)+"-"+str(word_index-1))
                    break
                elif (not top_row_straight.isdigit() and not top_row_straight=="."):
                    partno_list.append(i)
                    adj_symbol_index.append(str(row_index-1)+"-"+str(word_index))
                    break
                elif (not bottom_row_straight.isdigit() and not bottom_row_straight=="."):
                    partno_list.append(i)
                    adj_symbol_index.append(str(row_index+1)+"-"+str(word_index))
                    break
            else:
                same_row_right=line_m[row_index][word_index+1]
                same_row_left=line_m[row_index][word_index-1]
                diag_left_bottom=line_m[row_index+1][word_index-1]
                diag_right_bottom=line_m[row_index+1][word_index+1]
                diag_left_top=line_m[row_index-1][word_index-1]
                diag_right_top=line_m[row_index-1][word_index+1]
                top_row_straight=line_m[row_index-1][word_index]
                bottom_row_straight=line_m[row_index+1][word_index]

                if(not diag_left_top.isdigit() and not diag_left_top=="."):
                    partno_list.append(i)
                    adj_symbol_index.append(str(row_index-1)+"-"+str(word_index-1))
                    break
                elif (not top_row_straight.isdigit() and not top_row_straight=="."):
                    partno_list.append(i)
                    adj_symbol_index.append(str(row_index-1)+"-"+str(word_index))
                    break
                elif (not diag_right_top.isdigit() and not diag_right_top=="." ):
                    partno_list.append(i)
                    adj_symbol_index.append(str(row_index-1)+"-"+str(word_index+1))
                    break
                elif (not same_row_left.isdigit() and not same_row_left=="."):
                    partno_list.append(i)
                    adj_symbol_index.append(str(row_index)+"-"+str(word_index-1))
                    break
                elif (not same_row_right.isdigit() and not same_row_right=="."):
                    partno_list.append(i)
                    adj_symbol_index.append(str(row_index)+"-"+str(word_index+1))
                    break
                elif (not diag_left_bottom.isdigit() and not diag_left_bottom=="."):
                    partno_list.append(i)
                    adj_symbol_index.append(str(row_index+1)+"-"+str(word_index-1))
                    break
                elif (not bottom_row_straight.isdigit() and not bottom_row_straight=="."):
                    partno_list.append(i)
                    adj_symbol_index.append(str(row_index+1)+"-"+str(word_index))
                    break
                elif (not diag_right_bottom.isdigit() and not diag_right_bottom=="."):
                    partno_list.append(i)
                    adj_symbol_index.append(str(row_index+1)+"-"+str(word_index+1))
                    break
            word_index+=1
            
        start_index=word_index

    row_index+=1

sum=0
for partno in partno_list:
    sum+=int(partno)

temp_list=[]

index=[x for x in adj_symbol_index if adj_symbol_index.count(x) > 1]
temp_list.append(index)

#list_without_duplicates = [i for n, i in enumerate(index) if i not in index[:n]]

#print(adj_symbol_index)
#print(partno_list)

#print(index)

total_sum=0
new_index=0
for h in adj_symbol_index:
    old_index=0
    for k in adj_symbol_index:
        if (h == k and new_index < old_index):
            #x=h.split("-")
            print(h,k)
            print(partno_list[new_index], partno_list[old_index])
            products=int(partno_list[new_index])*int(partno_list[old_index])
            #print(products)
            total_sum+=products
            #print("new and old: ", new_index, old_index)
        old_index+=1
        
    new_index+=1
    
print("total sum:", total_sum)
