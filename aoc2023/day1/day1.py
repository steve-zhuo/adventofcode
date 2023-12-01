class Calibration:
    def __init__(self, a):
        self.a = a

    def get_sum(self):
        if len(self.a) == 0:
            return 0
        else:
            return int(self.a[0] + self.a[-1])

sum = 0
testline=0
with open("input","r") as fp:
    lines = fp.readlines()
for line in lines:
    index=0
    digit_list=[]
    index_list=[]
    for i in line:
        if i.isdigit():
            digit_list.append(i)
            index_list.append(index)
        index+=1
    word_list=["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    num_list=["1","2","3","4","5","6","7","8","9"]
    i=0
    for word in word_list:
 
        word_index=line.find(word)
        word_r_index=line.rfind(word)
        if word_index >= 0:
            if word_index > index_list[-1]:
                digit_list.append(num_list[i])
                index_list.append(word_index)
            j=0
            for k in index_list:
                
                if word_index < k:   
                    digit_list.insert(j, num_list[i])
                    index_list.insert(j, word_index)
                    break
                    
                j+=1
        if word_r_index > word_index:
            if word_r_index >= 0:
                if word_r_index > index_list[-1]:
                    digit_list.append(num_list[i])
                    index_list.append(word_r_index)
            j=0
            for k in index_list:
                if word_r_index < k:
                    digit_list.insert(j, num_list[i])
                    index_list.insert(j, word_r_index)
                    break
                  
                j+=1
            

        i+=1   
    calibration=Calibration(digit_list)      
    line_digit=calibration.get_sum()
    sum+=line_digit
print(sum)

