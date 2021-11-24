# from statistics import mean
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import requests
from bs4 import BeautifulSoup
import pyautogui as pg
import time
import webbrowser as web
import sqlite3



# PROBANDOOOO

import pandas as pd

# from flask import Flask, jsonify
from statistics import mean
from flask import Flask, request, jsonify
app = Flask(__name__)

from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import requests
from bs4 import BeautifulSoup
import pyautogui as pg
import time
import webbrowser as web
import sqlite3


app = Flask(__name__)
# from Nuevo_tp import alertando

CORS(app)
# resources = {r"/buscando/*": {"origins": "http://localhost"}})


# from flask_restful import Resource, Api
# from sqlalchemy import create_engine


@app.route('/consultas', methods = ['GET'])
def consultar():
    import sqlite3
    conexion = sqlite3.connect("consultaprecios.db")
    cursor = conexion.cursor()
    sentenciaSQL = cursor.execute("SELECT precioalerta FROM tablaclientes")
    resultado = cursor.fetchall()
    for resultadox in resultado:
        print(resultadox)
    conexion.commit()
    return jsonify("Lo minimo que la gente esta dispuesta a pagar por una propiedad es:", min(resultado))


#Examen 05/07/21 - EJERCICIO 3

@app.route('/borrados', methods = ['DELETE'])
def borrar(nombre):
    import sqlite3
    conexion = sqlite3.connect("consultaprecios.db")
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM tablaclientes where clientes = (?)", nombre )
    conexion.commit()
    return jsonify("El cliente ha sido eliminado de la base de datos")

@app.route('/buscando', methods = ['POST'])
def alertando_post():
    nombre = request.json["nombre"]
    link_cliente = request.json["link"]
    precio_alerta = request.json["precioalerta"]
    whatsapp = request.json["numero"]
    #Aca va el nombre que le pusimos al formulario en el front
    alertando(nombre, link_cliente, precio_alerta, whatsapp)

    return jsonify("Funciona")

def alertando(nombre, link_cliente, precio_alerta, whatsapp):
    url = requests.get(link_cliente)
    soup = BeautifulSoup(url.content,"html.parser")
    resultado = soup.find("span", {"class":"price-tag-fraction"}) #la posta
    precioInicio_text = resultado.text
    precioInicial = float(precioInicio_text)
    # whatsapp = float(whatsapp)
    '''Esto lo estamos haciendo en particular para meli pq el precio lo da en numeros con coma chicos'''
    precioInicial = precioInicial * 1000
    precio_alerta = float(precio_alerta)
#----------------
    url2 = "https://api-dolar-argentina.herokuapp.com/api/dolarblue"
    r = requests.get(url2)
    datos = r.json()
    precio_dolar_compra = datos['compra']
    precio_dolar_venta = datos['venta']
    # print(precio_dolar_compra)
    # print(precio_dolar_venta)
    ''' Aca estamos transformando de str a float el precio de el dolar para poder manipularlo'''
    a = precio_dolar_compra
    float(a)
    dolar_compra_float = int(float(a))
    b = precio_dolar_venta
    float(b)
    dolar_venta_float = int(float(b))
#--------------

    '''Aca estamos conviertiendo el precio que nos dio en cliente en pesos a dolares y lo redondemos a dos decimales'''
    precio_whatsapp = round((precioInicial * dolar_venta_float),2)
    '''Aca estamos pasando el precio del cliente convertido en dolares a str para poder concatenarlo en el mensaje de wapp'''
    a2= precio_whatsapp
    str(a2)
    preciowappstr = str(a2)
# Scrapping para mandar mensaje de whatsapp
    if precioInicial < precio_alerta:
        phone_no= str(whatsapp)
        parsedMessage=("Hola " + nombre + ", soy Carla de Yo te aviso." '\n'"Tu casa bajo de precio, el precio en pesos es $"+ preciowappstr + " . No dudes mas, compralo YA!" '\n'+ link_cliente)
        web.open('https://web.whatsapp.com/send?phone='+'+549'+phone_no+'&text='+parsedMessage)
        time.sleep(8)
        for i in range(2):
            pg.write('')
            pg.press('enter')
            print('Mensaje #'+str(i+1)+' enviado')
            pass
    else:
        print("Por el momento no bajo del precio esperado")

    conexion = sqlite3.connect("consultaprecios.db")
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO tablaclientes VALUES (?,?,?,?)", (nombre, link_cliente, precio_alerta, whatsapp))
    conexion.commit()



@app.route('/barrios', methods = ['GET'])
def barriando():
    data = pd.read_csv("precio-venta-deptos.csv")
    dataframe = pd.DataFrame(data)

    data_limpio = dataframe.loc[:, ['barrio', 'precio_prom', 'año']]

    data_validada = data_limpio[data_limpio.precio_prom.notna()]
    # Aca estamos filtrando para que nos muestre los valores mas actualizados (anio 2019)
    validado3 = data_validada[data_validada.año > 2018]
    # Aca estamos sacando los barrios que estaban duplicados
    test = validado3.drop_duplicates(subset=['barrio'])
    # Aca estamos sacando el indice de las columnas, pq quedaba mal
    sin_indice = test.set_index('barrio')
    resultadobarrio = sin_indice.loc[['ALMAGRO'], ['precio_prom']]

    for indice_fila, fila in resultadobarrio.iterrows():
        # print(indice_fila, fila)
        PrecioFinalMetro = (fila['precio_prom'])


    return jsonify(PrecioFinalMetro)

