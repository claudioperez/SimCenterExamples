#define analysis
numberer RCM
constraints Transformation
system Umfpack
integrator Newmark 0.5 0.25
test NormUnbalance 1.0e-2 10 
algorithm Newton
analysis Transient -numSubLevels 2 -numSubSteps 10

# add damping
set eigenValues [eigen 3]
modalDamping 0.02

# perform analysis
set tFinal [expr $numStep * $dt]
set tCurrent [getTime]
set ok 0

while {$ok == 0 && $tCurrent < $tFinal} {
    
    set ok [analyze 1 $dt]
    
    # if the analysis fails try initial tangent iteration
    if {$ok != 0} {
	test NormUnbalance 1.0e-2  1000 1
	algorithm ModifiedNewton -initial
	set ok [analyze 1 $dT]
	test NormUnbalance 1.0e-2  10 
	algorithm Newton
    }
    
    set tCurrent [getTime]
}
