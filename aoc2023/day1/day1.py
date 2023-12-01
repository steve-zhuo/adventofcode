class Calibration:
    def __init__(self, a):
        self.a = a

    def get_sum(self):
        if len(self.a) == 0:
            return 0
        else:
            return int(self.a[0] + self.a[-1])
 #   def get_sum_total(self,a):
 #       #calculate total sum
 #       sum = 0
 #       with open(self.a,"r") as fp:
 #           lines = fp.readlines()
 #       for line in lines:
 #           digit_list=[]
 #           for i in line:
 #               if i.isdigit():
 #                   digit_list.append(i)
 #           calibration=self.get_sum()        
 #           line_digit=calibration.get_sum()
 #           sum+=line_digit
 #       print(sum)

#calibration=Calibration("input")
#calculate total sum
sum = 0
with open("input","r") as fp:
    lines = fp.readlines()
for line in lines:
    digit_list=[]
    for i in line:
        if i.isdigit():
            digit_list.append(i)
    calibration=Calibration(digit_list)        
    line_digit=calibration.get_sum()
    sum+=line_digit
print(sum)

test="eightwothree"
if "eight" in test:
    print("three")
if "three" in test:
    print("eight")


