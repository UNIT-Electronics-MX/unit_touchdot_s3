Hardware Specifications
=========================

The TouchDot S3 development board is built around the ESP32-S3 Mini chip, offering a range of features tailored for wearables and IoT applications.






.. only:: html

   .. raw:: html

        <div style="text-align: center;">
            <h2 style="color: #4a90e2;">Schematic Diagram</h2>
            <button style="background-color: #87cefa; color: white; border: none; padding: 10px 20px;" 
                onclick="window.open('./_static/unit_sch_v_0_1_2_ue0072_touch_dot_s3.pdf', '_blank')">
            View Schematic (PDF)
            </button>
        </div>
        <br>
        <iframe src="./_static/unit_sch_v_0_1_2_ue0072_touch_dot_s3.pdf" style="width:100%; height:500px;" frameborder="0">
        </iframe>
        <br>



Pinout Distribution
--------------------


.. only:: latex


    .. figure::  /_static/touchdot/unit_pinout_v_0_1_3_ue0072_touch_dot_s3_en.png
        
        :align: center

        Dimension

.. only:: html

   .. raw:: html

      <div style="text-align: center;">
        <a href="./_static/touchdot/unit_pinout_v_0_1_3_ue0072_touch_dot_s3_en.png" target="_blank">
          <img 
            src="./_static/touchdot/unit_pinout_v_0_1_3_ue0072_touch_dot_s3_en.png" 
            alt="TouchDot S3 Pinout" 
            style="width: 90%; height: auto; border: 1px solid #ccc; border-radius: 8px;"
          >
        </a>
      </div>
      <br><br>





.. list-table:: PINOUT
   :widths: 25 25 50
   :header-rows: 1

   * - **Group**
     - **Available Pins**
     - **Suggested Use**
   * - **GPIO**
     - D2 to D13
     - Sensors, actuators
   * - **UART**
     - Tx and Rx
     - Serial communication
   * - **TouchPad**
     - T1 to T11
     - Capacitive sensors for touch detection
   * - **Analog**
     - A0 to A8
     - 12-bit (0–4095) resolution
   * - **SPI**
     - Optional
     - Displays, additional memory


Dimensions
----------

.. figure::  /_static/touchdot/unit_dimension_v_0_1_2_ue0072_touch_dot_s3.png
   :width: 500px
   :align: center

   Dimension



Topology
--------

.. figure:: /_static/touchdot/unit_topology_v_0_1_2_ue0072_touch_dot_s3.png
   :width: 500px
   :align: center

   Topology

.. list-table:: Topology
   :widths: 20 80
   :header-rows: 1

   * - Ref.
     - Description
   * - IC1
     - Espressif ESP32-S3
   * - U1
     - AP2112K 3.3V LDO Voltage Regulator
   * - PB1
     - Boot Push Button
   * - PB2
     - Reset Push Button
   * - SW1
     - Power On Switch
   * - L1
     - Power On LED
   * - L2
     - Charge On LED
   * - L3
     - Built-in LED (GPIO 6 or D13)
   * - L4
     - WS2812B-2020 LED
   * - SB1
     - Solder bridge to enable QWIIC VCC
   * - J1
     - Male USB Type-C Connector
   * - J2
     - Low-power I2C QWIIC JST Connector
   * - J3
     - PH2.0 mm Pitch Battery Connector
   * - J4
     - Micro SD Slot
   * - JP1
     - Sewable Pads
   * - JP2
     - Sewable Pads
   * - JP3
     - GPIO, system, and power supply pin headers
   * - JP4
     - GPIO, system, and power supply pin headers



.. only:: latex

   .. raw:: latex

      \clearpage
      \chapter*{Appendix A: Hardware Reference}
      \addcontentsline{toc}{chapter}{Appendix A: Hardware Reference}

      \section*{Schematic Diagram}
      \includepdf[pages=-]{unit_sch_V_0_1_2_ue0072_touch_dot_s3.pdf}

