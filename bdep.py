import requests
import json
import sys


def get_stations():
    r = requests.get('http://api.bart.gov/api/stn.aspx?cmd=stns&key=MW9S-E7SL-26DU-VV8V&json=y')
    j = json.loads(r.text)
    stations = {s['name']: s['abbr'] for s in j['root']['stations']['station']}
    return stations


def get_departures(abbr, name):
    try:
        r = requests.get('http://api.bart.gov/api/etd.aspx?cmd=etd&orig='+abbr+'&key=MW9S-E7SL-26DU-VV8V&json=y')
        j = json.loads(r.text)

        print('Trains from '+name+' station:\n')
        for item in j['root']['station'][0]['etd']:
            destination = item['destination']
            trains = []
            est = item['estimate']
            for e in est:
                if e['minutes'] == 'Leaving':
                    trains.append('Leaving now')
                else:
                    trains.append(e['minutes'] + ' minutes')

            print(destination + ': ' + ', '.join(trains))
    except:
        print("Invalid station or unknown input.")


def list_stations():
    stations = get_stations()
    for name, abbr in stations.items():
        print(abbr + ' | ' + name)


def main():
    stations = get_stations()
    stations_list = []
    for i, v in enumerate(stations.keys()):
        print(i, v)
        stations_list.append(v)

    station_number = int(input("Please choose a station: "))
    print('\n')
    get_departures(stations[stations_list[station_number]], stations_list[station_number])


if __name__ == '__main__':
    if len(sys.argv) == 1:
        main()
    elif len(sys.argv) == 2:
        if sys.argv[1] == 'list':
            list_stations()
        else:
            get_departures(sys.argv[1], sys.argv[1])
