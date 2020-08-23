model BasicBuilder -ndm 2 -ndf 3;	                         # 2 dimensions, 3 dof per node

# define GEOMETRY -------------------------------------------------------------
# nodal coordinates:
node 1    0.   0.0
node 2    0. 144.0
node 3    0. 288.0
node 4    0. 432.0
node 5    $L   0.0
node 6    $L 144.0 
node 7    $L 288.0 
node 8    $L 432.0 

# Single point constraints -- Boundary Conditions
fix 1 1 1 1;                                               # node DX DY RZ
fix 5 1 1 1

# Nodal mass:
mass 2 [expr $w/$g]  [expr $w/$g]     0.;                  # node#, Mx My Mz, Mass=Weight/g.
mass 3 [expr $w/$g]  [expr $w/$g]     0.     
mass 4 [expr $wR/$g] [expr $wR/$g]    0. 

equalDOF 2 6 1
equalDOF 3 7 1
equalDOF 4 8 1

# Define ELEMENTS -------------------------------------------------------------
# define geometric transformation: performs a linear geometric transformation of beam stiffness and 
# resisting force from the basic system to the global-coordinate system
geomTransf Linear 1
element elasticBeamColumn 1 1 2 $Ac $Ic $E 1
element elasticBeamColumn 2 2 3 $Ac $Ic $E 1
element elasticBeamColumn 3 3 4 $Ac $Ic $E 1
element elasticBeamColumn 4 5 6 $Ac $Ic $E 1
element elasticBeamColumn 5 6 7 $Ac $Ic $E 1
element elasticBeamColumn 6 7 8 $Ac $Ic $E 1
element elasticBeamColumn 7 2 6 $Ab $Ib $E 1
element elasticBeamColumn 8 3 7 $Ab $Ib $E 1
element elasticBeamColumn 9 4 8 $Ab $Ib $E 1
