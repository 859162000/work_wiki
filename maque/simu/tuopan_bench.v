`timescale 1ps/1ps

module testbench ();
reg [3:0] command;
//wire [7:0] tray_station;
wire [3:0] ricou;
wire [31:0] tray_height;
initial begin
  command = 0;
  #127 command = 4'h1;
  #32 command = 0;
end
//always #10 clk =~clk;
// Instance: e:/work/astar/rtl/tuopan.v
tuopan core_0 (/*autoinst*/
        //Inputs
        .tray_height (tray_height[31:0] ),
        .command     (command[3:0]     ),
        //Outputs
        .icou        (icou[3:0]        ));
// Instance: e:/work/astar/rtl/tray_module.v
tray_module tray_0 (/*autoinst*/
        //Inputs
        .icou        (icou[3:0]         ),
        //Outputs
        .tray_height (tray_height[31:0] ));
endmodule
