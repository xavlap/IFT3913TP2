import csv

total = 0;
total_classes = 0;
list = []
with open('../Data/class.csv', 'r') as inputs:
    r = csv.reader(inputs, delimiter=',')
    for row in r:
        l = [str(row[0]), str(row[1]), str(row[10])]
        list.append(l)
        if (str(row[10]) == 'rfc' or str(row[10]) == 'NaN'):
            pass
        else :
            total += float(row[10])

        total_classes += 1

print(total/total_classes)

with open('../Data/ckjm_RFC.csv', 'w') as outputs:
    w = csv.writer(outputs)
    for i in range(len(list)):
        w.writerow(list[i])
