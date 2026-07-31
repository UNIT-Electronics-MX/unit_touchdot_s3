## **Description**

The UNIT TouchDot S3 is a compact, circular development board based on the
Espressif ESP32-S3-MINI-1 module. Its sewable-pad layout is intended for
wearables, interactive textiles, IoT prototypes, and compact smart devices.
The board combines 2.4 GHz Wi-Fi and Bluetooth Low Energy connectivity with
capacitive-touch inputs, analog inputs, USB-C programming, battery operation,
microSD storage, a QWIIC-compatible I²C connector, and onboard visual feedback.

![](hardware/resources/unit_top_V_0_1_2_ue0072_Touch-Dot-S3.png){width=3.4in}

### **Applications**

- Wearable electronics and e-textiles
- Capacitive-touch user interfaces
- Battery-powered IoT nodes and data loggers
- Educational embedded-system projects
- Interactive art and compact connected devices

### **Software Support**

TouchDot S3 can be programmed through the Arduino ecosystem, MicroPython, or
Espressif ESP-IDF. The repository includes setup notes and examples for GPIO,
ADC, I²C, SPI/microSD, the WS2812 LED, wireless communication, and deep sleep.

### **Hardware Features**

- Espressif ESP32-S3-MINI-1-N8 module with dual-core Xtensa LX7 CPU
- 2.4 GHz 802.11 b/g/n Wi-Fi and Bluetooth Low Energy
- 16 sewable pads: 11 multiplexed GPIO pads, one NeoPixel data pad, two ground
  pads, one battery-voltage pad, and one 3.3 V pad
- Capacitive-touch and analog functions exposed on the sewable pads
- USB-C connector for power, native USB data, programming, and charging
- PH 2.0 mm Li-ion/LiPo battery connector and onboard charge management
- QWIIC-compatible 4-pin I²C connector at 3.3 V
- microSD socket connected through SPI
- WS2812B-2020 addressable RGB LED and a user LED
- Boot and reset buttons, power switch, and power/charge indicators
- Expansion, serial-programming, JTAG, and USB test-point access
