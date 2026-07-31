## **5 Board Operation**

### **5.1 First Power-Up**

1. Inspect the board for damage, debris, or shorts.
2. With the power switch off, connect a data-capable USB-C cable to a computer
   or regulated 5 V USB supply.
3. Move the power switch to ON. The PWR indicator should illuminate.
4. Select an ESP32-S3 target in the chosen development environment and select
   the board's USB serial port.
5. If automatic download mode does not start, hold **Boot**, momentarily press
   **Reset**, and then release **Boot**.

### **5.2 Arduino LED Test**

The following sketch checks the user LED on D13/GPIO7. GPIO7 is also the
microSD clock, so do not run this test while accessing a card.

```cpp
constexpr int LED_PIN = 7;

void setup() {
  pinMode(LED_PIN, OUTPUT);
}

void loop() {
  digitalWrite(LED_PIN, HIGH);
  delay(500);
  digitalWrite(LED_PIN, LOW);
  delay(500);
}
```

### **5.3 QWIIC / I²C Test**

The default documented I²C pins are SDA on GPIO5 and SCL on GPIO6. Confirm that
SB1 enables QWIIC VCC before expecting the connector to power a peripheral.

```cpp
#include <Wire.h>

void setup() {
  Serial.begin(115200);
  Wire.begin(5, 6);

  for (uint8_t address = 1; address < 127; ++address) {
    Wire.beginTransmission(address);
    if (Wire.endTransmission() == 0) {
      Serial.printf("I2C device: 0x%02X\n", address);
    }
  }
}

void loop() {}
```

### **5.4 microSD Use**

Use SPI pins CS=GPIO21, MOSI=GPIO9, MISO=GPIO8, and SCK=GPIO7. Format a
supported card with FAT32 before use. Because GPIO7 also drives the user LED
and GPIO7–9 are exposed on sewable pads, attached circuits must not contend
with the microSD bus.

### **5.5 Battery Operation**

Turn the board off before attaching a battery. Check connector polarity against
the released pinout, insert a compatible single-cell Li-ion/LiPo battery, and
then turn the power switch on. When USB-C is connected, the CHRG indicator may
illuminate while the onboard circuit charges the battery. Do not use a damaged,
swollen, reversed-polarity, or incompatible battery.

### **5.6 Shared-Pin Considerations**

The ESP32-S3 pin matrix permits multiple functions on a GPIO, but a physical pin
can only serve compatible roles at a given time. In particular:

- GPIO7 is D13, A6/T7, user LED, and microSD SCK.
- GPIO8 is D12, A7/T8, and microSD MISO.
- GPIO9 is D11, A8/T9, and microSD MOSI.
- GPIO21 is the microSD chip-select signal.
- GPIO5 and GPIO6 are the default QWIIC I²C bus.
- GPIO45 drives the onboard WS2812 and the NeoPixel chain-output pad.

Plan firmware and external wiring so these functions do not conflict.
