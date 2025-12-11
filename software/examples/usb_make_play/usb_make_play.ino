#include "USB.h"
#include "USBHIDKeyboard.h"

USBHIDKeyboard Keyboard;

// ---------------- Pines táctiles (ver pinout Touchdot S3) ----------------
// Usa caimanes: 1 clip a GND (mano/persona) y otro al pad del pin táctil.
const int T_UP = 1;      // GPIO1 -> Flecha Arriba
const int T_DOWN = 2;    // GPIO2 -> Flecha Abajo
const int T_LEFT = 3;    // GPIO3 -> Flecha Izquierda
const int T_RIGHT = 4;   // GPIO4 -> Flecha Derecha
const int T_SPACE = 11;  // GPIO11 -> Barra Espaciadora

// LED de estado (ajusta si usas otro LED)
const int PIN_LED = 7;  // Enciende si cualquier tecla está "tocada"

// ---------------- Mapa de teclas HID ----------------
struct TouchKey {
    int tpin;        // GPIO táctil
    int keycode;     // KEY_... o ' '
    uint16_t base;   // baseline calibrada
    bool prev;       // estado previo
} keys[] = {
        {T_UP, KEY_UP_ARROW, 0, false},
        {T_DOWN, KEY_DOWN_ARROW, 0, false},
        {T_LEFT, KEY_LEFT_ARROW, 0, false},
        {T_RIGHT, KEY_RIGHT_ARROW, 0, false},
        {T_SPACE, ' ', 0, false},
};

const uint8_t NKEYS = sizeof(keys) / sizeof(keys[0]);

// ---------------- Parámetros de touch (afinados para caimanes) ----------------
const int CAL_SAMPLES = 80;          // muestras para baseline (más alto = más estable)
const float THRESH_DROP = 0.20;      // % de caída vs baseline para "tocado" (0.20=20%)
const uint16_t MIN_DELTA = 150;      // caída absoluta mínima en cuentas (80–400 típico)
const int DEBOUNCE_MS = 12;          // periodo de escaneo / debouncing
const int AVG_SAMPLES = 6;           // promedio por lectura en runtime

// (Opcional) seguimiento lento del baseline cuando NO está tocado (0=off, 8≈filtro 1/8)
const int BASELINE_TRACK_SHIFT = 0;  // 0 = desactivado; 3..5 = ajuste muy lento

// ---------------- Estado global ----------------
uint32_t lastScanMs = 0;
uint32_t spaceDownMs = 0;  // para detectar SPACE mantenido y recalibrar

// ---------------- Utilidades ----------------
uint16_t touchAvg(int pin, int n = AVG_SAMPLES) {
    uint32_t acc = 0;
    for (int i = 0; i < n; ++i)
        acc += touchRead(pin);
    return (uint16_t)(acc / n);
}

void calibrate() {
    // No tocar pads durante esta fase
    for (auto &k : keys) {
        uint32_t acc = 0;
        for (int i = 0; i < CAL_SAMPLES; ++i) {
            acc += touchRead(k.tpin);
            delay(4);
        }
        k.base = (uint16_t)(acc / CAL_SAMPLES);
    }
}

bool touched(const TouchKey &k, uint16_t current, uint16_t &relThr) {
    // Umbral relativo + delta absoluto
    relThr = (uint16_t)(k.base * (1.0f - THRESH_DROP));
    bool relOk = current < relThr;
    bool absOk = (k.base > current) && ((k.base - current) >= MIN_DELTA);
    return relOk && absOk;
}

// ---------------- Setup ----------------
void setup() {
    pinMode(PIN_LED, OUTPUT);
    digitalWrite(PIN_LED, LOW);

    USB.begin();       // TinyUSB
    Keyboard.begin();  // HID Teclado

    delay(300);
    calibrate();
}

// ---------------- Loop ----------------
void loop() {
    if (millis() - lastScanMs < (uint32_t)DEBOUNCE_MS)
        return;
    lastScanMs = millis();

    bool anyPressed = false;
    bool isSpaceNow = false;

    for (auto &k : keys) {
        uint16_t v = touchAvg(k.tpin, AVG_SAMPLES);
        uint16_t relThr = 0;
        bool isPressed = touched(k, v, relThr);

        // Seguimiento lento de baseline cuando no está presionado
        if (!isPressed && BASELINE_TRACK_SHIFT > 0) {
            // k.base = k.base*(1 - alpha) + v*alpha, con alpha = 1/2^shift
            k.base = (uint16_t)((((uint32_t)k.base << BASELINE_TRACK_SHIFT) - k.base + v) >> BASELINE_TRACK_SHIFT);
        }

        // Generar eventos HID solo en cambio de estado
        if (isPressed && !k.prev) {
            Keyboard.press(k.keycode);
        } else if (!isPressed && k.prev) {
            Keyboard.release(k.keycode);
        }

        if (k.keycode == ' ')
            isSpaceNow = isPressed;
        k.prev = isPressed;
        anyPressed |= isPressed;

        // (Opcional) — descomenta para depurar por Serial:
        // Serial.printf("pin %d v=%u base=%u thr=%u %s\n", k.tpin, v, k.base, relThr, isPressed?"P":"-");
    }

    // Recalibración manteniendo SPACE ~3 s
    if (isSpaceNow) {
        if (spaceDownMs == 0)
            spaceDownMs = millis();
        else if (millis() - spaceDownMs > 3000) {
            calibrate();
            spaceDownMs = 0;  // evita recalibraciones repetidas
        }
    } else {
        spaceDownMs = 0;
    }

    digitalWrite(PIN_LED, anyPressed ? HIGH : LOW);
}