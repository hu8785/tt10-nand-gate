This file is used to generate your project datasheet. Please fill in the information below and delete any unused sections.

You can also include images in this folder and reference them in the markdown. Each image must be less than
512 kb in size, and the combined size of all images must be less than 1 MB.
-->

## How it works

The NAND gate is the complement of AND function. Its graphic symbol consists of an AND gate’s graphic symbol followed by a small circle. Here’s the logical representation of the NAND gate.

We start by declaring the module. module, a basic building design unit in Verilog HDL, is a keyword to declare the module’s name. NAND_2 is the identifier. Identifiers are the name of the module. The module command instructs the compiler to create a block containing certain inputs and outputs. The list in parenthesis is known as the port list, it contains the input and output ports. Then we declare other datatypes required in our design as follows.

wire Yd; 
wire in Verilog represents an electrical connection. It is internal, therefore not mentioned in the port list. Next,

and(Yd, A, B); 
not(Y, Yd); 
endmodule; 

Here AND is the operation performed on A, B, to get its output in Yd. Then Yd is passed through an inverter, and the output is obtained in Y. The compiler understands the AND and the NOT operation the same way we do. endmodule terminates the module.

## How to test

NAND Truth table

Inputs | Outputs A | B |Y 0 0 1 0 1 1 1 0 1 1 1 0


## External hardware

List external hardware used in your project (e.g. PMOD, LED display, etc), if any.
NONE
