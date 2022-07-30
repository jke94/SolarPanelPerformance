from matplotlib import collections
import matplotlib.pyplot as plt
from numpy import void
import pandas as pd

from regex import D

if __name__ == "__main__":

    data_dir = "../data/"
    data_file = "Datoshistóricos-20220410015735.xls"

    raw_df = pd.read_excel(data_dir + data_file, skiprows=2)

    data = raw_df['Poder(W)']

    print("From: 17/03/22 to 10/04/22")
    print(raw_df[raw_df["Poder(W)"] > 2000][['Hora', 'Poder(W)']])