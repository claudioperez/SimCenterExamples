

pset w 100.0
pset wR 50.0
pset k 326.32

set E 29000.0
set A 1e4
set Ic [expr $k*144*144*144/(24.*$E)]
set Ib 1e12
set g 386.1

puts [expr $w/$g]
puts [expr $wR/$g]




set L  288.0
set h  120.0
set E 29000.0 

set Ac 110.0 
pset Ic1 1190.0
pset Ic2 1190.0
set Ib 10e+8
set Ab 10e+8 
