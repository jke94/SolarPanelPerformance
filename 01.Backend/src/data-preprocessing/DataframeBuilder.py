from operator import le
from model.DataFileHelperXls import DataFileHelperXls
import pandas as pd

class DataframeBuilder:
    
    files = [
        DataFileHelperXls.data_fileA,
        DataFileHelperXls.data_fileB,
        DataFileHelperXls.data_fileC,
        DataFileHelperXls.data_fileD,
        DataFileHelperXls.data_fileE,
        DataFileHelperXls.data_fileF,
        DataFileHelperXls.data_fileG,
        DataFileHelperXls.data_fileH,
        DataFileHelperXls.data_fileI,

        DataFileHelperXls.data_fileJ,
        DataFileHelperXls.data_fileK,
        DataFileHelperXls.data_fileL,
        DataFileHelperXls.data_fileM
    ]

    __df_columns = [    'Hora',                     #   1  
                        'Modo de trabajo',          #   2 
                        'V MPPT 1(V)',              #   3
                        'I MPPT 1(A)',              #   4
                        'Ua(V)',                    #   5                    
                        'I AC 1(A)',                #   6
                        'F AC 1(Hz)',               #   7
                        'Poder(W)',                 #   8
                        'Temperature(ºC)',          #   9
                        'Salida de hoy(kWh)',       #   10 
                        'Generación total(kWh)',    #   11
                        'H Total(h)',               #   12
                        'RSSI(%)'                   #   13
    ]

    def __init__(
        self, 
        data_dir, 
        csv_raw_data,
        json_raw_data):

        self.__data_dir = data_dir
        self.__csv_raw_data = csv_raw_data
        self.__json_raw_data = json_raw_data
        self.__dataframe = pd.DataFrame()
        self.__dataframes = []

        self.__createDataframeFromXlsFiles()

    def GetRawDataframe(self):

        return self.__dataframe
        
    def __createDataframeFromXlsFiles(self):
        
        for item in range(len(self.files)):
            self.__dataframes.append(
                    pd.read_excel(
                        self.__data_dir + self.files[item], skiprows=2))

        # Build a dataframe with all values (joining the differents dataframes by xls file)
        for item in range(len(self.files)):
            self.__dataframe = pd.concat(self.__dataframes, ignore_index=True)

        # Set columns.
        self.__dataframe.columns = self.__df_columns

    def to_CSV(self):
        
        self.__dataframe.to_csv(
            self.__data_dir + self.__csv_raw_data, 
            index=False, 
            sep=';', 
            encoding='utf-8-sig')

        print(f"Dataframe '{self.__csv_raw_data}' raw data: Full data (row x col): {self.__dataframe.shape}\t")

    def to_JSON(self):
        
        self.__dataframe.to_json(
            self.__data_dir + self.__json_raw_data, 
            orient='records',
            indent=4
        )

        print(f"Dataframe '{self.__json_raw_data}' raw data: Full data (row x col): {self.__dataframe.shape}\t")