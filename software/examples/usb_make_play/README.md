# USB HID Keyboard with Touch Sensors

This Arduino sketch transforms your ESP32-S3 TouchDot board into a USB HID keyboard using capacitive touch sensors. Touch the designated pads to send arrow keys and space bar commands to your computer - perfect for gaming, presentations, or accessibility applications.

## Overview

The code implements a touch-based keyboard interface that detects when you touch specific GPIO pins and sends corresponding keystrokes via USB HID. It uses the ESP32-S3's built-in capacitive touch sensing capability with crocodile clips for easy connection.

## Features

- **USB HID Keyboard Emulation**: Acts as a standard USB keyboard
- **5 Touch Input Keys**: Arrow keys (Up, Down, Left, Right) + Space bar
- **Visual Feedback**: LED indicator shows when any key is being touched
- **Automatic Calibration**: Self-calibrates touch baselines on startup
- **Manual Recalibration**: Hold Space for 3 seconds to recalibrate
- **Debouncing**: Built-in filtering to prevent false triggers
- **Baseline Tracking**: Optional slow adjustment to environmental changes

## Hardware Setup

### Required Components

- ESP32-S3 TouchDot board
- 6 crocodile clips (alligator clips)
- USB-C cable for connection to computer

### Pin Mapping

| Touch Pin | GPIO | Function | HID Key |
|-----------|------|----------|---------|
| T_UP      | GPIO1  | Up Arrow | `KEY_UP_ARROW` |
| T_DOWN    | GPIO2  | Down Arrow | `KEY_DOWN_ARROW` |
| T_LEFT    | GPIO3  | Left Arrow | `KEY_LEFT_ARROW` |
| T_RIGHT   | GPIO4  | Right Arrow | `KEY_RIGHT_ARROW` |
| T_SPACE   | GPIO11 | Space Bar | `' '` (Space) |
| LED       | GPIO7  | Status LED | Visual feedback |

### Connection Method

1. **Ground Reference**: Connect one crocodile clip to any GND pin on the board. This clip should touch your hand or body while using the device.

2. **Touch Pads**: Connect the other 5 crocodile clips to the corresponding GPIO pins (1, 2, 3, 4, 11).

3. **Usage**: Hold the GND clip in one hand and touch the other clips with your free hand to trigger keypresses.

```
[GND Clip] → Your hand/body (ground reference)
     ↓
[Touch Clips] → GPIO1, GPIO2, GPIO3, GPIO4, GPIO11
     ↓
   Touch to activate
```

## How It Works

### Touch Detection Algorithm

1. **Baseline Calibration**: On startup, the system measures the untouched capacitance value for each pin
2. **Threshold Detection**: A touch is detected when the capacitance drops by at least 20% AND by a minimum of 150 counts
3. **Debouncing**: Readings are averaged (6 samples) and scanned every 12ms to filter noise
4. **State Tracking**: Only generates key press/release events when state changes

### Key Parameters

```cpp
const int CAL_SAMPLES = 80;          // Calibration samples (higher = more stable)
const float THRESH_DROP = 0.20;      // 20% drop from baseline to detect touch
const uint16_t MIN_DELTA = 150;      // Minimum absolute drop in counts
const int DEBOUNCE_MS = 12;          // Scan period (milliseconds)
const int AVG_SAMPLES = 6;           // Samples averaged per reading
```

### Calibration Process

**Automatic (on startup):**
- Don't touch any pads during the first ~320ms after power-on
- The system will measure baseline capacitance for each pin

**Manual Recalibration:**
- Hold the SPACE touch pad for 3+ seconds
- Useful if environmental conditions change or sensors drift

## Usage Examples

### Gaming Controller

Play keyboard-controlled games using touch inputs:
- Arrow keys for movement/navigation
- Space for jump/action

### Presentation Remote

Control presentation software:
- Arrow keys for slide navigation
- Space to play/pause

### Accessibility Interface

Create custom touch-based input methods for users with mobility limitations.

## Installation

1. **Install Arduino IDE** (1.8.19 or newer) or use PlatformIO

2. **Install ESP32 Board Support**:
   - Add to Board Manager URLs: `https://espressif.github.io/arduino-esp32/package_esp32_index.json`
   - Install "esp32" by Espressif Systems (v3.0.0 or newer)

3. **Board Settings**:
   - Board: "ESP32-S3 Dev Module"
   - USB CDC On Boot: "Enabled"
   - USB Mode: "USB-OTG (TinyUSB)"
   - Port: Select your ESP32-S3 device

4. **Upload the Sketch**:
   - Open `usb_make_play.ino`
   - Click Upload
   - Wait for "Done uploading" message

5. **Connect to Computer**:
   - The board will enumerate as a USB HID keyboard
   - No drivers needed (works on Windows, Mac, Linux)

