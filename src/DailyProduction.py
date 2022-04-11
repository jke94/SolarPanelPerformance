import matplotlib.pyplot as plt
from numpy import void
import pandas as pd
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
    raw_df['Hora'] = pd.to_datetime(raw_df['Hora'], format="%d/%m/%Y %H:%M:%S")

    cols = ['Date', 'MaxDailyProduction', 'DailyAverage']
    dataframe = pd.DataFrame(columns=cols)
    
    df_raw_len = len(df_raw)
    max = 0.0
    max_array = []
    dates = []
    daily_average = []

    # Extract maximum daily production
    for index in range(df_raw_len):

        if (index + 1 < df_raw_len and 
            df_raw['Salida de hoy(kWh)'][index] > max and 
            df_raw['Salida de hoy(kWh)'][index + 1 ] == 0): 

            # We have the daily maximum!
            max = df_raw['Salida de hoy(kWh)'][index]
            max_array.append(max)
            dates.append(str(df_raw['Hora'][index].strftime("%d/%m/%y %H:%M:%S")))
            max = 0
        
        if(index + 1 == df_raw_len): # Last elemento
            max = df_raw['Salida de hoy(kWh)'][index]
            max_array.append(max)
            dates.append(str(df_raw['Hora'][index].strftime("%d/%m/%y %H:%M:%S")))
            max = 0
    
    # Extract daily average
    for index in range(len(dates)):
        daily_average.append(np.mean(max_array[0:index])) 


    dataframe['Date'] = dates
    dataframe['MaxDailyProduction'] = max_array
    dataframe['DailyAverage'] = daily_average

    return dataframe

def PlotMaxDailyProduction(dataframe, fileOutput) -> void:
    
    '''
        Plot and save as an image the maximum daily production date (kWh).

        Parameters
        ----------
        dataframe: DataFrame with the maximum daily production date.

        fileOutput: Path plus name of the file to save it.
    
    '''

    fig, axs = plt.subplots(nrows=1, ncols=1, figsize=(16,8), dpi=600)

    axs.bar(dataframe['Date'], dataframe['MaxDailyProduction'])
    axs.plot(dataframe['Date'], dataframe['DailyAverage'], color='red', 
                linewidth=4.0)

    axs.legend(['Daily average (kWh)', 'Max daily production (kWh)'])
    
    fig.suptitle('Solar panels production', fontsize=28)
    axs.set_ylabel('Maximum Production (kWh)', fontsize=24)
    axs.set_xlabel('Dates', fontsize=24)
    axs.set_xticklabels(dataframe['Date'], rotation = 70, ha = 'center', fontsize=15)
    axs.grid(True)

    for i in range(len(dataframe['Date'])):
        axs.text(   x=dataframe['Date'][i], 
                    y=dataframe['MaxDailyProduction'][i] + 0.1, 
                    s=dataframe['MaxDailyProduction'][i], 
                    fontsize=20 , 
                    horizontalalignment='center')

    fig.tight_layout()
    fig.savefig(fileOutput)

if __name__ == "__main__":
    
    data_dir = "../data/"
    data_file = "Datos históricos-20220412002558.xls"

    raw_df = pd.read_excel(data_dir + data_file, skiprows=2)

    df_MaxDailyPro = GetMaxDailyProduction(raw_df)
    print(df_MaxDailyPro)
    print(df_MaxDailyPro.describe())

    PlotMaxDailyProduction(df_MaxDailyPro, "../images/MaxProductionDiaria.jpg")