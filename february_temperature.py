import numpy as np
import matplotlib.pyplot as plt

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
        plt.plot(x_days, stations[0], marker='o')
        plt.plot(x_days, stations[1], marker='o')
        plt.plot(x_days, stations[2], marker='o')
        plt.plot(x_days, stations[3], marker='o')

        plt.legend(['Estación 1', 'Estación 2', 'Estación 3', 'Estación 4'])
        plt.xlabel('Días de Febrero')
        plt.ylabel('Temperatura Promedio')
        plt.title('Ex3 - Temperatura promedio de Febrero 2022')
        plt.tight_layout()
        plt.show()
    
    def get_histogram(data):
        x_days = []
        y_values = []
        for i in data[1:]:           
            month = str(i[0]).split("-")[1] == "02"
            avg_temp = str(i[3]) == "TM"
            if month and avg_temp:
                day = str(i[0]).split("-")[2]
                x_days.append(day)
                y_values.append(i[4])

        tempss = [float(hvaluetransf) for hvaluetransf in y_values]
        rangestemp = (-10, 25)
        plt.figure(figsize=(12,6))
        plt.hist(tempss, bins=20, range=rangestemp)
        plt.xlabel('Temperatura')
        plt.ylabel('Frecuencia')
        plt.title('Ex4.1 - Histograma de Temperaturas Febrero 2022')        
        
        convertlist = [float(valuetransf) for valuetransf in y_values]
        media = np.mean(convertlist)
        future_temps = np.random.normal(media,5.0,size=28)


        plt.figure(figsize=(12,6))
        plt.plot(range(1,29), future_temps)
        plt.xlabel('Días Febrero')
        plt.ylabel('Temperatura')
        plt.title('Ex4.2 - Histograma de Temperaturas Febrero 2022')
        plt.xticks(range(1,29))
        
        plt.show()

    def rain_predict(data):
        x_days = []
        rainy_days = []
        ppt_data = []
        for row in data[1:]:
            if len(ppt_data) == 3:
                if np.mean(ppt_data) > 0:
                    rainy_days.append(True)
                else:
                    rainy_days.append(False)
                ppt_data = []
            month = str(row[0]).split("-")[1] == "02"
            avg_temp = str(row[3]) == "PPT"
            if month and avg_temp:
                ppt_data.append(float(row[4]))
                day = str(row[0]).split("-")[2] 
                if day not in x_days:
                    x_days.append(day)
        
        rainy_days = np.array(rainy_days)
        plt.figure(figsize=(15, 6))
        plt.bar(x_days, rainy_days, color=['yellow' if rain else 'red' for rain in rainy_days])
        plt.xlabel('Días Febrero')
        plt.title('Ex5.1 - Predicción de lluvia de Febrero 2023')
        plt.yticks([0, 1], ['No llueve', 'Llueve'])
        plt.xticks(x_days)
        plt.show()

        y_values = [sum(rainy_days), len(rainy_days) - sum(rainy_days)]
        plt.figure(figsize=(8, 8))
        plt.pie(y_values, 
                explode=(0.1, 0), 
                labels=['Llueve', 'No llueve'], 
                colors=['yellow', 'orange'],
                autopct='%1.1f%%')
        plt.title('Ex5.2 - Predicción de lluvia de Febrero 2023')
        plt.show()
