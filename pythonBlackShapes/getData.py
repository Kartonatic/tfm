import pandas as pd
from geopy.geocoders import Nominatim
import time

# Load excel data
excel = pd.ExcelFile('LIBRO_PUNTOS_NEGROS_2014.xls')

#Convert Excel to dataframe
df = pd.DataFrame()
for i in range(0, len(excel.sheet_names)):
    sitio = excel.parse(excel.sheet_names[i], header=1 )
    hoja = excel.parse(excel.sheet_names[i], header=3 )
    hoja['Provincia'] = sitio.columns[1]    
    df = df.append(hoja)

#Create new dataframe for get locations
blackshapes = pd.DataFrame(columns=['Address', 'Province', 'Country' , 'numAccident', 'lat', 'long'])
geolocator = Nominatim()
#Get location for each row in df
i=0
for index, row in df.iterrows():
    if (str(row['DENOMINACIÓN']) != 'NaN'):
        if (str(row['DENOMINACIÓN']) != 'nan'):
            isError = True
            while (isError):
                try:
		    # get location and save on blackshapes
                    print(str(row['DENOMINACIÓN']) + ' ' + str(row['Provincia']) + ' ' + 'Spain' + str(row['TOTAL\nACCIDENTES']))
                    data = row['DENOMINACIÓN'] + ' ' + row['Provincia'] + ' ' + 'España'
                    location = geolocator.geocode(data)
                    blackshapes.loc[i] = [ row['DENOMINACIÓN'], row['Provincia'], 'Spain', row['TOTAL\nACCIDENTES'], location.latitude, location.longitude]
                    i+=1
                    isError = False
                except Exception as e:
                    print(str(e))
                    isError = True
                    time.sleep(30)
# save blackshapes into a csv
blackshapes.to_csv('blackshapes.csv')