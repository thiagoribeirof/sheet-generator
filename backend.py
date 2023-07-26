import pandas as pd


def createDataframe(portaria, vazao, tempoCaptacao, dataInstalacao, dataFim, frequencia):
    print(portaria, vazao, tempoCaptacao, dataInstalacao, dataFim, frequencia)
    match frequencia:
        case "DIARIO":
            freq = 'D'
        case "SEMANAL":
            freq = 'W'
        case "QUINZENAL":
            freq = '2W'
        case "MENSAL":
            freq = '4W'
    
    lista_datas = pd.date_range(start=dataInstalacao, end=dataFim, freq=freq)
    print(lista_datas)