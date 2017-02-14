`timescale 1ns/1ps

module testbench ();
reg clk;
reg rstart;

initial begin
  clk = 0;
  rstart = 0;
  #15 rstart = 1;
  #27 rstart = 0;
  #1000 rstart = 1;
  #27 rstart = 0;
end
always #10 clk =~clk;
// Instance: ~/astar/rtl/counter.v
counter counter_1 (/*autoinst*/
        //Inputs
        .clk    (clk    ),
        .rstart (rstart ),
        //Outputs
        .count  (count  ),
        .power  (power  ));
    );
endmodule
