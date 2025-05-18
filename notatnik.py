users:list = [
    {"name":"Krzysztof","location":"Białobrzegi","posts":500},
    {"name":"Maja","location":"Świecie","posts":300},
    {"name":"Zuzanna","location":"Radzyń_Podlaski","posts":700},
    {"name":"Kalina","location":"Rypin","posts":321},
 ]

import bs4
import folium

# mapa = folium.Map(location=[52.21, 21.0], zooom_start=6)
# folium.Marker(location=[52.21, 21.0], popup=f"").add_to(mapa)
# mapa.save = ("mapa.html")


def get_coordinates(city_name:str):->list:
    import requests
    from bs4 import BeautifulSoup
    url=f"https://pl.wikipedia.org/wiki/{city_name}"
    response=requests.get(ur).text
    response_html=BeautifulSoup(response,"html.parser")
    latitude=float(response_html.select(".latitude")[1].text.replace(",","."))
    longitude=float(response_html.select(".longitude")[1].text.replace(",","."))
    print(latitude,longitude)
    return [latitude,longitude]

def get_map(users_data:list)->None:
mapa = folium.Map(location=[52.21, 21.0], zooom_start=6)
for user in users:
    print(user["location"])

    folium.Marker(
        location=get_coordinates(user["location"]),
        popup=f"{user["location"]} {user['name']}"
    ).add_to(mapa)
mapa.save = ('mapa.html')






