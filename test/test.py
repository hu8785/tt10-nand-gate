import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles


@cocotb.test()
async def test_project(dut):
    dut._log.info("Start")

    # Clock: 10 us period
    clock = Clock(dut.clk, 10, unit="us")
    cocotb.start_soon(clock.start())

    # Reset
    dut._log.info("Reset")
    dut.ena.value = 1          # enable design
    dut.ui_in.value = 0
    dut.uio_in.value = 0
    dut.rst_n.value = 0
    await ClockCycles(dut.clk, 5)
    dut.rst_n.value = 1
    await ClockCycles(dut.clk, 1)

    dut._log.info("Test project behavior")

    # Test all four combinations of A (bit 0) and B (bit 1)
    # ui_in[0] = A, ui_in[1] = B
    test_vectors = [(0, 0), (0, 1), (1, 0), (1, 1)]

    for a, b in test_vectors:
        # Pack A and B into ui_in as a 2-bit integer: ui_in = {B,A}
        dut.ui_in.value = (b << 1) | a

        # Wait for a clock edge so combinational logic settles
        await ClockCycles(dut.clk, 1)

        # Read Y from uo_out[0] (LSB of the output bus)
        y = int(dut.uo_out.value) & 0x1

        # NAND truth table: Y = ~(A & B)
        expected = 0 if (a and b) else 1

        dut._log.info(f"A={a}, B={b}, Y={y}, expected={expected}")
        assert y == expected, f"NAND failed for A={a}, B={b}: got {y}, expected {expected}"
