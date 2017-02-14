`include "d:/lianghy/work/dfcl/astar/rtl/basic/define.h"
module command_sensor(/*autoarg*/
    //Inputs
    command, 

    //Outputs
    rcommand);
input [96:0] command;
output [96:0] rcommand;
// command : valid,hightest,lowest,time
// [96],[95:64],[63:32],[31:0]
//wire [95:0] rcommand;
assign #1 rcommand = command[96]?command[95:0]:rcommand;
endmodule
