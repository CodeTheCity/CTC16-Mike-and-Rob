# CTC16-Mike-and-Rob
CTC16 team looking at modifying devices to show air quality indications


# LED boards
Original board:

![Original board](https://f002.backblazeb2.com/file/ormiret-pub/CTC16-air-pics/original_board.jpg)

Microcontroller removed and some wires added:

![With some wires](https://f002.backblazeb2.com/file/ormiret-pub/CTC16-air-pics/wired.jpg)

Schematic

![Schematic](https://f002.backblazeb2.com/file/ormiret-pub/CTC16-air-pics/wiring.png)

Connections from NodeMCU to the LED board:

5V -> 5V pad on the back of the board

GND -> GND pad on the back of the board (though all GNDs are common so could tack it on elsewhere if more convenient)


D5 -> R pad of MCU footprint

D6 -> G pad of MCU footprint

D2 -> B pad of MCU footprint

D1 -> W pad of MCU footprint

Put details of Wifi netorks into secrets.py then load boot.py, main.py and pwm_alert.py as main.py onto nodemcu running micropython.

boot.py looks at what wifi networks it can see and if there is a passowrd for them in secrets.py it connects. 

Then main.py (pwm_alert.py) will be run, which gets the colour it should display from the web and sets the colour component values as duty cycles for PWM.

Rough layout of the transistors on the board: 

![Transistors](http://foo.bodaegl.com/transistors.png)

Can put control lines onto resistors if MCU pads aren't usable after removing MCU.
