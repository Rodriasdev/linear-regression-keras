import pandas as pd


def getCsv(file):
    datos = pd.read_csv(file, sep=",", skiprows=32, usecols=[0,1])
    x = datos.iloc[:,0].values
    y =  datos.iloc[:,1].values

    return x,y
