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

![product](./images/top.png)

## Introduction

The Unit Touchdot S3 is a compact and powerful development board based on the ESP32-S3 Mini, tailored for applications in wearable electronics, IoT devices, educational platforms, and smart automation. Inspired by the Lilypad design philosophy, it offers a low-profile, sewable form factor ideal for integration into textiles and compact enclosures, while delivering advanced wireless and processing capabilities.

Equipped with 2.4 GHz Wi-Fi and Bluetooth 5.0, the Touchdot S3 enables seamless communication with mobile devices, web services, and wireless sensor networks. Its modern interface includes a USB-C connector for programming and power delivery, onboard LiPo battery charging, and a standard QWIIC I²C port for rapid peripheral integration.

Designed for rapid prototyping and creative development, the Touchdot S3 bridges the gap between wearable design and embedded computing, offering a robust platform for students, makers, and engineers alike.

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
- Educational tools for STEM
- Environmental monitoring
- Creative electronics and art-tech installations
- Smart Home
- Industrial Automation
- Health Care
- Consumer Electronics
- Smart Agriculture
- POS Machines

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

| Interface  | Signals / Pins            | Typical Use                                         |
|------------|----------------------------|-----------------------------------------------------|
| UART       | Tx, Rx                     | Serial terminal or sensor communication            |
| I2C        | SDA, SCL                   | QWIIC modules, OLED displays                       |
| SPI        | MOSI, MISO, SCK, CS        | External flash, TFT display                        |
| USB        | D+, D-                     | Native USB device or host                          |

### Supports

| Symbol | I/O   | Description                         |
|--------|-------|-------------------------------------|
| VCC    | Input | Power supply (3.3V or 5V)           |
| GND    | GND   | Ground connection                   |
| IO     | Bidirectional | General-purpose I/O pins    |

## Block Diagram

![Function Diagram](images/pinout.png)

## Dimensions

![Dimensions](images/dimension.png)

## Usage

Works with:

- Arduino IDE (ESP32 board manager)
- PlatformIO (ESP32-S3 support)
- ESP-IDF toolchain
- MicroPython firmware
- CircuitPython (via UF2 bootloader)

## Downloads

- [Schematic PDF](docs/schematic.pdf)
- [Board Dimensions DXF](docs/dimensions.dxf)
- [Pinout Diagram PNG](docs/pinout.png)

## Purchase

- [Buy from UNIT Electronics](https://www.uelectronics.com)
- [Open product page](https://www.uelectronics.com/products/unit-lily-s3)
