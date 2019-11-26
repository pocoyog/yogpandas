import pandas as pd
cars = pd.read_csv('cars.csv')
print('First Five \n', cars.head())
print('Last Five \n', cars.tail())

