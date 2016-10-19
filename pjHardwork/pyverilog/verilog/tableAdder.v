`timescale 1ps/1ps
// Created by         :lianghy
// Filename           :adder.v
// Author             :lianghy
// Created On         :2016-06-21 21:40
// Last Modified      : 
// Update Count       :2016-06-21 21:40
// Description        :
//                     
//=======================================================================
// 输入：data1 + data2 =
// 输出：result
// 过程：
//   data1，将data1存入寄存器a
//   +，将rega存入加法器端口1
//   data2，将data2存入加法器端口2
//   =，将计算结果输出
module tableAdder(/*autoarg*/
);
input [3:0] data1;
input [3:0] data2;
input [3:0] op;

always @(posedge clk) begin
	dataOut <= #`FFD ldataOut;
end
assign ldataOut = (op==`EQUAL)?(data1+data2):ldataOut;
assign 
endmodule
