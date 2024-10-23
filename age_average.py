import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import statistics
import matplotlib.pyplot as plt

data = pd.read_csv("data\Mall_Customers.csv")

age = data["Age"]
spent_score = data["Spending Score (1-100)"]
print(spent_score)

male = []
female =  []
teens_female = []
teens_male = []
mature_female =[]
mature_male = []
old_male = []
old_female = []

for i in range(1,len(data)):
    if data.iloc[i]["Genre"] == "Male":
        male.append(data.iloc[i]["Age"])
        if data.iloc[i]["Age"] <= 20:
            teens_male.append(data.iloc[i])
        elif data.iloc[i]["Age"] > 20 and data.iloc[i]["Age"] < 50:
             mature_male.append(data.iloc[i])
        else:
            old_male.append(data.iloc[i])
    else:
        female.append(data.iloc[i]["Age"])
        if data.iloc[i]["Age"] <= 20:
            teens_female.append(data.iloc[i])
        elif data.iloc[i]["Age"] > 20 and data.iloc[i]["Age"] < 50:
             mature_female.append(data.iloc[i])
        else:
            old_female.append(data.iloc[i])




print(f"La media de edad de las personas en el Mall es de {statistics.mean(age)}")
colors = np.random.rand(len(data))

print(f"La media de edad de las mujeres en el Mall es de {statistics.mean(female)}")
print(f"La media de edad de las mujeres en el Mall es de {statistics.mean(male)}")

print(f"cantidad de mujeres teen hasta 20 años es de {len(teens_female)}")
print(f"cantidad de hombres teen hasta 20 años es de {len(teens_male)}")

print(f"cantidad de mujeres maduras entre 20 y 50 años es de {len(mature_female)}")
print(f"cantidad de hombres maduros entre 20 y 50 años es de {len(mature_male)}")

print(f"cantidad de mujeres mayores desde 50 arriba es de {len(old_female)}")
print(f"cantidad de hombres mayores desde 50 arriba es de {len(old_male)}")


plt.scatter(age, spent_score,c=colors,label='Media entre edad y gasto')
plt.xlabel("Age")
plt.ylabel("Spending Score (1-100)")
plt.show()

