import pandas as pd

if __name__ == "__main__":

    data = "./01.Backend/data/SolarPanel-RawData.csv"

    raw_df = pd.read_csv(data, sep=';')

    # Examples, extract custom data
    print(raw_df.loc[raw_df['Poder(W)'] > 2220][['Hora','Poder(W)']])
    print(raw_df.loc[raw_df['Temperature(ºC)'] > 54.4][['Hora','Temperature(ºC)']])