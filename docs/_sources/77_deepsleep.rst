Deep Sleep Mode
===============

Overview
--------
The ESP32-S3 Deep Sleep mode is an ultra-low power state that significantly reduces power consumption 
by shutting down most of the chip's components, including the CPU, most RAM, and digital peripherals. 
In this mode, only the RTC (Real-Time Clock) controller, RTC peripherals, and RTC memory remain powered, 
allowing the device to wake up from various sources while consuming minimal power (typically around 5-10 µA).

Deep Sleep is ideal for battery-powered applications that need to operate for extended periods with 
minimal power consumption, such as IoT sensors, wearables, and remote monitoring devices.

Features
--------
* **Ultra-low power consumption**: ~5-10 µA in deep sleep mode
* **Multiple wake-up sources**: External GPIO, timers, touch pads, ULP coprocessor
* **RTC memory retention**: Preserve data across sleep cycles
* **Fast wake-up**: Resume execution quickly from sleep state
* **Configurable wake conditions**: Flexible wake-up triggers
* **Power domain control**: Selective power management for different chip regions

Deep Sleep Wake-up Sources
---------------------------

The ESP32-S3 supports multiple wake-up sources that can bring the chip out of deep sleep:

.. list-table:: Wake-up Sources
   :header-rows: 1
   :widths: 20 30 50

   * - Wake Source
     - Function
     - Description
   * - **EXT0**
     - ``esp_sleep_enable_ext0_wakeup()``
     - Wake up using a single RTC GPIO pin (level-triggered: HIGH or LOW)
   * - **EXT1**
     - ``esp_sleep_enable_ext1_wakeup()``
     - Wake up using multiple RTC GPIO pins (supports AND/OR logic)
   * - **Timer**
     - ``esp_sleep_enable_timer_wakeup()``
     - Wake up after a specified time period (microseconds)
   * - **Touch Pad**
     - ``esp_sleep_enable_touchpad_wakeup()``
     - Wake up when touch sensor detects a touch event
   * - **ULP**
     - ``esp_sleep_enable_ulp_wakeup()``
     - Wake up by Ultra-Low-Power coprocessor program
   * - **GPIO**
     - ``esp_deep_sleep_enable_gpio_wakeup()``
     - Wake up using GPIO pins (ESP32-S3 specific)

GPIO Features and Capabilities
-------------------------------

RTC GPIO Pins (Deep Sleep Wake-up Capable)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The ESP32-S3 has specific GPIO pins that are connected to the RTC domain and can be used 
as wake-up sources during deep sleep. These pins maintain their state and can trigger wake-up events.

.. list-table:: ESP32-S3 RTC GPIO Pins
   :header-rows: 1
   :widths: auto

   * - GPIO
     - RTC GPIO
     - Wake Support
     - Additional Features
   * - GPIO0
     - RTC_GPIO0
     - EXT0/EXT1
     - Strapping pin, ADC1_CH0, TOUCH1
   * - GPIO1
     - RTC_GPIO1
     - EXT0/EXT1
     - ADC1_CH1, TOUCH2
   * - GPIO2
     - RTC_GPIO2
     - EXT0/EXT1
     - ADC1_CH2, TOUCH3, Strapping pin
   * - GPIO3
     - RTC_GPIO3
     - EXT0/EXT1
     - ADC1_CH3, TOUCH4
   * - GPIO4
     - RTC_GPIO4
     - EXT0/EXT1
     - ADC1_CH4, TOUCH5
   * - GPIO5
     - RTC_GPIO5
     - EXT0/EXT1
     - ADC1_CH5, TOUCH6
   * - GPIO6
     - RTC_GPIO6
     - EXT0/EXT1
     - ADC1_CH6, TOUCH7
   * - GPIO7
     - RTC_GPIO7
     - EXT0/EXT1
     - ADC1_CH7, TOUCH8
   * - GPIO8
     - RTC_GPIO8
     - EXT0/EXT1
     - ADC1_CH8, TOUCH9
   * - GPIO9
     - RTC_GPIO9
     - EXT0/EXT1
     - ADC1_CH9, TOUCH10
   * - GPIO10
     - RTC_GPIO10
     - EXT0/EXT1
     - ADC1_CH10, TOUCH11
   * - GPIO11
     - RTC_GPIO11
     - EXT0/EXT1
     - ADC2_CH0, TOUCH12
   * - GPIO12
     - RTC_GPIO12
     - EXT0/EXT1
     - ADC2_CH1, TOUCH13
   * - GPIO13
     - RTC_GPIO13
     - EXT0/EXT1
     - ADC2_CH2, TOUCH14
   * - GPIO14
     - RTC_GPIO14
     - EXT0/EXT1
     - ADC2_CH3, TOUCH15
   * - GPIO15
     - RTC_GPIO15
     - EXT0/EXT1
     - ADC2_CH4, XTAL_32K_P
   * - GPIO16
     - RTC_GPIO16
     - EXT0/EXT1
     - ADC2_CH5, XTAL_32K_N
   * - GPIO17
     - RTC_GPIO17
     - EXT0/EXT1
     - ADC2_CH6
   * - GPIO18
     - RTC_GPIO18
     - EXT0/EXT1
     - ADC2_CH7
   * - GPIO19
     - RTC_GPIO19
     - EXT0/EXT1
     - ADC2_CH8, USB D-
   * - GPIO20
     - RTC_GPIO20
     - EXT0/EXT1
     - ADC2_CH9, USB D+
   * - GPIO21
     - RTC_GPIO21
     - EXT0/EXT1
     - Can be used for RTC functions

