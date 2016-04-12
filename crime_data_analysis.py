import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def read_csvdataset():
    #Read_CSV with column_names
    crime_data=pd.read_csv(r"D:\PPD_Crime_Incidents_2012-2014.csv",names=['District','PSA','Dispatch_Date','DC_number','Location','UCR_Code','Crime_Category','Co_ordinates'])
    #Creating DataFrame of crime_data
    df=pd.DataFrame(crime_data)
    return df

#function to visualize count by crime category
def count_by_crime_category(df):
    df['Crime_Category'].value_counts().sort_values(ascending=True).plot(kind='barh')
    plt.title("Data Representation Of Crime By Category")
    plt.ylabel('Crime Category')
    plt.xlabel('Number of Crimes per category')
    plt.show()

#function to visualize count by crime location
def count_by_crime_location(df):
    #top 20 locations with higher crimes
    fracs=[x for x in df['Location'].value_counts().sort_values(ascending=False).head(20)]
    df['Location'].value_counts().sort_values(ascending=False).head(20).plot(kind='barh').plot()
    plt.title("Data Representation Of Crime By Location : Areas more prone to crimes")
    plt.show()

    # bottom 20 location with less crimes
    df['Location'].value_counts().sort_values(ascending=False).tail(20).plot(kind='pie')
    plt.title("Data Representation Of Crime By Location : Areas less prone to crime")
    plt.show()


df=read_csvdataset()
print(df['Location'].value_counts().min(),df['Location'].value_counts().sort_values(ascending=True))
count_by_crime_category(df)
count_by_crime_location(df)
