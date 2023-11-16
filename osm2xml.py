import json
import sys
from fusion.util.geo import LocalCoordinateSystem

print('''<?xml version="1.0" encoding="UTF-8"?>
<graphml xmlns="http://graphml.graphdrawing.org/xmlns" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://graphml.graphdrawing.org/xmlns http://graphml.graphdrawing.org/xmlns/1.0/graphml.xsd">''')
with open(sys.argv[1],'r') as fp:
  data=json.load(fp)['elements']
nodes = {}
nid = {}
for d in data:
  if d['type'] == 'way' and 'tags' in d and 'aerodrome' in d['tags']:
    print(f'''<!-- {d['tags']['name']} -->''')
  if d['type'] == 'way' and 'tags' in d and 'aeroway' in d['tags'] and d['tags']['aeroway'] in ['taxiway','taxilane']: #,'runway']:
    for n in d['nodes']:
      if n not in nodes:
        nodes[n] = None
        nid[n] = len(nid)
lat = 9999
lon = 9999
for d in data:
  if d['type'] == 'node' and d['id'] in nodes:
    nodes[d['id']] = (d['lat'],d['lon'])
    lat = min(lat, d['lat'])
    lon = min(lon, d['lon'])

print('''  <key id="key0" for="node" attr.name="coords" attr.type="string" />
  <key id="key1" for="edge" attr.name="weight" attr.type="double" />
  <graph id="G" edgedefault="directed" parse.nodeids="free" parse.edgeids="canonical" parse.order="nodesfirst">''')
cs = LocalCoordinateSystem(lat, lon, 0)
vertices = {}
for k,v in nodes.items():
  coord = cs.lla_to_enu(*v)
  print(
f'''    <node id="n{nid[k]}">
      <data key="key0">{coord[0]:.4f},{coord[1]:.4f}</data>
    </node>''')

i = 0
for d in data:
  if d['type'] == 'way' and 'tags' in d and 'aeroway' in d['tags'] and d['tags']['aeroway'] in ['taxiway','taxilane']: #,'runway']:
    for j in range(1,len(d['nodes'])):
        print(
    f'''    <edge id="e{i}" source="n{nid[d['nodes'][j-1]]}" target="n{nid[d['nodes'][j]]}">
          <data key="key1">1</data>
        </edge>''')
        # Reverse direction.
        i += 1
        print(
    f'''    <edge id="e{i}" source="n{nid[d['nodes'][j]]}" target="n{nid[d['nodes'][j-1]]}">
          <data key="key1">1</data>
        </edge>''')
        i += 1
print('''  </graph>
</graphml>''')
    
