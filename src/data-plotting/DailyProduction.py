from datetime import datetime
from turtle import color
import matplotlib.pyplot as plt
from numpy import void
import pandas as pd
import numpy as np

def GetDailyAverage(array_dailyProduction):
    '''
        Calculate daily average production date (kWh).

        Parameters
        ----------
        array: Array with the daily production values.

        return: Array with the average.
    
    '''

    dailyAverage = []
    index = 0

    for index in range(len(array_dailyProduction)):
        dailyAverage.append(round(np.mean(array_dailyProduction[:index + 1]),2))

    return dailyAverage

def PlotMaxDailyProduction(dataframe, fileOutput) -> void:
    
    '''
        Plot and save as an image the maximum daily production date (kWh).

        Parameters
        ----------
        dataframe: DataFrame with the maximum daily production date.

        fileOutput: Path plus name of the file to save it.
    
    '''

    # Crete figure
    fig, axs = plt.subplots(nrows=1, ncols=1, figsize=(16,8), dpi=600)

    # Set plot bar for daily production.
    axs.bar(dataframe['Date'], dataframe['MaxDailyProduction'], color='royalblue')

    # Set plot line for daily historical average production.
    axs.plot(dataframe['Date'], dataframe['DailyHistoricalAverage'], color='red', linewidth=4.0)

    # Set plot line for daily average production.
    axs.plot(dataframe['Date'], GetDailyAverage(dataframe['MaxDailyProduction']), color='darkorange', linewidth=4.0)
    
    axs.legend(['Historical average production (kWh)', 'Daily average production (kWh)','Production (kWh)'],
        bbox_to_anchor=(0.4,1.01,1,0.2), loc="upper left")
    
    fig.suptitle('Solar panels production' + 
        ' - Total: ' + str(round(sum(dataframe['MaxDailyProduction']),2)) + 
        ' kWh - Date average: ' + str(round(np.mean(dataframe['MaxDailyProduction']),2)) + ' kWh',
        fontsize=24)


    axs.set_ylabel('Maximum Production (kWh)', fontsize=24)
    axs.set_xlabel('Dates' + ' (' + str(len(dataframe)) + ' days)', fontsize=24)
    axs.set_xticklabels(dataframe['Date'], rotation = 70, ha = 'center', fontsize=10)
    axs.grid(True)

    print(dataframe)

    for i in range(len(dataframe['Date'])):
        axs.text(   x=dataframe['Date'][i], 
                    y=dataframe['MaxDailyProduction'][i] + 0.1, 
                    s=dataframe['MaxDailyProduction'][i], 
                    fontsize=8, 
                    horizontalalignment='center')

    fig.tight_layout()
    fig.savefig(fileOutput)

if __name__ == "__main__":
    
    data_dir = "./data/"
    image_dir = "./images/"

    data_input_file = "SolarPanel-MaxDailyProduction.csv"
    plot_output_image = "DailyProduction.jpg"

    startDay    = datetime(2022, 5, 1)
    endDay      = datetime(2022, 6, 1)

    raw_df = pd.read_csv(data_dir + data_input_file, sep=';')
    raw_df['Date'] =  pd.to_datetime(raw_df['Date'], format='%Y-%m-%d %H:%M:%S')

    mask = (raw_df['Date'] > startDay) & (raw_df['Date'] <= endDay)

    df = raw_df.loc[mask]
    df['Date'] = df['Date'].dt.strftime('%d/%m/%y  %H:%M:%S')
    df.reset_index(drop=True, inplace=True)

    PlotMaxDailyProduction(df, image_dir + plot_output_image)