GPIO Wake-up Modes
^^^^^^^^^^^^^^^^^^

.. list-table:: GPIO Wake-up Configuration
   :header-rows: 1
   :widths: 25 75

   * - Mode
     - Description
   * - **Level Triggered (EXT0)**
     - Wake up when a single GPIO reaches a specific level (HIGH=1 or LOW=0). 
       Simple and commonly used for button wake-up.
   * - **Level Triggered (EXT1)**
     - Wake up when multiple GPIOs meet certain conditions. Supports:
       
       - **ALL_LOW**: Wake when ALL selected pins are LOW
       - **ANY_HIGH**: Wake when ANY selected pin is HIGH
   * - **Edge Triggered (GPIO)**
     - Wake up on rising or falling edge of GPIO signal. More flexible but 
       requires ESP32-S3 specific API.

Power Consumption Comparison
-----------------------------

Understanding the power consumption in different modes helps optimize battery life:

.. list-table:: ESP32-S3 Power Consumption Modes
   :header-rows: 1
   :widths: 25 25 50

   * - Mode
     - Current Draw
     - Use Case
   * - **Active (WiFi TX)**
     - ~160-260 mA
     - Normal operation with WiFi transmitting
   * - **Active (WiFi RX)**
     - ~80-100 mA
     - WiFi receiving/listening
   * - **Modem Sleep**
     - ~20-30 mA
     - CPU active, WiFi/BT suspended
   * - **Light Sleep**
     - ~0.8-3 mA
     - CPU suspended, peripherals can wake it
   * - **Deep Sleep**
     - ~5-10 µA
     - Only RTC active, requires reset-like wake
   * - **Hibernation**
     - ~2-5 µA
     - Minimal power, limited wake sources

Complete Implementation Example
--------------------------------

This example demonstrates a power-efficient button interface that uses deep sleep to conserve 
battery life. The system monitors a button and enters deep sleep after 10 seconds of continuous 
press, then wakes up when the button is released.

Button-Controlled Deep Sleep with Visual Feedback
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Application Description:**

- **Normal Operation**: Button clicks are detected and can be used for UI interaction
- **Long Press Detection**: Holding the button for 10 seconds triggers deep sleep
- **Wake-up Indication**: LED blinks 3 times upon waking from deep sleep
- **Power Saving**: System enters ultra-low power mode (~5-10 µA) when sleeping
- **Smart Wake-up**: Wakes automatically when button is released (transitions to HIGH)

**Hardware Connections:**

- **GPIO11**: Button input with internal pull-up (button connects to GND when pressed)
- **GPIO7**: LED output for visual feedback (active HIGH)

