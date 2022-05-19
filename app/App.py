import pandas as pd

import calendar as cl
import datetime



    
    

def Modele(semaine, jour, année, heure ): 
    nom_fichier="mix"+str(année)+".csv"
    df=pd.read_csv(nom_fichier, encoding= 'unicode_escape',delimiter = ";", usecols=['Date','Heures','Consommation'])
    janvier=cl.Calendar()
    offset=0
    for day in janvier.itermonthdates(année,1):
        if day.year!=année:
            offset+=1 
        if int(day.day)==1 and day.month==1:
            premier_jour_année=day
    a=(semaine-1)*7-offset
    
    compteur=0
    compteur_mois=0
    compteur_jour=1
    while compteur<a:
        compteur_mois+=1
        compteur_jour=0
        mois=cl.Calendar()
        for day in mois.itermonthdates(année,compteur_mois):
            if day.month==compteur_mois:
                compteur+=1
                compteur_jour+=1
                
                if compteur==a:
                    
                    break
    if compteur_mois==0:
        compteur_mois+=1
    if jour=="lundi":
        compteur_jour+=1
    if jour=="mardi":
        compteur_jour+=2
    if jour=="mercredi":
        compteur_jour+=3
    if jour=="jeudi":
        compteur_jour+=4
    if jour=="vendredi":
        compteur_jour+=5
    if jour=="samedi":
        compteur_jour+=6
    if jour=="dimanche":
        compteur_jour+=7
    print(compteur_mois)
    print(compteur_jour)
    jour=datetime.date(année,compteur_mois,compteur_jour)

    print(jour)
    
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
        print(int(df_day)==int(jour.day))
        if int(jour.month)==int(df_month) and int(jour.day)==int(df_day) and df_heure==heure:
            return df_conso
    return 'rien trouvé'
    
    


def Modele2(journée,mois,année,heure):
    nom_fichier="mix"+str(année)+".csv"
    df=pd.read_csv(nom_fichier, encoding= 'unicode_escape',delimiter = ";", usecols=['Date','Heures','Consommation'])
    jour=datetime.date(année,mois,journée)
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
        print(int(df_day)==int(jour.day))
        if int(jour.month)==int(df_month) and int(jour.day)==int(df_day) and df_heure==heure:
            return df_conso


def post_lieu(journée1:int,mois1:int,année1:int,heure1:str,journée2:int,mois2:int,année2:int,heure2:str):
    données={'conso':[]}
    journée=0
    while journée!=journée1:
        journée+=1
    mois=0
    while mois!=mois1:
        mois+=1
    année=0
    while année!=année1:
        année+=1
    heure=''+heure1
    données['conso'].append("le "+str(journée)+"/"+str(mois)+"/"+str(année)+" à "+heure+" consommation: "+str(Modele2(journée,mois,année,heure)))
    while journée!=journée2 or mois!=mois2 or année!= année2  or heure!=heure2:
        
        hour=int(heure[0:2])
        minute=int(heure[3:])
        minute+=15
        if minute==0:
            hour+=1
        if hour==24:
            hour=0
            journée+=1
        if journée==32:
            journée=1
            mois+=1
        if mois==13:
            mois=1
            année+=1
        heure=str(hour)+":"+str(minute)
        données['conso'].append("le "+str(journée)+"/"+str(mois)+"/"+str(année)+" à "+heure+" consommation: "+str(Modele2(journée,mois,année,heure)))
    return données

print(post_lieu(1,1,2020,'23:00',1,1,2020,'23:45'))




