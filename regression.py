import math
import csv
import os


## TODO:


# alternate test case
# x = [52.16, 55.23, 56.74, 58.12, 60.67]
# y = [157.48, 164.56, 152.40, 150.94, 170.72]
# test case, replace with read from excel file or cvs
# x = [17, 13, 12, 15, 16, 14, 16, 16, 18, 19]
# y = [94, 73, 59, 80, 93, 85, 66, 79, 77, 91]
y = []  # Dependent variable
x = []  # Independent variable

# read file and pull vallues

file = os.path.join("Resources", "text.csv")
with open(file, mode="r") as values:
    reader = csv.reader(values)
    header = next(reader)

    for row in reader:
        y.append(int(row[0]))
        x.append(int(row[1]))


xmean = sum(x) / len(x)
ymean = sum(y) / len(y)

sumxminusxmeansq = 0.00
sumyminusymeansq = 0.00
sumxminusxmean = 0.00
sumyminusymean = 0.00
xXyY = 0.0
# slope
b = 0.0
# Intercept
a = 0.0
# pearsons correlation coeeficient
r = 0

for i in range(len(x)):
    sumxminusxmeansq += (x[i] - xmean) ** 2
    sumxminusxmean += x[i] - xmean
    sumyminusymeansq += (y[i] - ymean) ** 2
    sumyminusymean += y[i] - ymean
    xXyY += (x[i] - xmean) * (y[i] - ymean)

r = xXyY / math.sqrt(sumxminusxmeansq * sumyminusymeansq)
b = r * math.sqrt(sumyminusymeansq / (len(y) - 1) / (sumxminusxmeansq / (len(x) - 1)))
a = ymean - b * xmean

print("Pearson Correlation Coeeficient: " + str(r))
print("Slope: " + str(b))
print("Y Intercept: " + str(a))
