
import numpy
import pandas

from matplotlib import pyplot as plt

from Module3 import df

#checking the shape of dataframe df(records,columns)
print('*************Data shape***********')
print(df.shape)

#checking the data types (dtypes are underlying types of pandas dataframe)
print('*************Data type***********')
print(df.dtypes)

#checking the dataframe head
print('*************Inspecting data head***********')
print(df.head(1))

#replacing non-numerical data in the month and day with numerical data(ENCODING)
df.month.replace(('jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec'), (1,2,3,4,5,6,7,8,9,10,11,12)
                 ,inplace=True)
df.day.replace(('mon','tue','wed','thu','fri','sat','sun'),(1,2,3,4,5,6,7),inplace=True)
print('*************Inspecting head after data replacement***********')
print(df.head(1))

#showing statistics for all columns in the data
#beware of descriptive statistics on encoded attributes like month and day
print(df.describe())

#finding the linear correlation between variables in the dataset
#linear corr of month and day doesn't make sense since its originally categorical data
print('*************correlation***********')
print(df.corr(method='pearson'))
