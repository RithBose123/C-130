import csv
import pandas as pd
df=pd.read_csv("final.csv")
del df["Luminosity"]
del df["Star_name1"]
del df["Distance1"]
del df["Mass1"]
del df["Radius1"]
print(df.shape)
df.to_csv("Actualresult.csv")