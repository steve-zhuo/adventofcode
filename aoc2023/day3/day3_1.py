import re

with open("input","r") as fp:
    #lines = fp.readlines()
    line_m=fp.read().splitlines()
row_len=0
partno_list=[]
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
#        print("start and end indexes:", start_index, row_len)
        for j in range(1, word_length+1):
            if (row_index==0 and word_index ==0): 
                same_row_right=line_m[row_index][word_index+1]
                diag_right_bottom=line_m[row_index+1][word_index+1]
                bottom_row_straight=line_m[row_index+1][word_index]

                if (not same_row_right.isdigit() and not same_row_right==".") or (not diag_right_bottom.isdigit() and not diag_right_bottom==".") or (not bottom_row_straight.isdigit() and not bottom_row_straight=="."):
                    partno_list.append(i)
                    break
            elif(row_index==0 and word_index ==row_len-1):
                same_row_left=line_m[row_index][word_index-1]
                diag_left_bottom=line_m[row_index+1][word_index-1]
                bottom_row_straight=line_m[row_index+1][word_index]

                if(not same_row_left.isdigit() and not same_row_left==".") or (not diag_left_bottom.isdigit() and not diag_left_bottom==".") or (not bottom_row_straight.isdigit() and not bottom_row_straight=="."):
                    partno_list.append(i)
                    break
            elif(row_index==row_len-1 and word_index==0):
                top_row_straight=line_m[row_index-1][word_index]
                same_row_right=line_m[row_index][word_index+1]
                diag_right_top=line_m[row_index-1][word_index+1]
                
                if(not top_row_straight.isdigit() and not top_row_straight==".") or (not same_row_right.isdigit() and not same_row_right==".") or (not diag_right_top.isdigit() and not diag_right_top=="."):
                    partno_list.append(i)
                    break
            elif(row_index==row_len-1 and word_index==row_len-1):
                top_row_straight=line_m[row_index-1][word_index]
                diag_left_top=line_m[row_index-1][word_index-1]
                same_row_left=line_m[row_index][word_index-1]

                if(not top_row_straight.isdigit() and not top_row_straight==".") or (not diag_left_top.isdigit() and not diag_left_top==".") or (not same_row_left.isdigit() and not same_row_left=="."):
                    partno_list.append(i)
                    break
            elif(row_index==0):
#                print("word index:", word_index)
                same_row_right=line_m[row_index][word_index+1]
                same_row_left=line_m[row_index][word_index-1]
                diag_left_bottom=line_m[row_index+1][word_index-1]
                diag_right_bottom=line_m[row_index+1][word_index+1]
                bottom_row_straight=line_m[row_index+1][word_index]
               
                if(not same_row_left.isdigit() and not same_row_left==".") or (not same_row_right.isdigit() and not same_row_right==".") or (not diag_left_bottom.isdigit() and not diag_left_bottom==".") or (not bottom_row_straight.isdigit() and not bottom_row_straight==".") or (not diag_right_bottom.isdigit() and not diag_right_bottom=="."):
                    partno_list.append(i)
                    break
            elif(row_index==row_len-1):
                same_row_left=line_m[row_index][word_index-1]
                same_row_right=line_m[row_index][word_index+1]
                diag_left_top=line_m[row_index-1][word_index-1]
                top_row_straight=line_m[row_index-1][word_index]
                diag_right_top=line_m[row_index-1][word_index+1]

                if(not same_row_left.isdigit() and not same_row_left==".") or (not same_row_right.isdigit() and not same_row_right==".") or (not diag_left_top.isdigit() and not diag_left_top==".") or (not top_row_straight.isdigit() and not top_row_straight==".") or (not diag_right_top.isdigit() and not diag_right_top=="."):
                    partno_list.append(i)
                    break
            elif(word_index==0):
 
                top_row_straight=line_m[row_index-1][word_index]
                bottom_row_straight=line_m[row_index+1][word_index]
                diag_right_bottom=line_m[row_index+1][word_index+1]
                same_row_right=line_m[row_index][word_index+1]
                diag_right_top=line_m[row_index-1][word_index+1]

                if(not top_row_straight.isdigit() and not top_row_straight==".") or (not bottom_row_straight.isdigit() and not bottom_row_straight==".") or (not diag_right_top.isdigit() and not diag_right_top==".") or (not same_row_right.isdigit() and not same_row_right==".") or (not diag_right_bottom.isdigit() and not diag_right_bottom=="."):
                    partno_list.append(i)
                    break
            elif(word_index==row_len-1):
                diag_left_top=line_m[row_index-1][word_index-1]
                same_row_left=line_m[row_index][word_index-1]
                diag_left_bottom=line_m[row_index+1][word_index-1]
                top_row_straight=line_m[row_index-1][word_index]
                bottom_row_straight=line_m[row_index+1][word_index]

                if(not diag_left_top.isdigit() and not diag_left_top==".") or (not same_row_left.isdigit() and not same_row_left==".") or (not diag_left_bottom.isdigit and not diag_left_bottom==".") or (not top_row_straight.isdigit() and not top_row_straight==".") or (not bottom_row_straight.isdigit() and not bottom_row_straight=="."):
                    partno_list.append(i)
                    break
            else:
#                print("word index:", word_index)
                same_row_right=line_m[row_index][word_index+1]
                same_row_left=line_m[row_index][word_index-1]
                diag_left_bottom=line_m[row_index+1][word_index-1]
                diag_right_bottom=line_m[row_index+1][word_index+1]
                diag_left_top=line_m[row_index-1][word_index-1]
                diag_right_top=line_m[row_index-1][word_index+1]
                top_row_straight=line_m[row_index-1][word_index]
                bottom_row_straight=line_m[row_index+1][word_index]

                if(not diag_left_top.isdigit() and not diag_left_top==".") or (not top_row_straight.isdigit() and not top_row_straight==".") or (not diag_right_top.isdigit() and not diag_right_top=="." ) or (not same_row_left.isdigit() and not same_row_left==".") or (not same_row_right.isdigit() and not same_row_right==".") or (not diag_left_bottom.isdigit() and not diag_left_bottom==".") or (not bottom_row_straight.isdigit() and not bottom_row_straight==".") or (not diag_right_bottom.isdigit() and not diag_right_bottom=="."):
                    partno_list.append(i)
                    break
            word_index+=1
        start_index=word_index

    row_index+=1
    
sum=0
for partno in partno_list:
    sum+=int(partno)
print(len(partno_list))
print(sum)
