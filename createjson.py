import json
import pandas as pd
import datetime

data={"consos":[]}
for année in range(2012,2021):
    nom_fichier="mix"+str(année)+".csv"
    df=pd.read_csv(nom_fichier, encoding= 'unicode_escape',delimiter = ";", usecols=['Date','Heures','Consommation'])
    for i in range(len(df)):
            df_date = df.values[i][0]
            df_heure = df.values[i][1]
            df_conso=df.values[i][2]
        
            df_year=df_date[6:]
            # print(year)
            df_month=df_date[3:5]
            # print(month)
            df_day=df_date[0:2]
            # print(day)
            # data['consos'].append(str(df_day)+"/"+str(df_month)+"/"+str(df_year)+" à "+str(df_heure)+" consommation: "+str(df_conso))
            data['consos'].append([str(df_day),str(df_month),str(df_year),str(df_heure),str(df_conso)])


jsonString = json.dumps(data)
jsonFile = open("data.json", "w")
jsonFile.write(jsonString)
jsonFile.close()