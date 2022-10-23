import csv

stats = 0;
zeroes = 0;
list = []
with open('../Data/class.csv', 'r') as inputs:
    r = csv.reader(inputs, delimiter=',')
    for row in r:
        l = [str(row[0]), str(row[1]), str(row[12])]
        if (row[12] == 'lcom*' or row[12] == 'NaN'):
            pass
        else :
            stats += float(row[12])
            if float(row[12]) == 0:
                 zeroes = zeroes + 1
        list.append(l)

print(stats / len(list))
print(zeroes)
print(len(list))

with open('../Data/ckjm_lcom.csv', 'w') as outputs:
    w = csv.writer(outputs)
    for i in range(len(list)):
        w.writerow(list[i])

