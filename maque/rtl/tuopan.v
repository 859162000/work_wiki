`timescale 1ps/1ps
// Created by         :lianghy
// Filename           :tuopan.v
// Author             :lianghy
// Created On         :2015-11-13 11:12
// Last Modified      :2015-12-29 11:12
// Update Count       :2015-11-13 11:12
// Description        :
//                     
//=======================================================================
`include "../rtl/define.h"
module tuopan(/*autoarg*/
    //Inputs
    command, tray_height, 

    //Outputs
    icou);
input [3:0] command;
input [7:0] tray_height; 
// if ht_get_tar==1, at the same time dis_to_tar_cou==0
//output [1:0] action;
output [3:0] icou;

wire station_changed;
// target
// Instance: e:/work/astar/rtl/command_sensor.v
command_sensor command_sensor_0 (/*autoinst*/
        //Inputs
        .command  (command[96:0]  ),
        //Outputs
        .rcommand (rcommand[96:0] ));
// Instance: e:/work/astar/rtl/tray_height_sensor.v
tray_height_sensor tray_height_sensor_0 (/*autoinst*/
        //Inputs
        .tray_height     (tray_height[31:0] ),
        //Outputs
        .tray_station    (tray_station[7:0] ),
        .station_changed (station_changed   ));
//// Instance: e:/work/astar/rtl/action_controller.v
//action_controller action_controller_0 (/*autoinst*/
//// Instance: e:/work/astar/rtl/adjustment.v
//adjustment adjustment_0 (/*autoinst*/
//// Instance: e:/work/astar/rtl/judgment.v
//judgment judgment_0 (/*autoinst*/
// Instance: e:/work/astar/rtl/self_detection.v
self_detection self_detection_0 (/*autoinst*/
        //Inputs
        .self_detection_enable (self_detection_enable ),
        .stray_station         (stray_station[7:0]    ),
        .sensor                (sensor[1:0]           ),
        .main_station          (main_station[1:0]     ),
        //Outputs
        .aicou                 (aicou[3:0]            ),
        .action                (action[1:0]           ),
        .fi_self_dete          (fi_self_dete          ));
/***************************************************/
/*****global define**********************************************/
/*
*
name               width define/description
main_station       2     core station; 00:rest 01:busy 10:empty 11:power on
sensor             2     00:null 01:tray_height 10:obj_height
stray_station      8     height, unit is cm
action             2     00:null 01:current
aicou              4     current control
sd_en              1     seldf detection enable
*/
endmodule
