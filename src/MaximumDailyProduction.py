import matplotlib.pyplot as plt
import pandas as pd

if __name__ == "__main__":
    
    dataframe = pd.read_excel("../data/Datoshistóricos-20220410015735.xls", skiprows=2)

    #Parse date
    dataframe['Hora'] = pd.to_datetime(dataframe['Hora'], format="%d/%m/%Y %H:%M:%S")

    dataframe_len = len(dataframe)
    max = 0.0
    max_array = []
    dates = []

    for index in range(dataframe_len):

        if (index + 1 < dataframe_len and 
            dataframe['Salida de hoy(kWh)'][index] > max and 
            dataframe['Salida de hoy(kWh)'][index + 1 ] == 0):

            max = dataframe['Salida de hoy(kWh)'][index]
            print(dataframe['Hora'][index],'-', max, '(kWh)')
            max_array.append(max)
            dates.append(str(dataframe['Hora'][index].strftime("%d/%m %H:%M:%S")))
            max = 0
        
        if(index + 1 == dataframe_len): # Ultimo elemento
            max = dataframe['Salida de hoy(kWh)'][index]
            print(dataframe['Hora'][index],'-', max, '(kWh)')
            max_array.append(max)
            dates.append(str(dataframe['Hora'][index].strftime("%d/%m %H:%M:%S")))
            max = 0

    fig, axs = plt.subplots(nrows=1, ncols=1, figsize=(16,8), dpi=600)

    fig.suptitle('Electricidad Asunción Esteban Fuente S.L.', fontsize=28)
    axs.bar(dates, max_array)
    axs.set_ylabel('Producción máxima (kWh)', fontsize=24)
    axs.set_xlabel('Días', fontsize=24)
    axs.set_xticklabels(dates, rotation = 70, ha = 'center', fontsize=15)
    axs.grid(True)

    for i in range(len(dates)):
        axs.text(x=dates[i], y=max_array[i] + 0.1, s=max_array[i], fontsize=20 , horizontalalignment='center')


    fig.tight_layout()
    fig.savefig("../images/MaxProductionDiaria.jpg")