@app.route('/barrios1', methods = ['GET'])
def barriando1():
    data = pd.read_csv("precio-venta-deptos.csv")
    dataframe = pd.DataFrame(data)

    data_limpio = dataframe.loc[:, ['barrio', 'precio_prom', 'año']]

    data_validada = data_limpio[data_limpio.precio_prom.notna()]
    # Aca estamos filtrando para que nos muestre los valores mas actualizados (anio 2019)
    validado3 = data_validada[data_validada.año > 2018]
    # Aca estamos sacando los barrios que estaban duplicados
    test = validado3.drop_duplicates(subset=['barrio'])
    # Aca estamos sacando el indice de las columnas, pq quedaba mal
    sin_indice = test.set_index('barrio')
    resultadobarrio1 = sin_indice.loc[['BELGRANO'], ['precio_prom']]

    for indice_fila, fila in resultadobarrio1.iterrows():
        # print(indice_fila, fila)
        PrecioFinalMetro1 = (fila['precio_prom'])


    return jsonify(PrecioFinalMetro1)

@app.route('/barrios2', methods = ['GET'])
def barriando2():
    data = pd.read_csv("precio-venta-deptos.csv")
    dataframe = pd.DataFrame(data)

    data_limpio = dataframe.loc[:, ['barrio', 'precio_prom', 'año']]

    data_validada = data_limpio[data_limpio.precio_prom.notna()]
    # Aca estamos filtrando para que nos muestre los valores mas actualizados (anio 2019)
    validado3 = data_validada[data_validada.año > 2018]
    # Aca estamos sacando los barrios que estaban duplicados
    test = validado3.drop_duplicates(subset=['barrio'])
    # Aca estamos sacando el indice de las columnas, pq quedaba mal
    sin_indice = test.set_index('barrio')
    resultadobarrio2 = sin_indice.loc[['MONSERRAT'], ['precio_prom']]

    for indice_fila, fila in resultadobarrio2.iterrows():
        # print(indice_fila, fila)
        PrecioFinalMetro2 = (fila['precio_prom'])


    return jsonify(PrecioFinalMetro2)

@app.route('/barrios3', methods = ['GET'])
def barriando3():
    data = pd.read_csv("precio-venta-deptos.csv")
    dataframe = pd.DataFrame(data)

    data_limpio = dataframe.loc[:, ['barrio', 'precio_prom', 'año']]

    data_validada = data_limpio[data_limpio.precio_prom.notna()]
    # Aca estamos filtrando para que nos muestre los valores mas actualizados (anio 2019)
    validado3 = data_validada[data_validada.año > 2018]
    # Aca estamos sacando los barrios que estaban duplicados
    test = validado3.drop_duplicates(subset=['barrio'])
    # Aca estamos sacando el indice de las columnas, pq quedaba mal
    sin_indice = test.set_index('barrio')
    resultadobarrio3 = sin_indice.loc[['PALERMO'], ['precio_prom']]

    for indice_fila, fila in resultadobarrio3.iterrows():
        # print(indice_fila, fila)
        PrecioFinalMetro3 = (fila['precio_prom'])


    return jsonify(PrecioFinalMetro3)

@app.route('/barrios4', methods = ['GET'])
def barriando4():
    data = pd.read_csv("precio-venta-deptos.csv")
    dataframe = pd.DataFrame(data)

    data_limpio = dataframe.loc[:, ['barrio', 'precio_prom', 'año']]

    data_validada = data_limpio[data_limpio.precio_prom.notna()]
    # Aca estamos filtrando para que nos muestre los valores mas actualizados (anio 2019)
    validado3 = data_validada[data_validada.año > 2018]
    # Aca estamos sacando los barrios que estaban duplicados
    test = validado3.drop_duplicates(subset=['barrio'])
    # Aca estamos sacando el indice de las columnas, pq quedaba mal
    sin_indice = test.set_index('barrio')
    resultadobarrio4 = sin_indice.loc[['RECOLETA'], ['precio_prom']]

    for indice_fila, fila in resultadobarrio4.iterrows():
        # print(indice_fila, fila)
        PrecioFinalMetro4 = (fila['precio_prom'])


    return jsonify(PrecioFinalMetro4)

@app.route('/barrios5', methods = ['GET'])
def barriando5():
    data = pd.read_csv("precio-venta-deptos.csv")
    dataframe = pd.DataFrame(data)

    data_limpio = dataframe.loc[:, ['barrio', 'precio_prom', 'año']]

    data_validada = data_limpio[data_limpio.precio_prom.notna()]
    # Aca estamos filtrando para que nos muestre los valores mas actualizados (anio 2019)
    validado3 = data_validada[data_validada.año > 2018]
    # Aca estamos sacando los barrios que estaban duplicados
    test = validado3.drop_duplicates(subset=['barrio'])
    # Aca estamos sacando el indice de las columnas, pq quedaba mal
    sin_indice = test.set_index('barrio')
    resultadobarrio5 = sin_indice.loc[['VILLA CRESPO'], ['precio_prom']]

    for indice_fila, fila in resultadobarrio5.iterrows():
        # print(indice_fila, fila)
        PrecioFinalMetro5 = (fila['precio_prom'])


    return jsonify(PrecioFinalMetro5)










if __name__ == '__main__':
    app.run(debug= True, port=4000)







