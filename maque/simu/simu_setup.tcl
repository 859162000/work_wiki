if {[file exists work]} {
  file delete -force work
}
vlib work
do ./dofile.do
