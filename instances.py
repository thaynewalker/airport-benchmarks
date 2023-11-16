import sys
import random

print('''<?xml version="1.0" encoding="UTF-8"?>
<root>''')

nodes = set()
with open(sys.argv[1], 'r') as vfp:
  for line in vfp.readlines():
    if 'node id' in line:
      nodes.add(line.split('"')[1][1:])
nodes = list(nodes)

starts = set()
goals = set()
for i in range(1000):
  start = random.randint(0,len(nodes)-1)
  while start in starts:
      start = random.randint(0,len(nodes)-1)
  goal = random.randint(0,len(nodes)-1)
  while goal in goals:
      goal = random.randint(0,len(nodes)-1)
  print(f'''   <agent start_id="{nodes[start]}" goal_id="{nodes[goal]}"/>''')

print('''</root>''')
