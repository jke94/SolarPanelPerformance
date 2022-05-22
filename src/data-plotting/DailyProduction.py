from datetime import datetime
import matplotlib.pyplot as plt
from numpy import void
import pandas as pd
import numpy as np

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
    axs.plot(dataframe['Date'], dataframe['DailyHistoricalAverage'], color='red', 
                linewidth=4.0)

    axs.legend(['Historical average production (kWh)', 'Max daily production (kWh)'])
    
    fig.suptitle('Solar panels production' + ' (' + str(len(dataframe)) + ' days)', fontsize=28)
    axs.set_ylabel('Maximum Production (kWh)', fontsize=24)
    axs.set_xlabel('Dates', fontsize=24)
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

    startDay    = datetime(2022, 4, 1)
    endDay      = datetime(2022, 5, 1)

    raw_df = pd.read_csv(data_dir + data_input_file, sep=';')
    raw_df['Date'] =  pd.to_datetime(raw_df['Date'], format='%Y-%m-%d %H:%M:%S')

    mask = (raw_df['Date'] > startDay) & (raw_df['Date'] <= endDay)

    df = raw_df.loc[mask]
    df['Date'] = df['Date'].dt.strftime('%d/%m/%y  %H:%M:%S')
    df.reset_index(drop=True, inplace=True)

    PlotMaxDailyProduction(df, image_dir + plot_output_image)