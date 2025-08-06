---
title: "Touchdot S3 Development Board"
version: "1.0"
modified: "2025-04-23"
output: "touchdot_s3_development_board"
subtitle: "Compact ESP32-S3 mini microcontroller development board inspired by Lilypad. Ideal for IoT, control systems, and creative electronics projects."
---

<!--
# README_TEMPLATE.md
Este archivo sirve como entrada para generar un PDF técnico estilo datasheet.
Edita las secciones respetando el orden, sin eliminar los encabezados.
-->

# ESP32-S3 Development Board 

![product](../../hardware/resources/unit_top_V_0_1_2_ue0072_Touch-Dot-S3.png)

## Introduction
The Unit Touchdot S3 is a compact ESP32-S3 Mini board designed for wearable electronics, IoT devices, educational projects, and smart automation. Its Lilypad-inspired, low-profile, sewable design makes it perfect for integrating into textiles and compact enclosures while providing advanced wireless and processing capabilities.

Equipped with 2.4 GHz Wi-Fi, Bluetooth 5.0, and a modern interface featuring a USB-C connector, onboard LiPo charging, and a QWIIC I²C port, the board supports rapid prototyping and creative development. It offers a robust platform bridging wearable design and embedded computing, tailored for students, makers, and engineers.

## Functional Description

- Integrated ESP32-S3 module with 2.4 GHz Wi-Fi and Bluetooth 5.0
- USB-C connector for power and programming
- 3.3V power rail compatible with low-voltage peripherals
- Built-in QWIIC connector for easy I²C module integration
- Micro SD card slot using SPI interface
- Onboard NeoPixel (WS2812) RGB LED

## Electrical Characteristics & Signal Overview

- Operating voltage: 3.3V
- Max current draw: 500mA (with Wi-Fi active)
- GPIO logic level: 3.3V
- ADC resolution: 12-bit (0–4095)
- Touchpad sensitivity: configurable

## Applications

- Wearable electronics
- IoT sensor nodes
- Smart home and automation
- Educational tools for STEM (science, technology, engineering, and mathematics)
- Environmental monitoring
- Creative electronics and art-tech installations
- Smart Home
- Health Care


## Pin & Connector Layout

| Group     | Availables pins | Suggested use                          |
|-----------|-----------------|----------------------------------------|
| GPIO      | D2 to D13       | Sensors, actuators                     |
| UART      | Tx and Rx       | Serial communication                   |
| TouchPad  | T1 to T11       | Capacitive sensors for touch detection |
| Analog    | A0 to A8        | 12-bit (0–4095) resolution             |
| SPI       | Optional        | Displays, additional memory            |

## Settings

### Interface Overview

### Interface Overview

| Interface | Signals / Pins   | Typical Use                                 |
|-----------|------------------|---------------------------------------------|
| UART      | TX (GPIO17)      | Serial transmit (TX)                        |
| UART      | RX (GPIO16)      | Serial receive (RX)                         |
| I2C       | SDA (GPIO5)      | I²C data line (QWIIC, OLED, sensors)        |
| I2C       | SCL (GPIO6)      | I²C clock line                              |
| SPI       | MOSI (GPIO9)     | Data to SPI device                          |
| SPI       | MISO (GPIO8)     | Data from SPI device                        |
| SPI       | SCK (GPIO13)     | SPI clock signal                            |
| SPI       | CS (GPIO21)      | Chip select for SPI device                  |
| USB       | D+ (GPIO20)      | USB differential data (+)                   |
| USB       | D− (GPIO19)      | USB differential data (−)                   |


### Supports

| Symbol   | I/O           | Description                                       |
|----------|---------------|---------------------------------------------------|
| USB -C   | Input         | USB-C connector for 5V power and data             |
| Li-ion/LiPo     | Input         | Connector for LiPo battery power (3.7V - 4.2V)      |
| VCC      | Input         | Main power supply (3.3V)                           |
| GND      | Ground        | Ground connection                                |
| IO       | Bidirectional | General-purpose I/O pins                         |
| NeoPixel | Output    GPIO25    | WS2812 RGB LED data output                        |

## Block Diagram

![Function Diagram](../../hardware/resources/unit_pinout_top_v_0_2_0_ue0072_touch_dot_s3_en.png)

![Function Diagram](../../hardware/resources/unit_pinout_bottom_v_0_2_0_ue0072_touch_dot_s3_en.png)

## Dimensions

![Dimensions](../../hardware/resources/unit_dimension_V_0_1_2_ue0072_Touch-Dot-S3.png)

## Usage

Works with:

- Arduino IDE (ESP32 board manager)
- ESP-IDF toolchain
- MicroPython firmware
- CircuitPython (via UF2 bootloader)

## Downloads

- [Schematic PDF](https://github.com/UNIT-Electronics-MX/unit_touchdot_s3/tree/main/hardware#hardware)
- [Board Dimensions](https://github.com/UNIT-Electronics-MX/unit_touchdot_s3/tree/main/hardware#dimensions)
- [Pinout Diagram PNG](https://github.com/UNIT-Electronics-MX/unit_touchdot_s3/tree/main/hardware#pinout)

## Purchase

- [Buy from UNIT Electronics](https://www.uelectronics.com)
- [Open product page](https://github.com/UNIT-Electronics-MX/unit_touchdot_s3/tree/main)

