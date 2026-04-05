import numpy as np
from scipy import stats

marks = [60 ,20 ,10 ,10 ,30 ,60 ,20 ,50]

#Standard Deviation: measures how much values differ from mean
std = np.std(marks)
print("Std of marks: ",std)

#Mode: most frequently occurring value
mode = stats.mode(marks,keepdims=True)
print("Mode of marks: ",mode.mode[0])

#Variance: square of standard deviation
var = np.var(marks)
print("Var of marks: ",var)

#Mean: average value
mean = np.mean(marks)
print("Mean of marks: ",mean)

#Median: middle value after sorting
median = np.median(marks)
print("Median of marks: ",median)
