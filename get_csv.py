import pandas as pd


def getCsv(file):
    datos = pd.read_csv(file, sep=",", skiprows=32, usecols=[0,1])
    x = datos.iloc[:,0]
    y =  datos.iloc[:,1]

    return x,y
