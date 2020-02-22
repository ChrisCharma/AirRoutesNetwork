import numpy as np
import pandas as pd

df = pd.read_csv('routes.csv')
# Giving my dataset some column names
df.columns = ['Airline', 'AirlineID', 'SrcAirport', 'SrcAirportID', 'DesAirport', 'DesAirportID', 'Codeshare', 'Stops',
              'Equipment']
df = df.drop(['Airline', 'AirlineID', 'SrcAirportID', 'DesAirportID', 'Codeshare', 'Stops',
         'Equipment'], axis=1)
df.to_csv('SrcDesNames.csv', index=False)
