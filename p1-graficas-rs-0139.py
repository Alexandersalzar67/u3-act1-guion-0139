import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#Alexander Salazar nc = 0139
#crearemos nuestra tabla y la guardaremos con pandas
# tenemos 5 listas de redes sociales con 4 elementos por lista
fb = ['Facebook', 8833, True, 2006]
twt = ['Twitter', 8575, False, 2008]
ig = ['Instagram', 7575, True, 2010]
wsp = ['Whatsapp', 8828, True, 2009]
tel = ['Telegram', 2992, False, 2010]
lkn = ['Linkdin', 7277, False, 2012]
# creamos una lista de listas (conformando la tabla)
lista_redes_sociales=[fb,twt,ig,wsp,tel,lkn]
print(lista_redes_sociales)

df_redes_sociales=pd.DataFrame(lista_redes_sociales,columns=["Nombre","Cantidad","Es_FB","Años"])
print(df_redes_sociales)

#df_redes_sociales.to_csv("redessociales.csv", index=False)
#crear grafica de lineas
#donde x es Nombre en el eje horizontal
#donde y es Cantidad en el eje vertical
plt.plot(df_redes_sociales["Nombre"],df_redes_sociales["Cantidad"])
plt.title("Graficas redes sociales 0139")
plt.xlabel("Nombre de las redes")
plt.ylabel("Cantidad de usuarios")
plt.show()

#creamos una grafica de puntos
plt.scatter(df_redes_sociales["Nombre"],df_redes_sociales["Cantidad"])
plt.show()
#graficas de barras
plt.bar(df_redes_sociales["Nombre"],df_redes_sociales["Cantidad"])
plt.title("Graficas redes sociales 0139")
plt.xlabel("Nombre de las redes")
plt.ylabel("Cantidad de usuarios")
plt.show()
# ordenarla grafica de barras de forma descendente
# de la mas grande a la mas pequeñas
df_rs_ordenar=df_redes_sociales.sort_values("Cantidad",ascending=False)
plt.bar(df_rs_ordenar["Nombre"],df_rs_ordenar["Cantidad"])
plt.show()

# coloreando la grafica
df_rs_ordenar=df_redes_sociales.sort_values("Cantidad",ascending=False)
plt.bar(df_rs_ordenar["Nombre"],df_rs_ordenar["Cantidad"],
        color=["b","g","c","m","y","r"])
plt.show()

# Grafica de pastel de redes sociales
#plt.scatter(df_redes_sociales["Nombre"],df_redes_sociales["Cantidad"])
plt.pie(df_redes_sociales["Cantidad"],labels=df_redes_sociales["Nombre"])
plt.show()