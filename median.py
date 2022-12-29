import pandas as pd




#read csv
df = pd.read_csv('C:\\set-2---test-outliers-ShrimayiS-main\\dia.csv')
df.sort_values("Pregnancies")
#find the median of first column - Pregnancies
median1 = df['Pregnancies'].median() 

#print the value and round off to 2 decimal places

print(round(median1, 2))
