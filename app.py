import folium
from folium.plugins import HeatMapWithTime
import requests
from math import radians, sin, cos, sqrt, atan2
import webbrowser
import time


KEY = "b56e0bc159783b8396833600c20d83db"
escolha = input("Digite a opção de busca: (1 = latitude e longitude ; 2 = Cidade)")
if escolha == (1):
    lat = input("Insira a LATITUDE: ")
    lon = input("Insira a LONGITUDE: ")

    LINK = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={KEY}"
else :
    cidade = input("Insira a cidade desejada: ")
    LINK = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={KEY}"
    

requisicao = requests.get(LINK)
requisicao_dados = requisicao.json()
print(requisicao_dados)
lat = requisicao_dados['coord']['lat'] 
lon = requisicao_dados['coord']['lon']

escolha2 = input("Digite a opção de busca da segunda cidade: (1 = latitude e longitude ; 2 = Cidade)")
if escolha2 == (1):
    lat2 = input("Insira a LATITUDE: ")
    lon2 = input("Insira a LONGITUDE: ")

    LINK2 = f"https://api.openweathermap.org/data/2.5/weather?lat={lat2}&lon={lon2}&appid={KEY}"
else :
    cidade2 = input("Insira a cidade desejada: ")
    LINK2 = f"https://api.openweathermap.org/data/2.5/weather?q={cidade2}&appid={KEY}"

requisicao2 = requests.get(LINK2)
requisicao_dados2 = requisicao2.json()
print(requisicao_dados2)
lat2 = requisicao_dados2['coord']['lat'] 
lon2 = requisicao_dados2['coord']['lon']        

def formula(lat, lon, lat2, lon2):
    R = 6371.0

    lat = radians(lat)
    lon = radians(lon)
    lat2 = radians(lat2)
    lon2 = radians(lon2)

    dlon = lon2 - lon
    dlat = lat2 - lat

    a = sin(dlat / 2)**2 + cos(lat) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    D = R * c

    return D
 
distancia = formula(lat, lon, lat2, lon2)

latm = ((lat+lat2)/2)
lonm = ((lon+lon2)/2)


mapa = folium.Map([lat, lon], zoom_start=14, tiles="cartodbpositron")

folium.PolyLine([(lat,lon),(lat2,lon2)], tooltip="Distancia").add_to(mapa)

folium.Marker(
    location=[lat, lon],
    tooltip="Click me!",
    popup="Cidade 1",
    icon=folium.Icon(icon="cloud"),
).add_to(mapa)

folium.Marker(
    location=[latm, lonm],
    tooltip=distancia,
    popup="Ponto Medio",
    icon=folium.Icon(icon="cloud"),
).add_to(mapa)

folium.Marker(
    location=[lat2, lon2],
    tooltip="Click me!",
    popup="Mt. Hood Meadows",
    icon=folium.Icon(icon="cloud"),
).add_to(mapa)


mapa

mapa.save("mapa.html")
time.sleep(4)
webbrowser.open("mapa.html")

