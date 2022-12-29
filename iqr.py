import pandas as pd
import numpy as np



#read the csv file
df = pd.read_csv('C:\\set-2---test-outliers-ShrimayiS-main\\dia.csv')


#find the first quantile and third quantile
Q3 = np.quantile(df['Pregnancies'], 0.75)
Q1 = np.quantile(df['Pregnancies'], 0.25)
print(Q1)
print(Q3)

#find iqr
IQR = Q3 - Q1
print(IQR)
#round off iqr to two decimal places
print(round(IQR, 3))
