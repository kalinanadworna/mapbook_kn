import folium

mapa = folium.Map(location=[52.21, 21.0], zooom_start=6)
folium.Marker(location=[52.21, 21.0], popup=f"").add_to(mapa)
mapa.save = ("mapa.html")






