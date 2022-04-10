
from turtle import color
import matplotlib.pyplot as plt
from numpy import void
import pandas as pd
import numpy as np
import datetime

if __name__ == "__main__":

    data_dir = "../data/"
    data_file = "Datoshistóricos-20220410015735.xls"

    raw_df = pd.read_excel(data_dir + data_file, skiprows=2)

    # Preprocessing (Parse date)
    raw_df['Hora'] = pd.to_datetime(raw_df['Hora'], format="%d/%m/%Y %H:%M:%S")

    date = datetime.datetime(2022, 4, 5)

    dataframe = raw_df[raw_df['Hora'].between(date, date + datetime.timedelta(days=1))]
    
    start = dataframe['Hora'].iloc[0].strftime("%d/%m/%y %H:%M:%S")
    end = dataframe['Hora'].iloc[len(dataframe)-1].strftime("%d/%m/%y %H:%M:%S")

    fig, axs = plt.subplots(nrows=2, ncols=1, figsize=(40,16), dpi=600)
    fig.suptitle('Power (W) & Temeperature (ºC)' +
                     ' ( ' + start + ' - ' + end + ' )',  fontsize=28)

    axs[0].plot(dataframe['Hora'], dataframe['Poder(W)'], color='black', 
                linewidth=2.0)
    axs[0].legend(['Power (W)'], fontsize=20)
    axs[0].get_xaxis().set_visible(False)
    axs[0].set_ylabel('Maximum Production (kWh)', fontsize=24)
    axs[0].set_xlabel('Dates', fontsize=24)
    axs[0].tick_params(axis='both', which='major', labelsize=20)
    axs[0].grid(True)

    axs[1].grid(True)
    axs[1].plot(dataframe['Hora'], dataframe['Temperatura(℃)'], 
                color='red', linewidth=2.0)
    axs[1].legend(['Temperature (ºC)'], fontsize=20)
    axs[1].get_xaxis().set_visible(False)
    axs[1].set_xlabel('Dates', fontsize=24)
    axs[1].tick_params(axis='both', which='major', labelsize=20)
    axs[1].set_ylabel('Temperature (ºC)', fontsize=24)

    fig.tight_layout()
    fig.savefig("../images/PowerByDay-" + date.strftime("%d-%m-%Y") + ".jpg")
