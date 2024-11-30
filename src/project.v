/*
 * Copyright (c) 2024 Jonny Edwards
 * SPDX-License-Identifier: Apache-2.0
 */

module tt_um_fountaincoder_top_abc (
    input  wire       clk,      // clock
    input  wire       ena,      // will go high when the design is enabled
    input  wire [7:0] ui_in,    // Dedicated inputs
    output wire [7:0] uo_out,   // Dedicated outputs
    input  wire [7:0] uio_in,   // IOs: Input path
    output wire [7:0] uio_out,  // IOs: Output path
    output wire [7:0] uio_oe,   // IOs: Enable path (active high: 0=input, 1=output)
    input  wire       rst_n     // reset_n - low to reset
);

// All output pins must be assigned. If not used, assign to 0.
assign uio_oe  = 8'b0;

ABC abc
(
	.clk(clk), 
	.enable(ena),
	.reset(rst_n), 
	.X1(ui_in[0]),
	.X2(ui_in[1]),
	.A(uo_out[3:0]),
	.B(uo_out[7:4]),
	.C1(uio_out[3:0]),
	.C2(uio_out[7:4])
);

endmodule

