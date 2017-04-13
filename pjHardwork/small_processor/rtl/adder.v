`timescale 1ns/1ps
// file name: adder.v
// author: lianghy
// time: 2017-3-13 11:20:36

`include "define.v"

module adder(
input clk,
input rst_n,
input data_in1,
input data_in2,
input op,
output data_o,
output over
);

reg [`DATA_WIDTH-1:0] reg_data_in1, reg_data_in2;

always @(posedge clk) begin
    if (!rst_n) begin
        reg_data_in1 <= `DATA_WIDTH'b0;
        reg_data_in2 <= `DATA_WIDTH'b0;
    end else begin
        reg_data_in1 <= data_in1;
        reg_data_in2 <= data_in2;
    end
end

assign complement_data_in2 = ~reg_data_in2+`DATA_WIDTH'b1;
assign {over, data_o} = op ? (reg_data_in1+complement_data_in2) :
    (reg_data_in1+reg_data_in2);

endmodule
