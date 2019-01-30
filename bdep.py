import requests
import json

station = 'POWL'
r = requests.get('http://api.bart.gov/api/etd.aspx?cmd=etd&orig='+station+'&key=MW9S-E7SL-26DU-VV8V&json=y')
j = json.loads(r.text)

print('Trains from '+station+' station:')
for item in j['root']['station'][0]['etd']:
    destination = item['destination']
    trains = []
    est = item['estimate']
    for e in est:
        if e['minutes'] == 'Leaving':
            trains.append('Leaving now')
        else:
            trains.append(e['minutes'] + ' minutes')

    print(destination + ' : ' + ', '.join(trains))

