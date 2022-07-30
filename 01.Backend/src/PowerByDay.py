
import matplotlib.pyplot as plt
from numpy import void
import pandas as pd
import datetime

def PlotPowerDay(dataframe, fileOutput) -> void:
    
    '''
        Plot and save as an image the daily production (kWh).

        Parameters
        ----------
        dataframe: DataFrame with the production durin the day.

        fileOutput: Path plus name of the file to save it.
    
    '''
    # Select X and Y datas.
    start = dataframe['Hora'].iloc[0].strftime("%d/%m/%y %H:%M:%S")
    end = dataframe['Hora'].iloc[len(dataframe)-1].strftime("%d/%m/%y %H:%M:%S")

    # Create plot.
    fig, axs = plt.subplots(nrows=2, ncols=1, figsize=(40,16), dpi=600)
    fig.suptitle('Power (W) & Temeperature (ºC)' +
                     ' ( ' + start + ' - ' + end + ' )',  fontsize=28)

    # Subplot 0, rirst row.
    axs[0].plot(dataframe['Hora'], dataframe['Poder(W)'], 
                color='black', 
                linewidth=2.0)
    axs[0].legend(['Power (W)'], fontsize=20)
    axs[0].get_xaxis().set_visible(False)
    axs[0].set_ylabel('Maximum Production (kWh)', fontsize=24)
    axs[0].set_xlabel('Dates', fontsize=24)
    axs[0].tick_params(axis='both', which='major', labelsize=20)
    axs[0].grid(True)

    # Subplot 1, second row.
    axs[1].plot(dataframe['Hora'], dataframe['Temperatura(℃)'], 
                color='red', linewidth=2.0)
    axs[1].legend(['Temperature (ºC)'], fontsize=20)
    axs[1].get_xaxis().set_visible(False)
    axs[1].set_ylabel('Temperature (ºC)', fontsize=24)
    axs[1].set_xlabel('Dates', fontsize=24)
    axs[1].tick_params(axis='both', which='major', labelsize=20)
    axs[1].grid(True)

    # Fix the plot and save as a image.
    fig.tight_layout()
    fig.savefig(fileOutput + date.strftime("%d-%m-%Y") + ".jpg")


if __name__ == "__main__":

    data_dir = "../data/"
    data_file = "PowerTemperature-13-03-17-04.xls"

    # USER: Select the day
    date = datetime.datetime(year=2022, month=4, day=7)

    raw_df = pd.read_excel(data_dir + data_file, skiprows=2)

    # Preprocessing (Parse date)
    raw_df['Hora'] = pd.to_datetime(raw_df['Hora'], format="%d/%m/%Y %H:%M:%S")

    # Select range of dates (one day, or more days.)
    df = raw_df[raw_df['Hora'].between(date, date + datetime.timedelta(days=1))]
    
    # Plot Dataframe
    PlotPowerDay(dataframe=df, fileOutput="../images/PowerByDay-")