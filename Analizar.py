
#1.Extraccion de datos (DATA EXTRACTION)
def leerAno(ano):
    ficheroAnual=open(f"{ano}_lloguer_preu_trim.csv",'r',encoding='utf-8')
    datosAnuales=ficheroAnual.readlines()
    return datosAnuales


datosAgregados = []
for ano in range(2014,2024):
    datosAnuales = leerAno(ano)
    datosAgregados += datosAnuales
#2.Manipulacion de datos (DATA WRANGLING,DATA CLEANING)
datosAgregados_limpios=[]
for linea in datosAgregados:
    linea_limpia=linea.replace('"','') #Eliminamos las comillas por espacios blancos
    linea_limpia=linea_limpia.replace('\n','') #Eliminamos los saltos de linea
    linea_limpia=linea_limpia.replace("Sant Pere, Santa Caterina i la Ribera",'Sant Pere & Santa Caterina i la Ribera')
    linea_limpia=linea_limpia.split(',')
    datosAgregados_limpios.append(linea_limpia)

#3.ANalisis de datos (DATA ANALYSIS)

def AnalizarBarrio():
    trimestresVilaGracia = [] # Definir las variables antes del bloque condicional
    alquileresVilaGracia = []
    trimestresVallcarca = []
    alquileresVallcarca = []
    trimestresColl = []
    alquileresColl = []
    trimestresSalut = []
    alquileresSalut = []
    trimestresCamp = []
    alquileresCamp = []
    
    for linea in datosAgregados_limpios:
        if linea[3] == 'Gràcia' and linea[6] == 'Lloguer mitjà mensual (Euros/mes)':
                
                if linea[5] == 'la Vila de Gràcia':
                    alquileresVilaGracia.append(linea[0]+"\n"+linea[1]+"T")
                    trimestresVilaGracia.append(float(linea[-1]))
                    
                elif linea[5]=='Vallcarca i els Penitents':
                    alquileresVallcarca.append(linea[0]+"\n"+linea[1]+"T")
                    trimestresVallcarca.append(float(linea[-1]))
                    
                elif linea[5]=='el Coll':
                    alquileresColl.append(linea[0]+"\n"+linea[1]+"T")
                    trimestresColl.append(float(linea[-1]))
                    
                elif linea[5]=='la Salut':
                    alquileresSalut.append(linea[0]+"\n"+linea[1]+"T")
                    trimestresSalut.append(float(linea[-1]))
                elif linea[5]=="el Camp d'en Grassot i Gràcia Nova":
                    alquileresCamp.append(linea[0]+"\n"+linea[1]+"T")
                    trimestresCamp.append(float(linea[-1]))
    
    # Devolver los datos analizados
    datos={

        "la Vila de Gràcia":[trimestresVilaGracia,alquileresVilaGracia],

        "Vallcarca i els Penitents":[trimestresVallcarca,alquileresVallcarca],

        "el Coll":[trimestresColl,alquileresColl],

        "la Salut":[trimestresSalut,alquileresSalut],

        "el Camp d'en Grassot i Gràcia Nova":[trimestresCamp,alquileresCamp]

    }

    return datos

# 4. VISUALIZACIÓN DE DATOS (DATA VISUALIZATION)
from matplotlib import pyplot as plt

fig,ax = plt.subplots(figsize=(15,8))
for key,value in AnalizarBarrio().items():
    x=value[1]
    y=value[0]
    ax.plot(x,y,label=key)
    ax.tick_params(axis='both', which='major', labelsize=7)
    ax.set_title("Evolució del lloguer mitjà a Vila de Gràcia (Euros): 2014-2023")
    ax.legend(loc="upper left")
    ax.set_xlabel("Años", fontdict = {'fontsize':14, 'fontweight':'bold', 'color':'tab:blue'})
    ax.set_ylabel("Lloguers (Euros)", fontdict = {'fontsize':14, 'fontweight':'bold', 'color':'tab:blue'})
    ax.grid()
plt.show()














