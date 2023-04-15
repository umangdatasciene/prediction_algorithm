import csv
import statistics
import numpy as np

data_x = []
data_y = []


with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader) 
    for row in reader:
        data_x.append(float(row[0]))
        data_y.append(float(row[1]))


mean_x = statistics.mean(data_x)
mean_y = statistics.mean(data_y)
print('Mean of x:', mean_x)
print('Mean of y:', mean_y)


median_x = statistics.median(data_x)
median_y = statistics.median(data_y)
print('Median of x:', median_x)
print('Median of y:', median_y)


try:
    mode_x = statistics.mode(data_x)
except statistics.StatisticsError:
    mode_x = 'No mode found for x'
print('Mode of x:', mode_x)
try:
    mode_y = statistics.mode(data_y)
except statistics.StatisticsError:
    mode_y = 'No mode found for y'
print('Mode of y:', mode_y)

stdev_x = statistics.stdev(data_x)
stdev_y = statistics.stdev(data_y)
print('Standard deviation of x:', stdev_x)
print('Standard deviation of y:', stdev_y)


corr = np.corrcoef(data_x, data_y)[0, 1]
print('Correlation:', corr)

var_x = statistics.variance(data_x)
var_y = statistics.variance(data_y)
print('Variance of x:', var_x)
print('Variance of y:', var_y)
