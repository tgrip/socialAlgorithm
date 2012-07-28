__author__ = 'Theo'

import csv

maxVal = 0
secondVal = 0
mostName = ''
secondName = ''
csvFile = open('file.txt')
fileReader = csv.reader(csvFile)

for row in fileReader:
    if row[1] == 'F':
#        print row[2]
        if int(row[2]) > maxVal:
            print 'changed to', row[2]
            secondVal = maxVal
            secondName = mostName
            maxVal = int(row[2])
            mostName = row[0]
#        elif row[2] > secondVal:
#            secondVal = row[2]

print maxVal, secondVal, mostName, secondName