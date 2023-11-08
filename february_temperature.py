import numpy as np
import matplotlib.pyplot as plt
from numpy import random

class Temperature:
    def get_average(data):
        x_days = []
        stations = [[], [], [], []]
        counter = 0
        for i in data[1:]:
            if counter == 4:
                counter = 0
            month = str(i[0]).split("-")[1] == "02"
            avg_temp = str(i[3]) == "TM"
            if month and avg_temp:
                stations[counter].append(float(i[4]))  # Convertir a float
                day = str(i[0]).split("-")[2]
                if day not in x_days:
                    x_days.append(day)
                counter += 1

        plt.figure(figsize=(12, 6))
#plt.subplot(1, 4, i+1)
        plt.plot(x_days, stations[0], marker='o')
        plt.plot(x_days, stations[1], marker='o')
        plt.plot(x_days, stations[2], marker='o')
        plt.plot(x_days, stations[3], marker='o')

        plt.legend(['Estación 1', 'Estación 2', 'Estación 3', 'Estación 4'])
        plt.xlabel('Días de Febrero')
        plt.ylabel('Temperatura Promedio')
        #plt.title(f'Estación {i+1}')

        plt.tight_layout()
        plt.show()
"""
        #2
        plt.subplot(1, 2, 2)
        plt.bar(x_days, y_values)
        plt.xlabel('Days')
        plt.ylabel('Average Temperature')
        plt.title("GRÀFIC 2")
        return plt.show()
    
    def get_histogram(info):
        x_days = []
        y_values = []
        for i in info[1:]:           
            month = str(i[0]).split("-")[1] == "02"
            avg_temp = str(i[3]) == "TM"
            if month and avg_temp:
                day = str(i[0]).split("-")[2]
                x_days.append(day)
                y_values.append(i[4])
                
        #Mostrar histograma
        plt.hist(y_values, bins=10, range=(-10,25), color='green', histtype='bar', rwidth=0.8)
        plt.xlabel('Temperatura')
        plt.ylabel('Frecuencia')
        plt.title('Histograma temperatura mediana en Febrero')
        plt.show()
        #Mostrar grafico tiempo febrero 2023
        temperatures_random = []
        for day in range(1,29):
            temperatures_random.append(random.randint(-10,25))
        plt.plot(range(1,29), temperatures_random, color='green')
        plt.xlabel('Days')
        plt.ylabel('Temperature')
        plt.title('Temperatures in February 2023')
        plt.xticks(range(1,29))
        plt.show()


   
    
"""