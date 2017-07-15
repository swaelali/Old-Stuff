import re, os

with open('demo.html','r') as f:
    script = f.read()
f.close()

with open('readings.txt', 'r') as readsf:
    readings = readsf.read()
readsf.close()

lat = readings.splitlines()[0]
lng =  readings.splitlines()[1]

script = re.sub('LatLng\(\d+\.\d+\,\d+\.\d+\)','LatLng('+lat+','+lng+')',script)

nf = open('demo1.txt','w')
nf.write(script)
nf.close()

os.rename('demo1.txt','demo1.html')
