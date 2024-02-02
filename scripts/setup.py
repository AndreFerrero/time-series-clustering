import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

script_path = os.getcwd()
path = os.path.dirname(script_path)

def import_data(path):
    data = R'data'
    data_path = os.path.join(path, data)
    
    # List all files in the folder
    csv_files = [file for file in os.listdir(data_path) if file.endswith(".csv") if file != 'InfoComune.csv']

    # Create an empty dictionary to store DataFrames
    dataframes = {}

    # Iterate through each CSV file
    for file in csv_files:
        # Extract the file name
        df_name = os.path.splitext(file)[0]
        
        # Create the DataFrame and store it in the dictionary
        dataframes[df_name] = pd.read_csv(os.path.join(data_path, file), header=0, skiprows = [1])
        
    return dataframes


dataframes = import_data(path)

# store dictionary items in specific variables to make it easier to loop through them
datasets = dataframes.values()
provinces = dataframes.keys()
data_prov_pairs = dataframes.items()

# columns to keep the average value only
pollutants = ['CO', 'NH3', 'NMVOC', 'NO2', 'NO', 'O3', 'PANS', 'PM10', 'PM2.5', 'SO2']

# metereological information
met = ['TG', 'TN', 'TX', 'HU', 'PP', 'QQ', 'RR']
met_pos = range(6, 13)
# date values
date = ['YYYY', 'MM', 'DD']
date_pos = list(range(3))

selected_columns = date + met + pollutants

numerics = met + pollutants

def clean_data(data):
    for province, df in data_prov_pairs:
        # change missing values to the proper format
        df.replace('---', np.nan, inplace = True)
        # ensure a unique format
        df = df.convert_dtypes()

        # rename the columns for date and metereological information
        old_date = df.columns[date_pos]
        old_met = df.columns[met_pos]
        
        df.rename(columns=dict(zip(old_date, date)), inplace=True)
        df.rename(columns=dict(zip(old_met, met)), inplace=True)
                
        df = df[selected_columns]

        # Combine 'YYYY', 'MM', 'DD' columns into a new 'date' column
        df['date'] = pd.to_datetime(df[['YYYY', 'MM', 'DD']].astype(str).agg('-'.join, axis=1), format='%Y-%m-%d')
        
        # Remove 'YYYY', 'MM', 'DD' columns
        df.drop(['YYYY', 'MM', 'DD'], axis=1, inplace=True)
                
        # Reorder columns with 'date' as the first column
        df = df[['date'] + [col for col in df.columns if col != 'date']]
        
        # first convert to numeric the columns in met and pollutants, since they are strings
        df[numerics] = df[numerics].apply(pd.to_numeric, errors = 'coerce')
        # round to the second decimal number for better visualization
        df[numerics] = df[numerics].round(2)
        
        # we want to filter the series so that we don't have missing values
        # We'll start from 2018-01-01 and move until 2020-12-28

        df = df[(df['date'] >= pd.to_datetime('2018-01-01')) & (df['date'] <= pd.to_datetime('2020-12-28'))]
        
        dataframes[province] = df

    return dataframes

dataframes = clean_data(dataframes)


        
