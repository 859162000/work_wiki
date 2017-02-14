`timescale 1ns/1ps
// file name: circle_list_regfile.v
// author: lianghy
// time: 2017-2-9 10:40:54

module circle_list_regfile(
input next_in,
input get_in,
output next_out,
output get_out,

input state_control    ,
input line_pointer_rst ,
input line_pointer_set ,
input [7:0] write_data       ,

output transmigration   ,
output [7:0] line_pointer_addr,
output [7:0] cur_data          
);


reg_data_in

ca
always @(get_in) begin
	

get_out = (reg_data_in==write_data)&&(next_in)
next_out = !(get_in)&&(data_out!=reg_data_out)
if 
always @(posedge get_out) begin
	next_out <= 1'b1
end
endmodule
