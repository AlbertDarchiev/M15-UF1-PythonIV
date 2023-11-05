import numpy as np
import matplotlib.pyplot as plt
from numpy import random

class Temperature:
    def get_average(data):
        x_days = []
        y_values = []
        for i in data[1:]:           
            month = str(i[0]).split("-")[1] == "02"
            avg_temp = str(i[3]) == "TM"
            if month and avg_temp:
                day = str(i[0]).split("-")[2]
                x_days.append(day)
                y_values.append(i[4])

        #plt.figure(figsize=(12, 9), )
        plt.subplot(1,2,1)
        plt.bar(x_days, y_values)
        plt.xlabel('Days')
        plt.ylabel('Average Temperature')
        plt.title("GRÀFIC 1")


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
        plt.show()


   
    
