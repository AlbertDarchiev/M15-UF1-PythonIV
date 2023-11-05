import matplotlib.pyplot as plt
import numpy as np
import csv
import february_temperature as ft
#44sdsdsd
def read_csv(input_csv) -> list:
    data = []
    with open(input_csv, 'r', encoding='utf-8') as csv_file:
        reader = csv.reader(csv_file, delimiter=",")
        for row in reader:
            data.append(row)
    csv_file.close()
    return data

data1 = read_csv('Data/Metadades.csv')
data2 = read_csv('Data/Estacions.csv')
data3 = read_csv('Data/Detall_Estacions.csv')

nd_metadata =np.array(data1)
nd_estacions =np.array(data2)
nd_detall_estacions =np.array(data3)

#print(nd_metadata)
type(nd_metadata)

#print(np.shape(nd_metadata))

#print(nd_metadata) 

ft.Temperature.get_average(nd_detall_estacions)

