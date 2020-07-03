#!/usr/bin/python

# written: fmk, adamzs 06/20

import sys

responses = sys.argv[1:]

# identify the responses of interest
nodes = [int(r.split('_')[1]) for r in responses]
dofs = [int(r.split('_')[3]) if len(r.split('_'))>2 else 1 
        for r in responses]

# load the node displacements
node_disp = []
with open('node_disp.out', 'r') as f:
	node_disp = [line.strip().split(' ') for line in f.readlines()]

# get the requested results
results = []
for n_i, d_i in zip(nodes, dofs):
	try:
		results.append(str(node_disp[n_i-1][d_i-1]))
	except:
		results.append('0.0')

# save the results
with open('results.out', 'w') as f:
	f.write(' '.join(results))