.. code-block:: c++

    #include "esp_sleep.h"

    #define BUTTON_PIN 11         // Button / Switch pin
    #define WAKE_PIN  GPIO_NUM_11 // Wake from deep sleep (HIGH level trigger)
    #define LED_PIN   7           // LED for visual feedback

    unsigned long pressStart = 0;
    bool isPressed = false;

    /**
     * @brief Blink LED to indicate wake-up from deep sleep
     * 
     * Provides visual feedback that the system has successfully
     * woken up from deep sleep mode.
     */
    void blinkWake() {
      for (int i = 0; i < 3; i++) {
        digitalWrite(LED_PIN, HIGH);
        delay(250);
        digitalWrite(LED_PIN, LOW);
        delay(250);
      }
    }

    void setup() {
      Serial.begin(115200);
      delay(400);  // Allow serial to stabilize

      // Configure GPIO pins
      pinMode(BUTTON_PIN, INPUT_PULLUP); // Button connects to GND when pressed
      pinMode(LED_PIN, OUTPUT);
      digitalWrite(LED_PIN, LOW);

      // Check what caused the wake-up
      esp_sleep_wakeup_cause_t cause = esp_sleep_get_wakeup_cause();
      
      if (cause == ESP_SLEEP_WAKEUP_EXT0) {
        // Woke up because button was released (GPIO went HIGH)
        Serial.println("=======================================");
        Serial.println("  Woke up from Deep Sleep!");
        Serial.println("  Trigger: GPIO11 (Button Released)");
        Serial.println("=======================================");
        blinkWake();   // Visual wake-up indication
      } else {
        // Normal power-on or reset
        Serial.println("=======================================");
        Serial.println("  Normal Boot - System Ready");
        Serial.println("  Press button for 10s to enter sleep");
        Serial.println("=======================================");
      }

      // Configure wake-up source: Wake when GPIO11 goes HIGH (button released)
      // This allows the button to be held LOW during sleep and wake on release
      esp_sleep_enable_ext0_wakeup(WAKE_PIN, 1);  // 1 = Wake on HIGH level
      
      Serial.println("\nMonitoring button state...\n");
    }

    void loop() {
      int btn = digitalRead(BUTTON_PIN);
      
      // ===============================================================
      // BUTTON PRESS DETECTION
      // ===============================================================
      if (btn == LOW && !isPressed) {
        // Button just pressed (went LOW)
        isPressed = true;
        pressStart = millis();
        Serial.println("Button PRESSED");
        Serial.println("   Hold for 10 seconds to enter deep sleep...");
      }

      // ===============================================================
      // BUTTON RELEASE DETECTION (Short Press)
      // ===============================================================
      if (btn == HIGH && isPressed) {
        // Button released before 10 seconds
        isPressed = false;
        unsigned long pressDuration = millis() - pressStart;
        
        Serial.print("Button RELEASED (");
        Serial.print(pressDuration);
        Serial.println(" ms)");
        Serial.println("   -> Short press detected - UI interaction");
        Serial.println("   -> You can handle your UI/images here\n");
        
        // Handle your button click event here
        // Example: Change display, toggle feature, etc.
      }

      // ===============================================================
      // LONG PRESS DETECTION - ENTER DEEP SLEEP
      // ===============================================================
      if (isPressed && btn == LOW) {
        unsigned long elapsed = millis() - pressStart;
        
        // Update progress every second
        static unsigned long lastUpdate = 0;
        if (elapsed - lastUpdate >= 1000) {
          lastUpdate = elapsed;
          Serial.print("Holding button: ");
          Serial.print(elapsed / 1000);
          Serial.println(" seconds...");
        }
        
        // Check if 10 seconds elapsed
        if (elapsed >= 10000) {
          // Long press detected - enter deep sleep
          Serial.println("\n=======================================");
          Serial.println("  LONG PRESS DETECTED!");
          Serial.println("  Entering Deep Sleep Mode...");
          Serial.println("  System will wake when button released");
          Serial.println("  Power consumption: ~5-10 uA");
          Serial.println("=======================================");
          
          delay(300);  // Allow serial to flush
          
          // Enter deep sleep
          // System stays asleep while button is held LOW
          // Wakes automatically when button is released (goes HIGH)
          esp_deep_sleep_start();
        }
      }

      delay(20);  // Small delay to debounce and reduce CPU load
    }

