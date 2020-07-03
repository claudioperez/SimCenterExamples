# tcl script to place abs difference between 2 numbers in output file results.out

pset a 1
pset b 0

set D [expr abs($a-$b)]

set outputFile [open "results.out" "w"]
puts $outputFile $D
close $outputFile