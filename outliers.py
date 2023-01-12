import pandas as pd
import numpy as np




#read the csv file
df = pd.read_csv('dia.csv')

#find the outliers with iqr for each column
df.sort_values("Pregnancies")
qp3=np.quantile(df['Pregnancies'], 0.75)
qp1=np.quantile(df['Pregnancies'], 0.25)
df.sort_values("Glucose")
qg3=np.quantile(df['Glucose'], 0.75)
qg1=np.quantile(df['Glucose'], 0.25)
df.sort_values("BloodPressure")
qbp3=np.quantile(df['BloodPressure'], 0.75)
qbp1=np.quantile(df['BloodPressure'], 0.25)
df.sort_values("SkinThickness")
qst3=np.quantile(df['SkinThickness'], 0.75)
qst1=np.quantile(df['SkinThickness'], 0.25)
df.sort_values("Insulin")
qi3=np.quantile(df['Insulin'], 0.75)
qi1=np.quantile(df['Insulin'], 0.25)
df.sort_values("BMI")
qbmi3=np.quantile(df['BMI'], 0.75)
qbmi1=np.quantile(df['BMI'], 0.25)
df.sort_values("DiabetesPedigreeFunction")
qdpf3=np.quantile(df['DiabetesPedigreeFunction'], 0.75)
qdpf1=np.quantile(df['DiabetesPedigreeFunction'], 0.25)
df.sort_values("Age")
qage3=np.quantile(df['Age'], 0.75)
qage1=np.quantile(df['Age'], 0.25)

iqrp=((np.quantile(df['Pregnancies'], 0.75))-(np.quantile(df['Pregnancies'], 0.25)))
iqrg=((np.quantile(df['Glucose'], 0.75))-(np.quantile(df['Glucose'], 0.25)))
iqrbp=((np.quantile(df['BloodPressure'], 0.75))-(np.quantile(df['BloodPressure'], 0.25)))
iqrst=((np.quantile(df['SkinThickness'], 0.75))-(np.quantile(df['SkinThickness'], 0.25)))
iqri=((np.quantile(df['Insulin'], 0.75))-(np.quantile(df['Insulin'], 0.25)))
iqrbmi=((np.quantile(df['BMI'], 0.75))-(np.quantile(df['BMI'], 0.25)))
iqrdpf=((np.quantile(df['DiabetesPedigreeFunction'], 0.75))-(np.quantile(df['DiabetesPedigreeFunction'], 0.25)))
iqrage=((np.quantile(df['Age'], 0.75))-(np.quantile(df['Age'], 0.25)))
print("Pregnancies iqr", iqrp)
df_filteredp = df[(df["Pregnancies"] < qp3) & (df["Pregnancies"] > qp1)]
print("Pregnancies outliers",df_filteredp)
print("Glucose",iqrg)
df_filteredg = df[(df["Glucose"] < qg3) & (df["Glucose"] > qg1)]
print("Glucose outliers",df_filteredg)
print("Blood Pressure",iqrbp)
df_filteredbp = df[(df["BloodPressure"] < qbp3) & (df["BloodPressure"] > qbp1)]
print("BloodPressure",df_filteredbp)
print("Skin Thickness",iqrst)
df_filteredst = df[(df["SkinThickness"] < qst3) & (df["SkinThickness"] > qst1)]
print("SkinThickness",df_filteredbp)
print("Insulin",iqri)
df_filteredi = df[(df["Insulin"] < qi3) & (df["Insulin"] > qi1)]
print("Insulin",df_filteredi)
print("BMI",iqrbmi)
df_filteredbmi = df[(df["BMI"] < qbmi3) & (df["BMI"] > qbmi1)]
print("BMI",df_filteredbmi)
print("Diabetes Pedigree Function",iqrdpf)
df_filtereddpf = df[(df["DiabetesPedigreeFunction"] < qdpf3) & (df["DiabetesPedigreeFunction"] > qdpf1)]
print("DiabetesPedigreeFunction",df_filtereddpf)
print("Age",iqrage)
df_filteredage = df[(df["Age"] < qage3) & (df["Age"] > qage1)]
print("Age",df_filteredbmi)

#find the column that has maximum outliers than the other column
df_dict={"Pregnancies": len(df_filteredp),
"Glucose": len(df_filteredg),
"BloodPressure": len(df_filteredbp),
"SkinThickness": len(df_filteredst),
"Insulin": len(df_filteredi),
"BMI": len(df_filteredbmi),
"DiabetesPedigreeFunction": len(df_filtereddpf),
"Age": len(df_filteredage),}
Key_max = max(df_dict, key = lambda x: df_dict[x])  
max_val = max([max(df_dict.values()) for dict in df_dict])


#print the name of the column and the number of values of the column that has maximum outliers. For example, if the first column has maximum outliers with 25, the value should be printed as 'Pregnancies 25' (without inverted comma)
print( Key_max, " " , max_val)  



