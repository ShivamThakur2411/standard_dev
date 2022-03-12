import csv
import math

from numpy import square

with open("data.csv") as f:
    reader = csv.reader(f)
    file_data = list(reader)

data = file_data[0]

sum_of_all_entries = 0
total_entries = len(data)

for x in data:
    sum_of_all_entries += int(x)

mean = sum_of_all_entries/total_entries
print("Mean of the data is == " + str(mean))


squared_list=[]

for y in data:
    num = int(y) - mean
    num = num**2
    squared_list.append(num)

sum=0

for i in squared_list:
    sum += i

print(sum)
len_subt_one = len(data)-1

num_bfr_sqrt = sum/len_subt_one
standard_dev = math.sqrt(num_bfr_sqrt)
print("Standard Deviation is == " + str(standard_dev))