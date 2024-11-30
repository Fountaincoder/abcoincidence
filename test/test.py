# SPDX-FileCopyrightText: © 2023 Uri Shaked <uri@tinytapeout.com>
# SPDX-License-Identifier: MIT

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles
import random

# DMADD madd(
        # .clk    (clk),
        # .run    (uio_in[3]),
        # .load   (uio_in[2]),
        # .insn   (uio_in[1:0]),
        # .index  (ui_in[7:4]),
        # .data   (ui_in[3:0]),
        # .out    ({uio_out[7:4],uo_out}),
        # .rst_n  (rst_n)
# );

@cocotb.test()
async def test_mn1(dut):
    dut._log.info("min 1")
  
    # Our example module doesn't use clock and reset, but we show how to use them here anyway.
    clock = Clock(dut.clk, 20, units="us")
    cocotb.start_soon(clock.start())
    dut.rst_n.value = 1
    await ClockCycles(dut.clk,1)
    dut.rst_n.value= 0
    dut.ena.value  = 1
    # await ClockCycles(dut.clk,1 )
    dut.ui_in.value = 0b0000_0001
    await ClockCycles(dut.clk,1 )
    dut.ui_in.value = 0b0000_0001
    await ClockCycles(dut.clk,1 )
    dut.ui_in.value = 0b0000_0001
    await ClockCycles(dut.clk,1 )
    dut.ui_in.value = 0b0000_0001
    await ClockCycles(dut.clk,1 )
    dut.ui_in.value = 0b0000_0011
    await ClockCycles(dut.clk,1 )
    dut.ui_in.value = 0b0000_0011
    await ClockCycles(dut.clk,1 )
    dut.ui_in.value = 0b0000_0011
    await ClockCycles(dut.clk,1 )
    dut.ui_in.value = 0b0000_0010
    await ClockCycles(dut.clk,1 )
    dut.ui_in.value = 0b0000_0010
    await ClockCycles(dut.clk,2 )
    dut._log.info(dut.uo_out.value)
    dut._log.info(dut.uio_out.value)
    # dut.uio_in.value  = 0b0000_1_0_00
    # await ClockCycles(dut.clk,30 )
    # dut._log.info(dut.uo_out.value)
    # assert dut.uo_out.value==1

