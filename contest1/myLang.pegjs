start
  = instruction+

instruction
  = instructionWithLabel / instructionWithoutLabel

instructionWithLabel
  = label opcode " " location "\n"

instructionWithoutLabel
  = opcode " " location "\n"

label
  = [A-Za-z][A-Za-z0-9]* " "

opcode
  = "LOAD"i / "STORE"i / "ADD"i / "SUB"i / "MULT"i / "DIV"i / "BG"i / "BE"i / "BL"i / "BU"i / "READ"i / "PRINT"i / "DC"i / "END"i

location
  = label / variable / immediate

variable
  = [A-Za-z][A-Za-z0-9]*

immediate
  = "=" [0-9]+