## Configuration

### Adjusting Sensitivity

If touches aren't detected or are too sensitive:

```cpp
// More sensitive (easier to trigger)
const float THRESH_DROP = 0.15;      // Reduce threshold to 15%
const uint16_t MIN_DELTA = 100;      // Lower minimum delta

// Less sensitive (harder to trigger, fewer false positives)
const float THRESH_DROP = 0.25;      // Increase threshold to 25%
const uint16_t MIN_DELTA = 200;      // Higher minimum delta
```

### Changing Key Mappings

Modify the `keys[]` array to assign different HID keys:

```cpp
struct TouchKey {
    int tpin;        // Touch GPIO pin
    int keycode;     // HID key code
    uint16_t base;   // Calibrated baseline
    bool prev;       // Previous state
} keys[] = {
    {T_UP, 'W', 0, false},           // Map to 'W' key
    {T_DOWN, 'S', 0, false},         // Map to 'S' key
    {T_LEFT, 'A', 0, false},         // Map to 'A' key
    {T_RIGHT, 'D', 0, false},        // Map to 'D' key
    {T_SPACE, KEY_RETURN, 0, false}, // Map to Enter key
};
```

Available HID key constants include:
- `KEY_UP_ARROW`, `KEY_DOWN_ARROW`, `KEY_LEFT_ARROW`, `KEY_RIGHT_ARROW`
- `KEY_RETURN` (Enter), `KEY_ESC`, `KEY_TAB`, `KEY_BACKSPACE`
- `'a'` to `'z'`, `'0'` to `'9'`
- `KEY_F1` to `KEY_F12`

### LED Pin

If your board uses a different LED pin:

```cpp
const int PIN_LED = 48;  // Change to your LED GPIO
```

## Debugging

Enable serial debug output by uncommenting this line in the main loop:

```cpp
Serial.printf("pin %d v=%u base=%u thr=%u %s\n", 
              k.tpin, v, k.base, relThr, isPressed?"P":"-");
```

Then open Serial Monitor (115200 baud) to see:
- Current capacitance values
- Baseline values
- Threshold calculations
- Press/release events

## Troubleshooting

### Keys Not Detected

1. **Calibration Issue**: Make sure you're not touching any pads during startup
2. **Poor Ground Connection**: Ensure the GND clip is making good contact with your skin
3. **Sensitivity Too Low**: Adjust `THRESH_DROP` to a lower value (e.g., 0.15)

### False Triggers / Too Sensitive

1. **Electrical Noise**: Keep cables short and away from power sources
2. **Increase Threshold**: Set `THRESH_DROP` to 0.25 or higher
3. **Increase Min Delta**: Set `MIN_DELTA` to 200 or higher

### Computer Doesn't Recognize Device

1. **USB Mode**: Verify USB Mode is set to "USB-OTG (TinyUSB)"
2. **CDC On Boot**: Enable "USB CDC On Boot"
3. **Cable**: Try a different USB cable (must support data, not just power)
4. **Drivers**: On Windows, ensure ESP32-S3 drivers are installed

### Drift Over Time

Enable baseline tracking to slowly adapt to environmental changes:

```cpp
const int BASELINE_TRACK_SHIFT = 3;  // Enable slow tracking
```

## API Reference

### Main Functions

```cpp
void calibrate()
```
Measures baseline capacitance for all touch pins. Call during startup or when recalibration is needed.

```cpp
uint16_t touchAvg(int pin, int n = AVG_SAMPLES)
```
Returns averaged touch reading from specified GPIO pin.

```cpp
bool touched(const TouchKey &k, uint16_t current, uint16_t &relThr)
```
Determines if a touch pad is currently being touched based on threshold logic.

### TinyUSB Keyboard Methods

```cpp
Keyboard.begin()        // Initialize USB HID keyboard
Keyboard.press(key)     // Press and hold a key
Keyboard.release(key)   // Release a key
```

## Performance

- **Scan Rate**: ~83 Hz (12ms debounce period)
- **Latency**: <15ms from touch to HID event
- **CPU Usage**: Minimal (<1% on ESP32-S3)
- **Power Draw**: ~80-100mA (active USB connection)

## License

This code is provided as-is for educational and commercial use. Modify and distribute freely.

## See Also

- [ESP32-S3 Touch Sensor Documentation](https://docs.espressif.com/projects/esp-idf/en/latest/esp32s3/api-reference/peripherals/touch_pad.html)
- [Arduino USB HID Library](https://github.com/espressif/arduino-esp32/tree/master/libraries/USB)
- ESP32-S3 TouchDot Board Pinout

## Contributing

Found a bug or have an improvement? Submit an issue or pull request to the repository.

---

**Author**: UNIT Electronics  
**Board**: ESP32-S3 TouchDot  
**Last Updated**: December 2025
