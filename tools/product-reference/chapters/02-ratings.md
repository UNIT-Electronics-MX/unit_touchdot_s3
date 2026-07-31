## **2 Electrical Characteristics**

### **2.1 Documented Operating Values**

| Symbol | Description | Value | Unit |
|---|---|---:|---|
| VUSB | USB-C input supply | 5 | V |
| VCC | Digital logic and QWIIC supply | 3.3 | V |
| VBAT | Single-cell Li-ion/LiPo battery input | Battery rail | — |
| ADCRES | ADC resolution used by the board documentation | 12 | bit |
| FI2C | Typical I²C bus frequency | 400 | kHz |

These are interface values documented by the project, not absolute maximum
ratings. Refer to the ESP32-S3-MINI-1, regulator, charger, and peripheral
component datasheets before designing near a component limit.

### **2.2 Electrical Precautions**

- GPIO, touch, ADC, UART, SPI, and I²C signals use 3.3 V logic. Do not apply 5 V
  directly to an ESP32-S3 GPIO.
- Keep analog input voltage within the 3.3 V supply domain.
- Use a protected, compatible single-cell Li-ion/LiPo battery with the correct
  PH 2.0 connector polarity shown in the pinout.
- Turn the board off before changing wiring or inserting/removing a microSD
  card.
- The 5 V expansion pin is a power rail, not a 5 V-tolerant logic reference.

### **2.3 Power Paths**

The board can be powered from USB-C or the battery connector. The AP2112K LDO
provides the 3.3 V rail. The power switch controls normal board operation, while
the onboard charge circuit supports battery charging from USB-C. The red PWR
and amber CHRG indicators show power and charging state respectively.
