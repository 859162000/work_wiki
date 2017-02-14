`timescale 1ps/1ps
// Created by         :lianghy
// Filename           :\lianghy\work\dfcl\astar\rtl\basic\tray_module.v
// Author             :lianghy
// Created On         :2015-12-29 11:17
// Last Modified      : 
// Update Count       :2015-12-29 11:17
// Description        :
//                     
//=======================================================================
`include "d:/lianghy/work/dfcl/astar/rtl/basic/define.h"
module tray_module(/*autoarg*/
    //Inputs
    icou, 

    //Outputs
    tray_height);

input [3:0] icou; // current in, of motor
output [31:0] tray_height;

parameter Mt = 1;
parameter Ag = 10;

reg clk;
reg [3:0] Fm;
reg [7:0] At;
reg [7:0] Vt;
reg [31:0] Ht;
wire [7:0] Fg;
initial begin
  clk = 0;
  Fm = 0;
  At = 0;
  Vt = 0;
  Ht = 0;
end
assign Fg = Ag*Mt;
assign # 2 height = Ht;
always #1 clk = ~clk;
always @(posedge clk) begin
    if (Ht==0 && Fm<Fg) begin
      At <= #2 0; // delay means h
    end
    else begin
      At <= #2 (Fm-Fg)/Mt; // delay means h
    end
    Fm <= #`FFD ricou; // 代表传输延时。
    Vt <= #2 Vt+At;
  if (&Ht) begin
    Ht <= #2 Ht;
  end
  else begin
    Ht <= #2 Ht+Vt;
  end
end
/*
* Ag = 10 m/s**2 ; 重力加速度
* Fm = icou {0~16} ; 电机力矩
* Fg = Ag*Mt ; 托盘受到重力
* At = { (Fm-Fg)/Mt ;托盘加速度
*      { 0          ;Fm<Fg, Ht=0
* Vt = V0+At ; 托盘速度
* Ht = H0+Vt ; 托盘高度
* 默认 Td时间间隔 是时钟周期。
*/
endmodule
