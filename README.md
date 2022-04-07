# MatrixModelling
repository about planing and programming my Matrix Project
I will program the codes once for Raspberry Pi and for Arduino


Helped Sites: 
- https://max7219.readthedocs.io/en/0.2.3/
- https://pinout.xyz/
- https://www.amazon.de/-/en/AZDelivery-MAX7219-Parent-32/dp/B079HVW652/ref=sr_1_22?crid=11HHEH02H8Y1P&keywords=pi%2Bmatrix%2Banzeige%2B4fach&qid=1649250100&s=computers&sprefix=pi%2Bmatrix%2Banzeige%2B4%2Bfach%2Ccomputers%2C60&sr=1-22&th=1

Raspberry Pi:
-
Library installation:
$ sudo apt-get install python-dev python-pip
$ sudo pip install max7219

or alternative clone from github.com:
$ git clone https://github.com/rm-hull/max7219.git
$ cd max7219
$ sudo pip install -e .

For the next step you have to do some settings in ur raspbian system:
$ cd max7219
$ sudo apt-get install python-dev python-pip
$ sudo pip install spidev
$ sudo python setup.py install

The GPIO pin-outs are connect as:
Board Pin	Name	Remarks	     RPiPin	    RPi Function
1	        VCC	      +5V Power	   2	    5V0
2	        GND	      Ground	   6	    GND
3	        DIN	      Data In	   19	    GPIO 10 (MOSI)
4	        CS	      Chip Select  24	    GPIO 8 (SPI CE0)
5	        CLK	      Clock	       23       GPIO 11 (SPI CLK)