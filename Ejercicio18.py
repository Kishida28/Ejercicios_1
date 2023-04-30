# Define el mapa mundial centrado alrededor de Lima, Perú con un zoom bajo
# https://python-graph-gallery.com/288-map-background-with-folium/
import folium
world_map = folium.Map(location=[-12.0431800, -77.0282400], zoom_start=12, tiles='Stamen Terrain')

# mostrando el mapa
world_map