#%%
import json
from json import decoder

#read
data = None
with open('BAUMKATOGD.json', 'r') as f:
    data = json.load(f)
# %%
print(f'# Bäume: {len(data["features"])}')
print('Arten: ')
arten = set()
for b in data['features']:
    arten.add(b['properties']['GATTUNG_ART'])
print(f'# {len(arten)}')
#print(arten)

#%% remove unedible
keys = ['ahorn', 'zeder', 'erle', 'eiche', 'buche', 
'esche', 'linde', 'pappel', 'ginkgo', 'gefülltblühende kastanie',
'pyramidenkastanie', 'akazie', 'säulen-schnurbaum', 'eibe', 'zypresse',
'ulme', 'weide', 'birke', 'kiefer', 'fontanesia phillyreoides', 
'riesenlebensbaum', 'fichte', 'tanne', 'magnolie', 'lärche',
'trompetenbaum', 'gelbe kastanie', 'stechpalme', 'schneekirsche',
'guttaperchabaum', 'zelkove', 'tulpenbaum', 'lederhülsenbaum',
'platane', 'mehlbeere', 'tamariske', 'trauerkirsche', 
'scharlachkastanie', 'götterbaum', 'schlehdorn', 'dreilappiger apfel',
'goldregen', 'rotdorn', 'lebensbaum', 'paulownia',
'pfarrerkapperl', 'flügelnuss', 'taubenbaum', 'katsurabaum',
'pagodenschnurbaum', 'gleditsia', 'scharlachkirsche', 
'gefülltblühende kirsche', 'zelkova', 'glanzmispel', 
'mammutbaum', 'robinie', 'gelbholz', 'weißdorn', 'flieder',
'zierbirne',  'schmalblättrige kastanie', 'douglasie', 'tokyokirsche',
'elsbeere', 'thuje', 'fenchelholzbaum', 'traubenkirsche',
'kreuzdorn', 'strauchkastanie', 'holzapfel', 'vielblütiger apfel',
'eisenholzbaum', 'perückenstrauch', 'tai-haku', 'amberbaum', 
'zierapfel', 'traubenkirsche', 'osagedorn', 'surenbaum', 
'blütenkirsche', 'scheinzypr', 'hahnendorn', 'rotblühende kastanie',
'zürgelbaum', 'wird gepflanzt', 'blasenbaum', 'baumwacholder',
'schneebirne', 'korkbaum', 'laubbaum', 'eisenholzbaum', 'judasblattbaum',
'winterkirsche', 'schnurbaum', 'rosskastanie', 'steinweichsel',
'eibisch', 'essigbaum', 'nelkenkirsche', 'spiegelrinden-kirsche',
'buchsbaum', 'säulenkirsche', 'nicht bekannt', 'judasbaum', 'blütenkirsche',
'blutapfel', 'mammutbaum', 'gleditschie', 'aesculus spec.', 'sanddorn',
'zelkove', 'geweihbaum', 'schnurbaum', 'jap. blüten-kirsche', 'blüten-kirsche',
'hickorynuss', 'hängebirne', 'flügelnuss', 'traubenkirsche',
'hirschkolbensumach', 'kugelkirsche', 'raketen-wacholder',
'pavie', 'wacholder', 'hartriegel', 'unbekannt']
arten = [a.lower() for a in arten]
def contained(s:str, l:list):
    for ll in l:
        if ll in s:
            return True
    return False
arten = [a for a in arten if not contained(a, keys)]
print(f'# {len(arten)}')
print(arten)

#%%
print(len(data['features']))
trees = [d for d in data['features'] if str.lower(d['properties']['GATTUNG_ART']) in arten]
print(len(trees))

#%% prepare geojson

geojson = {
    "type": "FeatureCollection",
    "features": []
}

for tree in trees:
    feature = {
        "type": "Feature",
        "properties": {
            "title": tree['properties']['GATTUNG_ART'],
            "description": f'straße: {tree["properties"]["OBJEKT_STRASSE"]}, umfang: {tree["properties"]["STAMMUMFANG_TXT"]}, höhe: {tree["properties"]["BAUMHOEHE_TXT"]}, nummer: {tree["properties"]["BAUMNUMMER"]}'
        },
        "geometry": {
            "coordinates": [round(x,6) for x in tree['geometry']['coordinates']],
            "type": "Point"
        }
    }
    geojson['features'].append(feature)


# debug
#geojson['features'] = geojson['features'][:100]
    
with open('trees.geojson', 'w', encoding='utf8') as outfile:
    json.dump(geojson, outfile, indent=4, ensure_ascii=False)
    


#%%



# %%
