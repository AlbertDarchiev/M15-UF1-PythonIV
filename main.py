import matplotlib.pyplot as plt
import numpy as np
import csv
import february_temperature as ft

def read_csv(input_csv) -> list:
    data = []
    with open(input_csv, 'r', encoding='utf-8') as csv_file:
        reader = csv.reader(csv_file, delimiter=",")
        for row in reader:
            data.append(row)
    csv_file.close()
    return data


data1 = read_csv("Data/Metadades.csv")
data2 = read_csv('Data/Estacions.csv')
data3 = read_csv('Data/Detall_Estacions.csv')

nd_metadata =np.array(data1)
nd_estacions =np.array(data2)
nd_detall_estacions =np.array(data3)

# EXERCICI 3
ft.Temperature.get_average(nd_detall_estacions)

# EXERCICI 4 Y 4.1
ft.Temperature.get_histogram(nd_detall_estacions)

# EXERCICI 5
ft.Temperature.rain_predict(nd_detall_estacions)



