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
from sqlalchemy import create_engine
from sqlalchemy.types import Integer
import DataframeBuilder as dfbuiler

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

        # TODO: Improve the if sentence
        if (
            (index + 1 < df_raw_len) 
            and 
            (
                (df_raw['Salida de hoy(kWh)'][index] > max and df_raw['Salida de hoy(kWh)'][index + 1 ] == 0)
                or 
                ((df_raw['Hora'][index + 1] - df_raw['Hora'][index]).days > 0) # Lost data.
            )):
        
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

    data_dir = "./01.Backend/data/"
    csv_raw_data = "SolarPanel-RawData.csv"
    json_raw_data = "SolarPanel-RawData.json"
    max_daily_production_csv = "SolarPanel-MaxDailyProduction.csv"
    max_daily_production_json = "SolarPanel-MaxDailyProduction.json"


    dfb = dfbuiler.DataframeBuilder(
        data_dir = data_dir,
        csv_raw_data = "SolarPanel-RawData.csv",
        json_raw_data = "SolarPanel-RawData.json"
    )

    dfb.to_CSV()

    dataframe = dfb.GetRawDataframe()

    df_MaxDailyProduction = GetMaxDailyProduction(dataframe)

    df_MaxDailyProduction.to_csv(
            data_dir + max_daily_production_csv, 
            index=False, 
            sep=';', 
            encoding='utf-8-sig')
    
    df_MaxDailyProduction.to_json(
        data_dir + max_daily_production_json,
        orient='records',
        indent=4
    )

    print("Dataframe 2 to CSV: Daily Prod. (row x col):\t", df_MaxDailyProduction.shape)

    # Save as Sqlite database
    engineA = create_engine('sqlite:///.\\01.Backend\data\SolarPanel-MaxDailyProduction.db', echo=False)
    rowcountA = df_MaxDailyProduction.to_sql('SolarPanel-MaxDailyProduction.db',con=engineA, index=False, if_exists='replace')
    engineA.dispose()
    print("Created.. SolarPanel-MaxDailyProduction.db:\t", rowcountA, "rows")

    # Save as Sqlite database
    engineB = create_engine('sqlite:///.\\01.Backend\data\SolarPanel-RawData.db', echo=False)
    rowcountB = dataframe.to_sql('SolarPanel-RawData.db',con=engineB, index=False, if_exists='replace')
    engineB.dispose()
    print("Created... SolarPanel-RawData.db:\t", rowcountB, "rows")
