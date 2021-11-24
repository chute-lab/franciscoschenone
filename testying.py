# from statistics import mean
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import requests
from bs4 import BeautifulSoup
import pyautogui as pg
import time
import webbrowser as web
import sqlite3

link_cliente = "https://casa.mercadolibre.com.ar/MLA-935252205-excelente-casa-en-venta-en-barrio-el-golf-_JM#position=4&search_layout=grid&type=item&tracking_id=fc1238eb-6d1b-44c0-8b24-626be2a37943"

url = requests.get(link_cliente)
soup = BeautifulSoup(url.content,"html.parser")
resultado = soup.find("div", {"class":"ui-pdp-thumbnail__picture"}) #la posta
print(resultado)
    # precioInicio_text = resultado.text
    # precioInicial = float(precioInicxio_text)


