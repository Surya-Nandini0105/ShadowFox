# Simple die rolling program
import random
count_6 = 0
count_1 = 0
two_6_in_row = 0
previous = 0

for i in range(20):
    roll = random.randint(1, 6)
    print("Roll:", roll)
    if roll == 6:
        count_6 += 1
        if previous == 6:
            two_6_in_row += 1
    if roll == 1:
        count_1 += 1
    
    previous = roll

print("Total 6s rolled:", count_6)
print("Total 1s rolled:", count_1)
print("Two 6s in a row:", two_6_in_row)
