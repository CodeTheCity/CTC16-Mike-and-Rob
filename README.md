# CTC16-Mike-and-Rob
CTC16 team looking at modifying devices to show air quality indications


# LED boards
Original board:

![Original board](http://foo.bodaegl.com/original_board.jpg)

Microcontroller removed and some wires added:

![With some wires](http://foo.bodaegl.com/wired.jpg)

Schematic

![Schematic](http://foo.bodaegl.com/wiring.png)

Connections from NodeMCU to the LED board:

5V -> 5V pad on the back of the board

GND -> GND pad on the back of the board (though all GNDs are common so could tack it on elsewhere if more convenient)


D5 -> R pad of MCU footprint

D6 -> G pad of MCU footprint

D2 -> B pad of MCU footprint

D1 -> W pad of MCU footprint
