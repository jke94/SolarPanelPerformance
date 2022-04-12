import pandas as pd

nombres = [
        'Morla de la Valdería',
        'Nogarejas',
        'Castrocalbón',
        'Corporales',
        'Truchillas']

temperatura = [
        'http://www.saihduero.es/risr/EA089/historico/xATRUFURflDOwEUR', # Morla de la Valdería
        'http://www.saihduero.es/risr/PL283/historico/xATRUFURfNDOywEU', # Nogarejas
        'http://www.saihduero.es/risr/PL284/historico/xATRUFURfRDOywEU', # Castrocalbón
        'http://www.saihduero.es/risr/PL282/historico/xATRUFURfJDOywEU', # Corporales
        'http://www.saihduero.es/risr/PL281/historico/xATRUFURfFDOywEU'  # Truchillas
]

publiometria = [
        'http://www.saihduero.es/risr/EA089/historico/xADTQNURflDOwEUR', # Morla de la Valdería
        'http://www.saihduero.es/risr/PL283/historico/xADTQNURfNDOywEU', # Nogarejas
        'http://www.saihduero.es/risr/PL284/historico/xADTQNURfRDOywEU', # Castrocalbón
        'http://www.saihduero.es/risr/PL282/historico/xADTQNURfJDOywEU', # Corporales
        'http://www.saihduero.es/risr/PL281/historico/xADTQNURfFDOywEU'  # Truchillas
]

for index in range(len(publiometria)):

        print("Data from: ", nombres[index])
        dataframes = pd.read_html(publiometria[index],
                decimal=',',thousands='.') # Three dataframes.
        print(dataframes[0].describe())
