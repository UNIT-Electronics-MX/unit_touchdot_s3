## **4 Connectors and Pinouts**

### **4.1 Top and Bottom Pinout**

![](hardware/resources/unit_pinout_top_v_0_2_0_ue0072_touch_dot_s3_en.png){width=6.3in}

![](hardware/resources/unit_pinout_bottom_v_0_2_0_ue0072_touch_dot_s3_en.png){width=6.3in}

### **4.2 Sewable Pads**

| Board label | ESP32-S3 signal | Additional function |
|---|---|---|
| A0 / T1 | GPIO1 | ADC, touch |
| A1 / T2 | GPIO2 | ADC, touch |
| A2 / T3 | GPIO3 | ADC, touch |
| A3 / T4 | GPIO4 | ADC, touch |
| D25 / NeoPixel | GPIO45 | WS2812 data output |
| D2 / T11 | GPIO11 | Touch |
| D3 / TX1 | GPIO17 | UART1 TX |
| D4 / RX1 | GPIO18 | UART1 RX |
| D10 / SS / T10 | GPIO10 | SPI chip select, touch |
| D11 / MOSI / A8 / T9 | GPIO9 | SPI MOSI, ADC, touch |
| D12 / MISO / A7 / T8 | GPIO8 | SPI MISO, ADC, touch |
| D13 / SCK / A6 / T7 | GPIO7 | SPI clock, ADC, touch, user LED |
| GND (2 pads) | GND | Ground return |
| VBAT | Battery rail | Battery supply access |
| 3V3 | 3.3 V rail | Regulated supply access |

### **4.3 QWIIC-Compatible Connector (J2)**

| Pin | Signal | ESP32-S3 GPIO |
|---:|---|---|
| 1 | GND | — |
| 2 | 3.3 V | — |
| 3 | SDA / A4 / T5 | GPIO5 |
| 4 | SCL / A5 / T6 | GPIO6 |

### **4.4 microSD Socket (J4, SPI Mode)**

| microSD pin | Name | SPI function | ESP32-S3 GPIO |
|---:|---|---|---|
| 1 | DAT2 | Not used in SPI mode | — |
| 2 | DAT3 / CD | CS | GPIO21 |
| 3 | CMD | MOSI | GPIO9 |
| 4 | VDD | 3.3 V | — |
| 5 | CLK | SCK | GPIO7 |
| 6 | VSS | GND | — |
| 7 | DAT0 | MISO | GPIO8 |
| 8 | DAT1 | Not used in SPI mode | — |

### **4.5 Expansion Header (2 × 6)**

| Position | Row 1 | Row 2 |
|---:|---|---|
| 1 | 5 V | GND |
| 2 | D27 / GPIO47 | D28 / GPIO48 |
| 3 | D19 / GPIO37 | D20 / GPIO38 |
| 4 | D17 / GPIO35 | D18 / GPIO36 |
| 5 | D15 / GPIO33 | D16 / GPIO34 |
| 6 | 3.3 V | GND |

### **4.6 Serial Programming Header (1 × 6)**

| Pin | Signal | ESP32-S3 connection |
|---:|---|---|
| 1 | GND | GND |
| 2 | EN / Reset | EN |
| 3 | 3.3 V | 3.3 V rail |
| 4 | D1 | GPIO44 (RX0) |
| 5 | D0 | GPIO43 (TX0) |
| 6 | Boot | GPIO0 |

The D0/D1 labels follow the released board artwork. When connecting an external
serial adapter, cross its TX and RX lines according to signal direction and
verify the 3.3 V logic level.

### **4.7 JTAG and USB Test Points**

| Label | Signal |
|---|---|
| D21 | GPIO39 / MTCK |
| D22 | GPIO40 / MTDO |
| D23 | GPIO41 / MTDI |
| D24 | GPIO42 / MTMS |
| D+ | USB D+ |
| D− | USB D− |