Code Explanation
^^^^^^^^^^^^^^^^

**Wake-up Configuration:**

.. code-block:: c++

    esp_sleep_enable_ext0_wakeup(WAKE_PIN, 1);

- Configures GPIO11 as wake-up source
- Parameter ``1`` means wake on HIGH level
- Button held LOW keeps device asleep
- Releasing button (goes HIGH) triggers wake-up

**Button State Machine:**

1. **Idle State**: Button HIGH (not pressed), waiting for press
2. **Pressed State**: Button LOW, timer starts counting
3. **Short Release**: Button released before 10s → Normal UI interaction
4. **Long Press**: Button held for 10s → Enter deep sleep
5. **Wake-up**: Button released during sleep → System wakes and blinks LED

**Power Optimization Strategy:**

- **Active Mode**: Only when monitoring button (20-30 mA)
- **Deep Sleep**: After long press (~5-10 µA)
- **Battery Savings**: ~99.97% reduction in power consumption during sleep

Alternative Wake-up Methods
----------------------------

Timer-Based Wake-up
^^^^^^^^^^^^^^^^^^^

Wake up after a specific time period (useful for periodic sensor readings):

.. code-block:: c++

    #define uS_TO_S_FACTOR 1000000ULL  // Conversion factor for micro to seconds
    #define TIME_TO_SLEEP  30          // Sleep for 30 seconds

    void setup() {
      // Configure timer wake-up
      esp_sleep_enable_timer_wakeup(TIME_TO_SLEEP * uS_TO_S_FACTOR);
      
      Serial.println("Going to sleep for 30 seconds");
      esp_deep_sleep_start();
    }

Multiple GPIO Wake-up (EXT1)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Wake up when multiple buttons are pressed:

.. code-block:: c++

    #define BUTTON1 GPIO_NUM_11
    #define BUTTON2 GPIO_NUM_12
    #define BUTTON3 GPIO_NUM_13

    void setup() {
      // Wake when ANY button is pressed (goes HIGH)
      uint64_t mask = (1ULL << BUTTON1) | (1ULL << BUTTON2) | (1ULL << BUTTON3);
      esp_sleep_enable_ext1_wakeup(mask, ESP_EXT1_WAKEUP_ANY_HIGH);
      
      esp_deep_sleep_start();
    }

Touch Pad Wake-up
^^^^^^^^^^^^^^^^^

Wake up from capacitive touch sensor:

.. code-block:: c++

    #include "driver/touch_pad.h"

    #define TOUCH_THRESH  40  // Threshold for touch detection

    void setup() {
      // Initialize touch pad
      touch_pad_init();
      touch_pad_set_voltage(TOUCH_HVOLT_2V7, TOUCH_LVOLT_0V5, TOUCH_HVOLT_ATTEN_1V);
      
      // Configure touch pad 9 (GPIO9) as wake source
      touch_pad_config(TOUCH_PAD_NUM9, TOUCH_THRESH);
      
      // Enable touch pad wake-up
      esp_sleep_enable_touchpad_wakeup();
      
      esp_deep_sleep_start();
    }

Best Practices
--------------

1. **Always flush serial output before sleep:**

   .. code-block:: c++

       Serial.println("Going to sleep...");
       Serial.flush();  // Wait for transmission to complete
       delay(100);
       esp_deep_sleep_start();

2. **Use RTC memory to preserve data across sleep cycles:**

   .. code-block:: c++

       RTC_DATA_ATTR int bootCount = 0;  // Preserved in RTC memory
       
       void setup() {
         bootCount++;
         Serial.printf("Boot number: %d\n", bootCount);
       }

3. **Disable unnecessary peripherals before sleep:**

   .. code-block:: c++

       // Disable WiFi and Bluetooth
       WiFi.disconnect(true);
       WiFi.mode(WIFI_OFF);
       btStop();

