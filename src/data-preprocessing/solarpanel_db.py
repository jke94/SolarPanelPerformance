'''
In the web: 
        1. Select all features to be extracted.
        2. Select de range of dates (two options):
                2.1. From day 1 until day 16  like range of date.
                       Example: 1th March until 16th March (both includes)
                2.2.  From day 16 until day 1 (next month) like range of date.
                        Example: 16th March until 1th April (both includes).
        3. Update the script to generate the data.

'''
import pandas as pd
from numpy import void
import numpy as np

def GetMaxDailyProduction(df_raw) -> pd.DataFrame:
    '''
    Algorithm to extract the maximum daily production (kWh).

    Parameters
    ----------
    df_raw: DataFrame with raw data to extract.

    Returns
    -------
    pd.DataFrame

    '''

    # Preprocessing (Parse date)
    df_raw['Hora'] = pd.to_datetime(df_raw['Hora'], format="%d/%m/%Y %H:%M:%S")

    cols = ['Date', 'MaxDailyProduction', 'DailyHistoricalAverage','MaxPoder','MaxPoderTime']
    df = pd.DataFrame(columns=cols)

    df_raw_len = len(df_raw)
    max = 0.0
    max_array = []
    dates = []
    daily_average = []

    max_poder = 0
    max_poder_array = []

    max_poder_time = 0
    max_poder_time_array = []

    # Extract maximum daily production
    for index in range(df_raw_len):

        if (index + 1 < df_raw_len and 
            df_raw['Salida de hoy(kWh)'][index] > max and 
            df_raw['Salida de hoy(kWh)'][index + 1 ] == 0): 

            # We have the daily maximum!
            max = df_raw['Salida de hoy(kWh)'][index]
            max_array.append(max)
            dates.append(str(df_raw['Hora'][index].strftime("%Y-%m-%d %H:%M:%S")))
            max = 0

            max_poder_array.append(max_poder)
            max_poder = 0

            max_poder_time_array.append(max_poder_time)
            max_poder_time = 0

        if(index + 1 == df_raw_len): # Last elemento
            max = df_raw['Salida de hoy(kWh)'][index]
            max_array.append(max)
            dates.append(str(df_raw['Hora'][index].strftime("%Y-%m-%d %H:%M:%S")))
            max = 0

            max_poder_array.append(max_poder)
            max_poder = 0

            max_poder_time_array.append(max_poder_time)
            max_poder_time = 0

        if(df_raw['Poder(W)'][index] > max_poder):
                max_poder = df_raw['Poder(W)'][index]
                max_poder_time = df_raw['Hora'][index].strftime("%H:%M:%S")
                

    # Extract daily average
    index = 0
    for index in range(len(max_array)):
        daily_average.append(round(np.mean(max_array[:index + 1]),2))

                
    df['Date'] = dates
    df['MaxDailyProduction'] = max_array
    df['DailyHistoricalAverage'] = daily_average
    df['MaxPoder'] = max_poder_array
    df['MaxPoderTime'] = max_poder_time_array

    return df


if __name__ == "__main__":

    data_dir = "./data/"
    csv_raw_data = "SolarPanel-RawData.csv"
    csv_max_daily_production_csv = "SolarPanel-MaxDailyProduction.csv"
    csv_max_daily_production_json = "SolarPanel-MaxDailyProduction.json"

    data_fileA = "SolarPanel-03-March-1-of-1-FullFeatures.xls"
    data_fileB = "SolarPanel-04-April-1-of-2-FullFeatures.xls"
    data_fileC = "SolarPanel-04-April-2-of-2-FullFeatures.xls"
    data_fileD = "SolarPanel-05-May-1-of-2-FullFeatures.xls"
    data_fileE = "SolarPanel-05-May-2-of-2-FullFeatures.xls"
    data_fileF = "SolarPanel-06-June-1-of-2-FullFeatures.xls"
    data_fileG = "SolarPanel-06-June-2-of-2-FullFeatures.xls"
    data_fileH = "SolarPanel-07-July-1-of-2-FullFeatures.xls"
    data_fileI = "SolarPanel-07-July-2-of-2-FullFeatures.xls"

    dataframeA = pd.read_excel(data_dir + data_fileA, skiprows=2)
    dataframeB = pd.read_excel(data_dir + data_fileB, skiprows=2)
    dataframeC = pd.read_excel(data_dir + data_fileC, skiprows=2)
    dataframeD = pd.read_excel(data_dir + data_fileD, skiprows=2)
    dataframeE = pd.read_excel(data_dir + data_fileE, skiprows=2)
    dataframeF = pd.read_excel(data_dir + data_fileF, skiprows=2)
    dataframeG = pd.read_excel(data_dir + data_fileG, skiprows=2)
    dataframeH = pd.read_excel(data_dir + data_fileH, skiprows=2)
    dataframeI = pd.read_excel(data_dir + data_fileI, skiprows=2)


    df_columns = [  'Hora', 'Modo de trabajo', 'V MPPT 1(V)', 'I MPPT 1(A)', 'Ua(V)',
                    'I AC 1(A)', 'F AC 1(Hz)', 'Poder(W)', 'Temperatura(℃)',
                    'Salida de hoy(kWh)', 'Generación total(kWh)', 'H Total(h)', 'RSSI(%)']

    # Rename columns
    df_columns = [item.replace('Temperatura(℃)', 'Temperature(ºC)') for item in df_columns]

    dataframe = pd.concat(
        [       dataframeA, # "SolarPanel-03-March-1-of-1-FullFeatures.xls"
                dataframeB, # "SolarPanel-04-April-1-of-2-FullFeatures.xls"
                dataframeC, # "SolarPanel-04-April-2-of-2-FullFeatures.xls"
                dataframeD, # "SolarPanel-05-May-1-of-2-FullFeatures.xls"
                dataframeE, # "SolarPanel-05-May-2-of-2-FullFeatures.xls"
                dataframeF, # "SolarPanel-06-June-1-of-2-FullFeatures.xls"
                dataframeG, # "SolarPanel-06-June-2-of-2-FullFeatures.xls"
                dataframeH, # "SolarPanel-07-July-1-of-2-FullFeatures.xls"
                dataframeI  # "SolarPanel-07-July-2-of-2-FullFeatures.xls"
        ])
    dataframe.columns = df_columns


    dataframe.to_csv(
            data_dir + csv_raw_data, 
            index=False, 
            sep=';', 
            encoding='utf-8-sig')

    print("Dataframe 1: Full data (row x col):\t", dataframe.shape)
            
    dataframe = pd.read_csv(data_dir + csv_raw_data, sep=';')

    df_MaxDailyProduction = GetMaxDailyProduction(dataframe)

    df_MaxDailyProduction.to_csv(
            data_dir + csv_max_daily_production_csv, 
            index=False, 
            sep=';', 
            encoding='utf-8-sig')

    df_MaxDailyProduction.to_json(
        data_dir + csv_max_daily_production_json,
        orient="index",
        indent=4
    )

    print("Dataframe 2: Daily Prod. (row x col):\t", df_MaxDailyProduction.shape)