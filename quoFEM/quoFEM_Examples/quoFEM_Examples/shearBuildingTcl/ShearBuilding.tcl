#units kips/in .. model with beam and column elements, stiff beams

# some parameters
pset w 100.0
pset wR 50.0
pset k 326.32

set factor 1.5
set motion elCentro

set E 29000.0
set A 1e4
set Ic [expr $k*144*144*144/(24.*$E)]
set Ib 1e12
set g 386.1

puts [expr $w/$g]
puts [expr $wR/$g]

# the model
model BasicBuilder -ndm 2 -ndf 3
node 1  0.0    0.0 
node 2  0.0 144.0 -mass [expr $w/$g]  [expr $w/$g]   0.
node 3  0.0 288.0 -mass [expr $w/$g]  [expr $w/$g]   0.
node 4  0.0 432.0 -mass [expr $wR/$g] [expr $wR/$g] 0.
node 5  288.   0.0 
node 6  288. 144.0 
node 7  288. 288.0 
node 8  288. 432.0 
fix 1 1 1 1
fix 5 1 1 1
equalDOF 2 6 1
equalDOF 3 7 1
equalDOF 4 8 1
geomTransf Linear 1
element elasticBeamColumn 1 1 2 $A $Ic $E 1
element elasticBeamColumn 2 2 3 $A $Ic $E 1
element elasticBeamColumn 3 3 4 $A $Ic $E 1
element elasticBeamColumn 4 5 6 $A $Ic $E 1
element elasticBeamColumn 5 6 7 $A $Ic $E 1
element elasticBeamColumn 6 7 8 $A $Ic $E 1
element elasticBeamColumn 7 2 6 $A $Ib $E 1
element elasticBeamColumn 8 3 7 $A $Ib $E 1
element elasticBeamColumn 9 4 8 $A $Ib $E 1

# Set some parameters
set record elCentro

# Source in TCL proc to read PEER SMD record
source ReadRecord.tcl
ReadRecord $record.AT2  $record.dat dT nPts	    

timeSeries Path 1 -filePath $record.dat -dt $dT -factor [expr $factor*$g]
pattern UniformExcitation  1 1 -accel 1

# no damping
rayleigh 0.0 0.0 0.0 0.0

recorder EnvelopeNode -file node.out -node 1 2 3 4 -dof 1 2 disp
#recorder EnvelopeElement -file forces.out -ele 1 2 3 forces

numberer RCM
constraints Transformation
system Umfpack
integrator Newmark 0.5 0.25
test NormUnbalance 1.0e-2 10 
algorithm Newton
analysis Transient -numSubLevels 2 -numSubSteps 10



set tFinal [expr $nPts * $dT]
set tCurrent [getTime]
set ok 0

while {$ok == 0 && $tCurrent < $tFinal} {
    
    set ok [analyze 1 $dT]
    
    # if the analysis fails try initial tangent iteration
    if {$ok != 0} {
	puts "regular newton failed .. lets try an initail stiffness for this step"
	test NormDispIncr 1.0e-8  1000 1
	algorithm ModifiedNewton -initial
	set ok [analyze 1 $dT]
	if {$ok == 0} {puts "that worked .. back to regular newton"}
	test NormDispIncr 1.0e-12  10 
	algorithm Newton
    }
    
    set tCurrent [getTime]
}

# REMOVE RECORDERS .. VERY IMPORTANT
remove recorders