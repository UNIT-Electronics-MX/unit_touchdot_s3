## **3 Functional Overview**

### **3.1 Processing and Wireless Connectivity**

The ESP32-S3-MINI-1-N8 module provides the application processor, flash
storage, 2.4 GHz Wi-Fi, and Bluetooth Low Energy. The board exposes native USB
D+ and D− signals through USB-C and dedicated test points.

### **3.2 Wearable I/O**

Large plated holes around the board edge may be soldered, clipped, or sewn with
conductive thread. The signal pads expose GPIO1–4, GPIO7–11, GPIO17, GPIO18,
and GPIO45. GPIO1–4 and GPIO7–11 also provide analog and/or capacitive-touch
functions as marked on the board pinout.

### **3.3 User Feedback and Controls**

- **L3 / D13:** user LED on GPIO7
- **L4 / D25:** WS2812B-2020 RGB LED data input on GPIO45; its data output is
  routed to the D25 sewable pad for chaining compatible LEDs
- **PB1:** Boot button associated with GPIO0
- **PB2:** Reset button connected to EN
- **SW1:** board power switch
- **L1 / L2:** power and charge indicators

### **3.4 I²C / QWIIC Expansion**

The four-pin QWIIC-compatible connector exposes GND, 3.3 V, SDA/GPIO5, and
SCL/GPIO6. Solder bridge SB1 enables the connector supply. The signal order and
3.3 V domain must be checked before attaching a cable or third-party module.

### **3.5 microSD Storage**

The bottom-side microSD socket operates in SPI mode. GPIO21 is chip select,
GPIO9 is MOSI, GPIO7 is SCK, and GPIO8 is MISO. Pull-up resistors for GPIO8,
GPIO9, and GPIO21 are associated with the microSD interface.

### **3.6 Battery and USB-C**

The PH 2.0 connector accepts a compatible single-cell Li-ion/LiPo battery.
USB-C supplies power, charges the battery through the onboard charge circuit,
and connects the ESP32-S3 native USB interface for programming and data.

### **3.7 Debug and Expansion Access**

The board includes a 2 × 6 expansion header, a six-pin serial-programming row,
JTAG test points, and USB D+/D− test points. These interfaces expose additional
GPIO and system signals while preserving the compact circular form factor.

![](hardware/resources/unit_topology_V_0_1_2_ue0072_Touch-Dot-S3.png){width=5.6in}

| Reference | Description |
|---|---|
| IC1 | Espressif ESP32-S3 module |
| U1 | AP2112K 3.3 V LDO regulator |
| PB1 / PB2 | Boot / reset push buttons |
| SW1 | Power switch |
| L1 / L2 | Power / charge indicators |
| L3 | User LED on GPIO7 (D13) |
| L4 | WS2812B-2020 RGB LED on GPIO45 (D25) |
| SB1 | QWIIC VCC enable solder bridge |
| J1 | USB-C connector |
| J2 | QWIIC-compatible I²C connector |
| J3 | PH 2.0 battery connector |
| J4 | microSD socket |
| JP1 / JP2 | Sewable pads |
| JP3 / JP4 | GPIO, system, and power headers |
