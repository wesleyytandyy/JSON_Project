import json

infile = open("eq_data_1_day_m1.json", "r")
outfile = open("readable_eq_data.json", "w")


# the json.load() funciron converts the data into a format python can work with in this case a giant dictionary
eq_data = json.load(infile)

# the json.dump() function takes a JSON data object and a file object and creates a file
# the indent=4 tells dump() to format the data using indentions

json.dump(eq_data, outfile, indent=4)


list_of_eqs = eq_data["features"]

mags, lons, lats = [], [], []

for eq in list_of_eqs:
    mag = eq["properties"]["mag"]
    lon = eq["geometry"]["coordinates"][0]
    lat = eq["geometry"]["coordinates"][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

print(mags[:10])
print(lons[:10])
print(lats[:10])

"""
print(eq_data["features"][0]["properties"]["mag"])
"""

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline


data = [Scattergeo(lon=lons, lat=lats)]

my_layout = Layout(title="Global Earthquakes")
fig = {"data": data, "layout": my_layout}

offline.plot(fig, filename="global_earthquakes.html")
