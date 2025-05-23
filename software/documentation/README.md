---
title: "S3 Development Board"
version: "1.0"
modified: "2025-04-30"
output: "s3_development_board"
subtitle: "ESP32-S3 development board with 2.4GHz Wi-Fi and Bluetooth 5.0"
---

<!--
# README_TEMPLATE.md
Este archivo sirve como entrada para generar un PDF técnico estilo datasheet.
Edita las secciones respetando el orden, sin eliminar los encabezados.
-->

# ESP32-S3 Development Board 

![product](./images/product.jpg)

## Introduction

Unit TouchDot S3 is a compact development board powered by the versatile ESP32-S3 chip, engineered for IoT, AI, and machine learning applications. Its design integrates the efficient ESP32-S3 Mini microcontroller—with low power consumption and an optional PSRAM configuration—to support both basic sensor projects and advanced prototypes. Additionally, the 3.3V power rail facilitates seamless connectivity with low-voltage components such as LilyPad and QWIIC sensors.

## Functional Description

- Integrated ESP32-S3 module with Wi-Fi and Bluetooth 5.0
- USB-C for power and programming
- 3.3V power rail compatible with low-voltage peripherals
- Built-in QWIIC connector for rapid sensor integration

## Electrical Characteristics & Signal Overview

- Operating voltage: 3.3V
- Max current draw: 500mA (with Wi-Fi active)
- GPIO logic level: 3.3V
- ADC resolution: 12-bit (0–4095)
- Touchpad sensitivity: configurable

## Applications

- IoT sensor nodes
- Smart home automation
- Environmental monitoring
- Educational prototyping platforms

## Features

- ESP32-S3 with dual-core Xtensa® processor
- Integrated 2.4GHz Wi-Fi and Bluetooth LE
- 11 capacitive touchpads
- 8 ADC channels
- Optional PSRAM support
- USB device and host support

## Pin & Connector Layout

| Group     | Availables pins | Suggested use                          |
|-----------|-----------------|----------------------------------------|
| GPIO      | D2 to D13       | Sensors, actuators                     |
| UART      | Tx and Rx       | Serial communication                   |
| TouchPad  | T1 to T11       | Capacitive sensors for touch detection |
| Analogic  | A0 to A8        | 12-bit (0–4095) resolution             |
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

![Function Diagram](images/pinout.jpg)

## Dimensions

![Dimensions](images/dimensions.jpg)

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
