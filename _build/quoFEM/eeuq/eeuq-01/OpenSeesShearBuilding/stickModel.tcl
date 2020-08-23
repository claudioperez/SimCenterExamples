#units kips/in
# some parameters

pset w 100.0
pset wR 50.0
pset k 326.32

set g 386.4
# the model
model BasicBuilder -ndm 2 -ndf 2
node 1    0. 0. 
node 2    0. 144. -mass [expr $w/$g] [expr $w/$g] 
node 3    0. 288. -mass [expr $w/$g] [expr $w/$g]     
node 4    0. 432. -mass [expr $wR/$g] [expr $wR/$g]  
fix 1 1 1
uniaxialMaterial Elastic 1 $k
element zeroLength 1 1 2 -mat 1 1 -dir 1 2
element zeroLength 2 2 3 -mat 1 1 -dir 1 2
element zeroLength 3 3 4 -mat 1 1 -dir 1 2



