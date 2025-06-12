.. STM32 Getting Started documentation master file, created by
   sphinx-quickstart on Thu Mar 13 11:22:00 2025.

TouchDot development board 
==========================

.. note::

   This documentation is actively evolving. For the latest updates and revisions,
   please visit the project's GitHub repository.


Leveraging the ESP32-S3 chip, the Touchdot S3 is a versatile development board crafted for creative wearables, IoT implementations, and smart devices. Inspired by the Lilypad aesthetic but delivering modern functionality, it marries a compact form factor with robust connectivity and power management features for seamless prototyping.

**Microcontroller: ESP32-S3 Mini**



- **Energy Efficient:** Optimized for low power consumption.
- **3.3 V Power Rail:** Compatible with wearable sensors and peripherals like QWIIC modules.

**Power Supply & Battery Management**

- **USB-C Charging & Communication:** Ensures reliable power delivery and straightforward programming.
- **Integrated LiPo Battery Management:** Streamlines power safety and efficiency without extra circuitry.
- **Distributed Power Pads:** Magnetic connectors deliver **GND** and **3.3 V** for simple, reliable wiring to sensors and actuators.

**Key Features**

.. list-table::
   :header-rows: 1

   * - **Feature**
     - **Description**
   * - Wi-Fi & Bluetooth LE
     - Dual wireless connectivity for seamless IoT and mobile interactions.
   * - Built-in LiPo Charging
     - Reliable battery charging integrated into the board design.
   * - Power & Reset Controls
     - Direct access to board power management with dedicated buttons for power and reset.
   * - Sewable Pads & Magnetic Connectors
     - Ideal for wearable projects and rapid prototyping with flexible module integration.
   * - Multiple Solder Points for GND & 3.3 V
     - Facilitates easy wiring to external sensors or actuators without complex setup.
   * - Standard QWIIC Connector
     - Supports quick connection of I²C peripherals such as sensors, displays, and expansion modules.

.. toctree::
   :maxdepth: 2
   :caption: Contents

   00_1_terms
   01_0_map
   01_1_tech
   01_setup
   02_lib
   02_1_esp-idf

   11_gpio
   22_adc
   33_i2c
   44_spi
   55_WS2812
   66_communication

   
   report
   
   




