import _gmplot
import argparse
import json

green = 10
yellow = 20
orange = 25
red = 100

ap = argparse.ArgumentParser()
ap.add_argument('-d', '--data', required=True,
    help='JSON data string')
args = vars(ap.parse_args())

json_data = json.loads(args['data'])

orangelats=[44.985563,44.970366,44.992770]
orangelngs=[-93.182058,-93.177255,-93.186360]
redlats=[44.983365,44.998281,44.996532]
redlngs=[-93.185968,-93.193360,-93.182029]
yellowlats=[44.956277,44.968683,44.977585]
yellowlngs=[-93.171469,-93.153370,-93.164273]
greenlats=[44.988368,44.968263,44.957578]
greenlngs=[-93.163870,-93.162276,-93.153360]
'''
for i in json_data:
    if i.count < green:
        greenlats.append(i.lat)
        greenlngs.append(i.lng)
    elif i.count < yellow:
        yellowlats.append(i.lat)
        yellowlngs.append(i.lng)
    elif i.count < orange: 
        orangelats.append(i.lat)
        orangelngs.append(i.lng)
    else:
        redlats.append(i.lat)
        redlngs.append(i.lng)
'''
gmap = _gmplot.GoogleMapPlotter(44.975473, -93.175166, 12)



#gmap.plot([37.428], [-122.144], 'cornflowerblue', edge_width=10)
#gmap.scatter(lats, lons, '#3B0B39', size=40, marker=False)
gmap.scatter(orangelats, orangelngs, 'orange', marker=True)
gmap.scatter(redlats, redlngs, 'red', marker=True)
gmap.scatter(greenlats, greenlngs, 'green', marker=True)
gmap.scatter(yellowlats, yellowlngs, 'yellow', marker=True)
#gmap.scatter(lats, lons, 'k', marker=True)
#gmap.heatmap(heat_lats, heat_lngs)

gmap.draw("mymap.html")