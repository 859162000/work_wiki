`timescale 1ps/1ps
// Created by         :lianghy
// Filename           :tray_station.v
// Author             :lianghy
// Created On         :2015-12-30 16:37
// Last Modified      : 
// Update Count       :2015-12-30 16:37
// Description        :
//                     
//=======================================================================
/*记录高度变化，生成在单位时间内，高度变化的方向和大小*/
`include "d:/lianghy/work/dfcl/astar/rtl/basic/define.h"
module tray_height_sensor(/*autoarg*/
    //Inputs
    tray_height, 

    //Outputs
    tray_station, station_changed);
input [31:0] tray_height;
output [7:0] tray_station;  
output station_changed;

// tray_station define:
// 8'h00 zero
// 8'h01 stable not zero
// 8'h02 move up   mup
// 8'h03 move down mdw

wire [31:0] rhtray_rec[7:0];
wire [7:0] tray_station;
assign # 2 rhtray_rec[0] = height;
generate
genvar wi;
  for (wi=1;wi<8;wi=wi+1) begin
    assign # 2 rhtray_rec[wi] = rhtray_rec[wi-1];
  end
endgenerate
assign tray_station = (rhtray_rec[0]==0)? 8'h00 :
  (rhtray_rec[1]==rhtray_rec[0])? 8'h01 :
  (rhtray_rec[1]<rhtray_rec[0])? 8'h02 :
  8'h03 ;
assign #2 station_changed = rhtray_rec[0]!=rhtray_rec[1];

/*
* station_changed : flag 1 means tray station has changed*/
endmodule
