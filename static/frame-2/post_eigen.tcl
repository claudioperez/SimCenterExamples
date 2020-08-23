
set numMeasurements 5

set measuredLambdas {1025.21 1138.11 1099.39 1002.41 1052.69}
set sigmaLambda 54.203

set measuredPhis {1.53 1.24 1.38 1.50 1.35}
set sigmaPhi 0.0705

set PI 3.14159

# calculate eigenvalues
set numModes 3
set eigenValues [eigen -fullGenLapack $numModes]

set phi [expr [nodeEigenvector 5 1 1] / [nodeEigenvector 3 1 1]]
set lambda [lindex $eigenValues 0]

set error {}
for {set m 0} {$m < $numMeasurements} {incr m 1} {
    lappend error [expr ([lindex $measuredLambdas $m] - $lambda) / $sigmaLambda]
}
for {set m 0} {$m < $numMeasurements} {incr m 1} {
    lappend error [expr ([lindex $measuredPhis $m] - $phi) / $sigmaPhi]
}

# create results file
set outFile [open "results.out" w]
puts $outFile "$error"
close $outFile
