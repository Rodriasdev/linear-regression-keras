import csv
def getCsv(file):
    with open(file, newline='') as archivo:
        lector_csv= csv.reader(archivo, delimiter=',', quotechar='"')
        alturas=[]
        pesos=[]


        for row in lector_csv:
            altura=row[0]
            peso=row[1]

            if altura != "Altura":
                alturas.append(altura)
                pesos.append(peso)


        return alturas,pesos

