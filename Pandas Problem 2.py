import pandas as pd
cars = pd.read_csv('cars.csv')
print('1')
print(cars.iloc[0:5:,range(0,11,2)])
#
print('2')
print(cars.loc[cars['Model']=='Mazda RX4'])
#
print('3')
print(cars.loc[cars['Model']=='Camaro Z28',['Model','cyl']])
#
print('4')
print(cars.loc[cars['Model']=='Mazda RX4',['Model','cyl','gear']])
print(cars.loc[cars['Model']=='Ford Pantera L',['Model','cyl','gear']])
print(cars.loc[cars['Model']=='Hona Civic',['Model','cyl','gear']])