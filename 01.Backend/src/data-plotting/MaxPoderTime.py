from datetime import datetime
from turtle import color
import matplotlib.pyplot as plt
from numpy import void
import pandas as pd
import numpy as np

import time
if __name__ == "__main__":
    
    data_dir = "./01.Backend/data/"
    image_dir = "./01.Backend/images/"

    data_input_file = "SolarPanel-MaxDailyProduction.csv"
    plot_output_image = "MaxPoderTime.jpg"

    now = datetime.now()

    startDay    = datetime(2022, 5, 1)
    endDay      = datetime(2022, 7, 1)

    raw_df = pd.read_csv(data_dir + data_input_file, sep=';')
    raw_df['Date'] =  pd.to_datetime(raw_df['Date'], format='%Y-%m-%d %H:%M:%S')

    mask = (raw_df['Date'] > startDay) & (raw_df['Date'] <= endDay)

    df = raw_df.loc[mask]
    df['Date'] = df['Date'].dt.strftime('%d/%m/%y  %H:%M:%S')
    df.reset_index(drop=True, inplace=True)

    plotTittle = 'Daily peak production (Generation Time: ' \
    + str(now.strftime("%d/%m/%y, %H:%M:%S")) + ') ' + 'Author: @JaviKarra94'

    x = np.array(df['Date'])
    y = np.array(df['MaxPoder'])
    
    fig, axs = plt.subplots(nrows=1, ncols=1, figsize=(16,8), dpi=600)
    fig.suptitle(plotTittle, fontsize=16)
    axs.set_xlabel('Dates: From ' + str(startDay.strftime("%d/%m/%y")) + ' to ' + str(endDay.strftime("%d/%m/%y")) +')', fontsize=24)
    axs.set_ylabel('Maximum peak (kWh)', fontsize=24)

    axs.scatter(x, y, linewidth=4.0, color='darkorange')

    axs.set_xticklabels(x, rotation = 90, ha = 'center', fontsize=10)
    axs.grid(True)

    fig.tight_layout()
    fig.savefig(image_dir + plot_output_image)