import json

infile = open("US_fires_9_1.json", "r")
outfile = open("readable_fire_data1.json", "w")

fire_data = json.load(infile)

json.dump(fire_data, outfile, indent=4)

datalons, datalats, databright = [], [], []
for x in fire_data:
    lon = x["longitude"]
    lat = x["latitude"]
    bright = x["brightness"]
    datalons.append(lon)
    datalats.append(lat)
    if bright > 450:
        databright.append(bright)


from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

data = [
    {
        "type": "scattergeo",
        "lon": datalons,
        "lat": datalats,
        "marker": {
            "size": [0.05 * bright for bright in databright],
            "color": databright,
            "colorscale": "viridis",
            "reversescale": True,
            "colorbar": {"title": "Brightness"},
        },
    }
]

my_layout = Layout(title="US Fire - 9/1/2020 through 9/13/2020")
fig = {"data": data, "layout": my_layout}

offline.plot(fig, filename="fire_1.html")
