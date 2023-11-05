import numpy as np
import matplotlib.pyplot as plt

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
        plt.subplot(1,2,2)
        plt.barh(x_days, y_values)
        plt.title("GRÀFIC 2")
        
        
        return plt.show()
