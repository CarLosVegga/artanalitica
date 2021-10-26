#import pandas as pd
import csv

print("Hola mundo")
counter = 0
suma = 0
with open('insurance.csv', newline='') as File:
    reader = csv.reader(File)
    for row in reader:
        if(counter != 0):
            suma += int(row[0])
        counter += 1
print(suma//counter)