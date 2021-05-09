"""Mean
Median
Variance
Std-dev
IQR (Inter-Quartile Range)
90th percentile
99th percentile
Median Absolute Deviation"""
import math
# for mean
def meancalc(list):
    sum = 0;
    for i in list:
        sum = sum+i
    mean = sum/num
    return mean

#for Median
def median(list):
    med = 0
    if num%2 == 0:   #even
        m = num/2
        med = (list[m]+list[m+1])/2
    else:                             #odd
        m = math.floor(num/2)
        med = list[m]
    return med    

# for variance
def variance(list):
    var = 0
    m = meancalc(lst)
    var = sum((i-m)**2 for i in list)/num
    return var
    
#for Std-dev
def std_dev(list):
    var = variance(list)
    std = math.sqrt(var)
    return std

#for InterQuartile Range
#IQR= 75Th percentile - 25th percentile 
#IQR = 3rd Quantile - 1st Quantile
    
def interqr(list):
    first = list[math.floor((num+1)/4)]
    third = list[math.floor((3*(num+1))/4)]
    iqr = third-first
    return iqr
        
#99th percentile
def percentile(list):
    index = math.floor((num-1)*(99/100))                            #knowing the index of x percentile 
    perc = list[index] 
    return perc

# median Absolute deviation
def MAD(list):
    med = median(list)
    l = [(abs(i-med)) for i in list]
    mad = median(l)
    return mad


if __name__ == "__main__":
    lst =[1,4,6,8,10,12,15]
    lst.sort()
    num = len(lst)
    print(meancalc(lst))
    print(median(lst))
    print(std_dev(lst))
    print(MAD(lst))
    print(interqr(lst))
    print(percentile(lst))