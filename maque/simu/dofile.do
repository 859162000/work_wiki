
vlog "../rtl/define.h" -work work
vlog "../rtl/tuopan.v" -work work
vlog "../rtl/basic/tray_module.v" -work work
vlog "../rtl/basic/tray_station.v" -work work
vlog "./tuopan_bench.v" -work work
set ELAB_OPTIONS ""
set TOP_LEVEL_NAME "testbench"
eval vsim -t 1ps -L work -l test_simu.log $TOP_LEVEL_NAME
view wave
add wave -noupdate -divider {Global Signals}
add wave -noupdate -format literal -radix hexadecimal /testbench/command
add wave -noupdate -format literal -radix hexadecimal /testbench/tray_height
add wave -noupdate -format literal -radix hexadecimal /testbench/icou
add wave -noupdate -divider {module tuopan Signals}
add wave -format literal -radix hexadecimal /testbench/core_0/rcommand
add wave -format literal -radix binary /testbench/core_0/tray_station
add wave -format literal -radix binary /testbench/core_0/tray_station
add wave -format literal -radix binary /testbench/core_0/tray_station
add wave -format literal -radix binary /testbench/core_0/tray_station
#add wave -noupdate -divider {tray_module}
#add wave /testbench/tray_0/*
#add wave /testbench/core_0/*
#run 1ns
##ps_gw : 4'h0 move up; 1 hold; 2 decrease force; 3 move down;
