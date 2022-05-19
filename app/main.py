from typing import Union
import json
from fastapi import FastAPI

app = FastAPI()

f = open('data.json')
data = json.load(f)


@app.get("/")
def read_root():
    return data


@app.get("/consos/{j1}/{m1}/{a1}/{h1}/{j2}/{m2}/{a2}/{h2}")
def read_item(j1: str, m1: str,a1:str,h1:str,j2:str,m2:str,a2:str,h2:str):
    result={"consos":[]}
    j=j1
    m=m1
    a=a1
    h=h1[0:2]
    min=h1[3:]
    i=0
    inter=False
    breaker=True
    while (int(data['consos'][i][0])<int(j2) or int(data['consos'][i][1])<int(m2) or int(data['consos'][i][2])<int(a2) or data['consos'][i][3]!=h2)and (breaker):
        if int(data['consos'][i][0])==int(j1) and int(data['consos'][i][1])==int(m1) and int(data['consos'][i][2])==int(a1) and  data['consos'][i][3]==h1:
            inter= True
        if inter:
            result["consos"].append("Le " +data['consos'][i][0]+"/"+data['consos'][i][1]+"/"+data['consos'][i][2]+" à " +data['consos'][i][3]+" la consommation a été de :"+data['consos'][i][4]+" MW")
        if int(data['consos'][i][0])==int(j2) and int(data['consos'][i][1])==int(m2) and int(data['consos'][i][2])==int(a2) and  data['consos'][i][3]==h2:
            inter=False
            breaker=False



        i+=1
    result["consos"].append("Le " +data['consos'][i][0]+"/"+data['consos'][i][1]+"/"+data['consos'][i][2]+" à " +data['consos'][i][3]+" la consommation a été de :"+data['consos'][i][4]+" MW")
    # afficheur="\n".join(result["consos"])
    return result
    return {"j1":j1,"m1":m1,"a1":a1,"h1":h1,"j2":j2,"m2":m2,"a2":a2,"h2":h2}
