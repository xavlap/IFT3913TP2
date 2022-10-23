import csv

list = []
with open('../Data/class.csv', 'r') as inputs:
    r = csv.reader(inputs, delimiter=',')
    for row in r:
        l = [str(row[0]), str(row[1]), str(row[10])]
        list.append(l)

with open('../Data/ckjm_RFC.csv', 'w') as outputs:
    w = csv.writer(outputs)
    for i in range(len(list)):
        w.writerow(list[i])
