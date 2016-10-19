`timescale 1ns/10ps
`define FFD 2

module add();
input clk, rst_n;
input [1:0] a,b;
output [1:0] c;

reg [1:0] regd;
always @(posedge clk) begin
	if (!rst_n) begin
		regd <= #`FFD 2'b11;
	end
	else begin
		regd <= #`FFD wired;
	end
end

wire [1:0] wired;
assign #2 wired = a+b;
endmodule

module testbench();
reg [1:0] inita,initb;
reg clk,rst_n
wire [1:0] c;
initial begin
	inita = 2'b00;
	initb = 2'b00;
	rst_n = 1'b1;
	clk = 1'b0;
	#3
	rst_n = 1'b0;
	#11
	rst_n = 1'b1;
	#10
	inita = 2'b01;
	initb = 2'b01;
end

always #4 clk = ~clk;
add adder(.clk(clk), .rst_n(rst_n), .a({inita[0],initb[1]}), .b(initb), .c(netc));
endmodule

