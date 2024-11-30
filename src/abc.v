// Gray counter
`define default_netname none

module ABC
(
	input clk, 
	input enable, 
	input reset, 
	input X1,
	input X2,
	output reg [3:0] A,
	output reg [3:0] B,
	output reg [3:0] C1,
	output reg [3:0] C2
);

	always @ (posedge reset or posedge clk)
	begin
		if (reset) begin
			A <= 0;
			B <= 0;
			C1 <= 0;
			C2 <= 0;
		end
		
		if (enable)
		begin
			A <= A + (!X1 && X2);
			B <= B + (X1 && !X2);
			C1 <= C1 + (X1 && X2);
			C2 <= C2+ (X1 && X2);
		end
	end

endmodule
