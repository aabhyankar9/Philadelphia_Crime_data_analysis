import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def read_csvdataset():
    #Read_CSV with column_names
    crime_data=pd.read_csv(r"D:\PPD_Crime_Incidents_2012-2014.csv",names=['District','PSA','Dispatch_Date','DC_number','Location','UCR_Code','Crime_Category','Co_ordinates'])
    #Creating DataFrame of crime_data
    df=pd.DataFrame(crime_data)
    return df

def count_by_crime_category(df):
    df['Crime_Category'].value_counts().sort_values(ascending=True).plot(kind='barh')
    plt.title("Data Representation Of Crime By Category")
    plt.ylabel('Crime Category')
    plt.xlabel('Number of Crimes per category')
    plt.show()

df=read_csvdataset()
count_by_crime_category(df)
