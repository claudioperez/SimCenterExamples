#!/usr/bin/python

# written: fmk, adamzs 06/20
# units kN & mm

import openseespy.opensees as ops

ops.wipe()

from params import *

# build the model

ops.model('basic', '-ndm', 2, '-ndf', 2)

ops.node(1,     0,    0)
ops.node(2,  4000,    0)
ops.node(3,  8000,    0)
ops.node(4, 12000,    0)
ops.node(5,  4000, 4000)
ops.node(6,  8000, 4000)

ops.fix(1, 1, 1)
ops.fix(4, 0, 1)

ops.uniaxialMaterial('Elastic', 1, E)

ops.element('truss', 1, 1, 2, Ao, 1)
ops.element('truss', 2, 2, 3, Ao, 1)
ops.element('truss', 3, 3, 4, Ao, 1)
ops.element('truss', 4, 1, 5, Au, 1)
ops.element('truss', 5, 5, 6, Au, 1)
ops.element('truss', 6, 6, 4, Au, 1)
ops.element('truss', 7, 2, 5, Ao, 1)
ops.element('truss', 8, 3, 6, Ao, 1)
ops.element('truss', 9, 5, 3, Ao, 1)

ops.timeSeries('Linear', 1)
ops.pattern('Plain', 1, 1)

ops.load(2, 0, -P)
ops.load(3, 0, -P)

# perform the analysis

ops.algorithm('Linear')
ops.integrator('LoadControl', 1.0)
ops.system('ProfileSPD')
ops.numberer('RCM')
ops.constraints('Plain')
ops.analysis('Static')
ops.analyze(1)

node_disp = [[ops.nodeDisp(node_i, dof_j) 
			 for dof_j in [1,2]] for node_i in range(1, 7)]

# save the node displacements

with open('node_disp.out', 'w') as f:
	for node_res in node_disp:
		f.write(' '.join([str(res) for res in node_res])+'\n')