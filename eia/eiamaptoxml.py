import sys

print('''<?xml version="1.0" encoding="UTF-8"?>
<graphml xmlns="http://graphml.graphdrawing.org/xmlns" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://graphml.graphdrawing.org/xmlns http://graphml.graphdrawing.org/xmlns/1.0/graphml.xsd">
  <key id="key0" for="node" attr.name="coords" attr.type="string" />
  <key id="key1" for="edge" attr.name="weight" attr.type="double" />
  <graph id="G" edgedefault="directed" parse.nodeids="free" parse.edgeids="canonical" parse.order="nodesfirst">''')

with open(sys.argv[1], 'r') as vfp:
    for line in vfp.readlines():
        v = line.split(' ')
        v = [v[0]]+v[1].strip().split(',')
        print(
f'''    <node id="n{v[0]}">
      <data key="key0">{v[1]},{v[2]}</data>
    </node>''')

with open(sys.argv[2], 'r') as vfp:
    for i,line in enumerate(vfp.readlines()):
        v = line.strip().split(',')
        print(
f'''    <edge id="e{i}" source="n{v[0]}" target="n{v[1]}">
      <data key="key1">1</data>
    </edge>''')
print('''  </graph>
</graphml>''')