4. **Consider wake-up latency (~100-500 ms)** for time-critical applications

5. **Test current consumption** with a multimeter to verify sleep mode operation

6. **Use appropriate pull-up/pull-down resistors** on wake-up GPIO pins

7. **Handle wake-up causes** to provide appropriate behavior based on wake source

Troubleshooting
---------------

**Device doesn't wake up:**

- Verify GPIO is RTC-capable (see GPIO table above)
- Check wake-up level configuration (HIGH vs LOW)
- Ensure external circuitry doesn't hold pin in sleep state
- Verify internal pull-up/pull-down configuration

**High current consumption in sleep:**

- Disable WiFi/BT before sleeping
- Check for peripherals keeping chip awake
- Verify GPIO states (floating pins consume power)
- Use deep sleep isolation for unused pins

**Unexpected wake-ups:**

- Add debouncing to wake-up GPIO
- Check for noise on wake-up lines
- Verify wake-up conditions (EXT1 ANY_HIGH vs ALL_LOW)
- Ensure stable power supply

API Reference
-------------

Key Functions
^^^^^^^^^^^^^

.. code-block:: c++

    // Enable wake-up sources
    esp_err_t esp_sleep_enable_ext0_wakeup(gpio_num_t gpio_num, int level);
    esp_err_t esp_sleep_enable_ext1_wakeup(uint64_t mask, esp_sleep_ext1_wakeup_mode_t mode);
    esp_err_t esp_sleep_enable_timer_wakeup(uint64_t time_in_us);
    esp_err_t esp_sleep_enable_touchpad_wakeup();
    esp_err_t esp_deep_sleep_enable_gpio_wakeup(uint64_t mask, esp_deepsleep_gpio_wake_up_mode_t mode);
    
    // Enter sleep
    void esp_deep_sleep_start();
    void esp_light_sleep_start();
    
    // Check wake-up cause
    esp_sleep_wakeup_cause_t esp_sleep_get_wakeup_cause();
    
    // Disable wake-up sources
    esp_err_t esp_sleep_disable_wakeup_source(esp_sleep_source_t source);

Wake-up Causes
^^^^^^^^^^^^^^

.. code-block:: c++

    typedef enum {
        ESP_SLEEP_WAKEUP_UNDEFINED,    // Not from sleep
        ESP_SLEEP_WAKEUP_ALL,          // Not a wake-up cause
        ESP_SLEEP_WAKEUP_EXT0,         // Wake by external signal (RTC_IO)
        ESP_SLEEP_WAKEUP_EXT1,         // Wake by external signal (RTC_CNTL)
        ESP_SLEEP_WAKEUP_TIMER,        // Wake by timer
        ESP_SLEEP_WAKEUP_TOUCHPAD,     // Wake by touchpad
        ESP_SLEEP_WAKEUP_ULP,          // Wake by ULP program
        ESP_SLEEP_WAKEUP_GPIO,         // Wake by GPIO
        ESP_SLEEP_WAKEUP_UART,         // Wake by UART
        ESP_SLEEP_WAKEUP_WIFI,         // Wake by WiFi
        ESP_SLEEP_WAKEUP_COCPU,        // Wake by COCPU int
        ESP_SLEEP_WAKEUP_COCPU_TRAP_TRIG,  // Wake by COCPU crash
        ESP_SLEEP_WAKEUP_BT           // Wake by BT
    } esp_sleep_wakeup_cause_t;

See Also
--------

* `ESP32-S3 Technical Reference Manual - Sleep Modes <https://www.espressif.com/sites/default/files/documentation/esp32-s3_technical_reference_manual_en.pdf>`_
* `ESP-IDF Deep Sleep Documentation <https://docs.espressif.com/projects/esp-idf/en/latest/esp32s3/api-reference/system/sleep_modes.html>`_
* `ESP32-S3 Low Power Design Guidelines <https://www.espressif.com/sites/default/files/documentation/esp32-s3_low_power_design_guide_en.pdf>`_
* :doc:`11_gpio` - GPIO Configuration and Usage
* :doc:`22_adc` - ADC with Low Power Modes