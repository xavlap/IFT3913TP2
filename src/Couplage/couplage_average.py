import csv

sum = 0;
i = 0
with open('../../Data/lcsec.csv', 'r') as inputs:
    r = csv.reader(inputs, delimiter=',')
    for row in r:
        sum+= float(row[3])
        i+=1

print(sum/i)