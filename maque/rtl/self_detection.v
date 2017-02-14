`timescale 1ps/1ps
// Created by         :lianghy
// Filename           :G:\lianghy\work\dfcl\astar\rtl\basic\self_detection.v
// Author             :lianghy
// Created On         :2016-01-12 15:48
// Last Modified      : 
// Update Count       :2016-01-12 15:48
// Description        :
//                     
//=======================================================================
`include "../rtl/basic/define.h"
/* theory:自测时，一次测试一个输出端口，输出量逐渐增加。
* actural: enlarge icou, get the force that can move the tray.
*/
module self_detection(/*autoargu*/
);
input [1:0] main_station;
input self_detection_enable;
input [1:0] sensor; // address
input [7:0] stray_station; // data
output [1:0] action; // address
output [3:0] aicou; // data
output fi_self_dete;// finishe initial self detection

reg [1:0] raction; // address
reg [3:0] raicou; // data
assign #2 action = raction;
assign #2 aicou = raicou;
assign #2 next_raction = raction<<1;
wire sensor_valid;
assign #2 sensor_valid = sensor!=2'b00;
wire [15:0] reflection_dict;
wire [15:0] rreflection_dict[1:0];// list word length equal or larger than action address width.
reg rlist_address; // start from zero.
assign #2 reflection_dict = {action,aicou,sensor,stray_station};
assign #4 rreflection_dict[rlist_address] = (writing&&sensor_valid)?reflection_dict:rreflection_dict[rlist_address];
assign #2 next_rlist_address = rlist_address+2'b01; // this is actual is a shift function. Using add is for writing convenion.
wire reg_data_equal_in;
assign #2 reg_data_equal_in = rreflection_dict[rlist_address]==reflection_dict; 
reg en,start,max_action_finished;
reg wen,writing,one_finish;
// max_action_finished : 所有动作都试过一次。
assign #2 max_action_finished = raction[1]&&one_finish;
// max_action_finished : 所有动作都试过一次。最后一个动件试验结束。
always begin
  if (self_detection_enable) begin
    #2 en = 1;
  end
  else begin
    if (start) begin
      #2 en = 0;
    end
    else begin
      #2 en = en;
    end
  end
end
always begin
  if (en) begin
    start = 1;
    raction = 2'b01;
    raicou = 4'b0;
    wen = 1;
    writing = 0;
    one_finish = 0;
    max_action_finished = 0;
    rlist_address = 2'b00;
  end
  else begin
    if (start) begin
      if (max_action_finished) begin
        start = 0;// finish sd
      end
      else begin
        // ref pic write_wave
        // writing
        if (wen) begin
          #2 writing = 1;
        end
        else begin
          if (one_finish) begin
            #2 writing = 0;
          end
          else begin
            #2 writing = writing;
          end
        end
        // wen
        if (writing) begin
          #2 wen = 0;
        end
        else begin
          #2 wen = 1;
        end
        // one_finish
        if (wen) begin
          #2 one_finish = 0;
        end
        else begin
          #2 one_finish = reg_data_equal_in;
        end
        // next address
        if (one_finish) begin
          #2 rlist_address = next_rlist_address;
          if (raction[1]) begin
            // 当最后一个动作时，动作不再移位。
            #4 raction = raction;
          end
          else begin
            #4 raction = next_raction;
          end
        end
        else begin
          #2 rlist_address = rlist_address;
          #2 raction = raction;
        end
        // self detection next
        if (writing) begin
        end
        else begin
        end
      end
    end
    else begin
    end
  end
end

initial begin
  // each inner node needs a random initial value.
end
endmodule
