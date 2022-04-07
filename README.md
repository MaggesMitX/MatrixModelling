# MatrixModelling
repository about planing and programming my Matrix Project
I will program the codes once for Raspberry Pi and for Arduino


Helped Sites: 
- https://max7219.readthedocs.io/en/0.2.3/
- https://pinout.xyz/
- https://www.amazon.de/-/en/AZDelivery-MAX7219-Parent-32/dp/B079HVW652/ref=sr_1_22?crid=11HHEH02H8Y1P&keywords=pi%2Bmatrix%2Banzeige%2B4fach&qid=1649250100&s=computers&sprefix=pi%2Bmatrix%2Banzeige%2B4%2Bfach%2Ccomputers%2C60&sr=1-22&th=1


Raspberry Pi:

- Library installation:
```sh
sudo apt-get install python-dev python-pip
```

```sh
sudo pip install max7219
```


- Or alternative clone from github.com:

```sh
git clone https://github.com/rm-hull/max7219.git
```
```sh
cd max7219
```
```sh
sudo pip install -e .
```

For the next step you have to do some settings in ur raspbian system:
```sh
cd max7219
```
```sh
sudo apt-get install python-dev python-pip
```
```sh
sudo pip install spidev
```
```sh
sudo python setup.py install
```

The GPIO pin-outs are connect as showed:

|Board Pin | Name | Remarks | RPiPin | RPi | Function|

 |1	        |VCC	    |+5V Power	   |2	    |5V0        | +V|
 |2	        |GND	      |Ground	   |6	    |GND        |-V|
 |3	        |DIN	      |Data In	   |19	    |GPIO 10    |(MOSI)|
 |4	        |CS	      |Chip Select     |24	    |GPIO 8     |(SPI CE0)|
 |5	        |CLK	      |Clock	   |23      |GPIO 11    |(SPI CLK)|


 Pre-requisites:
 By default, the SPI kernel driver is NOT enabled on the Raspberry Pi Raspian image. You can confirm whether it is enabled using the shell commands below:
 
```sh
$ lsmod | grep -i spi
spi_bcm2835             7424  0
```
Depending on the kernel version, this may report spi_bcm2807 rather than spi_bcm2835 - either should be adequate.
And that the devices are successfully installed in /dev:

```sh
$ ls -l /dev/spi*
crw------- 1 root root 153, 0 Jan  1  1970 /dev/spidev0.0
crw------- 1 root root 153, 1 Jan  1  1970 /dev/spidev0.1
```


max7219 cascaded:
If you have more than one device and they are daisy-chained together, you can initialize the library with:

```sh
import max7219.led as led

device = led.matrix(cascaded = 3)
device.show_message("Hello world!")
```

 Arduino:
 -
